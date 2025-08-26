#!/usr/bin/env python3
"""
API simplifiée pour le Startup Tokenization Marketplace
Utilise http.server au lieu de Flask pour éviter les dépendances
"""

import json
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from agents.market_agent import MarketAgent
from datetime import datetime
import sys
import os

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Instance globale du MarketAgent
market_agent = MarketAgent()

class MarketplaceHandler(BaseHTTPRequestHandler):
    """Gestionnaire HTTP pour l'API du marketplace"""
    
    def _set_headers(self, status_code=200, content_type='application/json'):
        """Configure les headers de la réponse"""
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def _send_json_response(self, data, status_code=200):
        """Envoie une réponse JSON"""
        self._set_headers(status_code)
        response = json.dumps(data, ensure_ascii=False, indent=2)
        self.wfile.write(response.encode('utf-8'))
    
    def do_OPTIONS(self):
        """Gestion des requêtes OPTIONS pour CORS"""
        self._set_headers()
    
    def do_GET(self):
        """Gestion des requêtes GET"""
        try:
            parsed_url = urlparse(self.path)
            path = parsed_url.path
            query_params = parse_qs(parsed_url.query)
            
            logger.info(f"GET {path}")
            
            if path == '/health':
                self._handle_health()
            elif path == '/market':
                self._handle_market()
            elif path.startswith('/market/token/'):
                symbol = path.split('/')[-1]
                self._handle_token_details(symbol)
            elif path == '/market/stats':
                self._handle_market_stats()
            elif path.startswith('/market/orderbook/'):
                symbol = path.split('/')[-1]
                self._handle_order_book(symbol)
            elif path.startswith('/market/price-history/'):
                symbol = path.split('/')[-1]
                days = int(query_params.get('days', [30])[0])
                self._handle_price_history(symbol, days)
            else:
                self._handle_not_found()
                
        except Exception as e:
            logger.error(f"Erreur lors du traitement de la requête: {str(e)}")
            self._send_json_response({
                "success": False,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }, 500)
    
    def _handle_health(self):
        """Endpoint de santé de l'API"""
        self._send_json_response({
            "status": "healthy",
            "timestamp": datetime.now().isoformat(),
            "service": "Startup Tokenization Marketplace API"
        })
    
    def _handle_market(self):
        """Endpoint principal pour récupérer toutes les startups tokenisées"""
        try:
            logger.info("GET /market - Récupération des données du marketplace")
            
            # Appel du MarketAgent
            market_data = market_agent.run()
            
            self._send_json_response({
                "success": True,
                "data": market_data,
                "timestamp": datetime.now().isoformat()
            })
            
        except Exception as e:
            logger.error(f"Erreur lors de la récupération du marché: {str(e)}")
            self._send_json_response({
                "success": False,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }, 500)
    
    def _handle_token_details(self, symbol):
        """Récupère les détails d'un token spécifique"""
        try:
            logger.info(f"GET /market/token/{symbol} - Récupération des détails du token")
            
            token_details = market_agent.get_token_details(symbol)
            
            if not token_details:
                self._send_json_response({
                    "success": False,
                    "error": f"Token {symbol} non trouvé",
                    "timestamp": datetime.now().isoformat()
                }, 404)
                return
            
            self._send_json_response({
                "success": True,
                "data": token_details,
                "timestamp": datetime.now().isoformat()
            })
            
        except Exception as e:
            logger.error(f"Erreur lors de la récupération du token {symbol}: {str(e)}")
            self._send_json_response({
                "success": False,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }, 500)
    
    def _handle_market_stats(self):
        """Récupère les statistiques globales du marché"""
        try:
            logger.info("GET /market/stats - Récupération des statistiques du marché")
            
            stats = market_agent.get_market_stats()
            
            self._send_json_response({
                "success": True,
                "data": stats,
                "timestamp": datetime.now().isoformat()
            })
            
        except Exception as e:
            logger.error(f"Erreur lors de la récupération des statistiques: {str(e)}")
            self._send_json_response({
                "success": False,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }, 500)
    
    def _handle_order_book(self, symbol):
        """Récupère l'order book d'un token"""
        try:
            logger.info(f"GET /market/orderbook/{symbol} - Récupération de l'order book")
            
            token = market_agent.get_token_details(symbol)
            if not token:
                self._send_json_response({
                    "success": False,
                    "error": f"Token {symbol} non trouvé",
                    "timestamp": datetime.now().isoformat()
                }, 404)
                return
            
            order_book = token.get("order_book", {})
            
            self._send_json_response({
                "success": True,
                "data": {
                    "symbol": symbol,
                    "order_book": order_book,
                    "timestamp": datetime.now().isoformat()
                }
            })
            
        except Exception as e:
            logger.error(f"Erreur lors de la récupération de l'order book: {str(e)}")
            self._send_json_response({
                "success": False,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }, 500)
    
    def _handle_price_history(self, symbol, days):
        """Récupère l'historique des prix d'un token"""
        try:
            logger.info(f"GET /market/price-history/{symbol} - Récupération de l'historique sur {days} jours")
            
            token = market_agent.get_token_details(symbol)
            if not token:
                self._send_json_response({
                    "success": False,
                    "error": f"Token {symbol} non trouvé",
                    "timestamp": datetime.now().isoformat()
                }, 404)
                return
            
            price_history = market_agent.generate_price_history(symbol, days)
            
            self._send_json_response({
                "success": True,
                "data": {
                    "symbol": symbol,
                    "price_history": price_history,
                    "period_days": days,
                    "timestamp": datetime.now().isoformat()
                }
            })
            
        except Exception as e:
            logger.error(f"Erreur lors de la récupération de l'historique des prix: {str(e)}")
            self._send_json_response({
                "success": False,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }, 500)
    
    def _handle_not_found(self):
        """Gestionnaire d'erreur 404"""
        self._send_json_response({
            "success": False,
            "error": "Endpoint non trouvé",
            "timestamp": datetime.now().isoformat()
        }, 404)
    
    def log_message(self, format, *args):
        """Désactive les logs par défaut du serveur HTTP"""
        pass

def run_server(port=5000):
    """Démarre le serveur HTTP"""
    server_address = ('', port)
    httpd = HTTPServer(server_address, MarketplaceHandler)
    
    logger.info("🚀 Démarrage de l'API Startup Tokenization Marketplace")
    logger.info("📊 MarketAgent initialisé et prêt")
    logger.info(f"🌐 Serveur démarré sur http://localhost:{port}")
    logger.info("📝 Endpoints disponibles:")
    logger.info("   GET /health - Vérification de santé")
    logger.info("   GET /market - Données du marketplace")
    logger.info("   GET /market/token/<symbol> - Détails d'un token")
    logger.info("   GET /market/stats - Statistiques globales")
    logger.info("   GET /market/orderbook/<symbol> - Order book")
    logger.info("   GET /market/price-history/<symbol> - Historique des prix")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logger.info("\n🛑 Arrêt du serveur...")
        httpd.shutdown()

if __name__ == '__main__':
    run_server()