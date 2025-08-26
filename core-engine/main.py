from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import logging
from datetime import datetime
from agents.market_agent import MarketAgent

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Instance globale du MarketAgent
market_agent = MarketAgent()

@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint de santé de l'API"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "Startup Tokenization Marketplace API"
    })

@app.route('/market', methods=['GET'])
def get_market():
    """
    Endpoint principal pour récupérer toutes les startups tokenisées listées
    GET /market
    """
    try:
        logger.info("GET /market - Récupération des données du marketplace")
        
        # Appel du MarketAgent
        market_data = market_agent.run()
        
        return jsonify({
            "success": True,
            "data": market_data,
            "timestamp": datetime.now().isoformat()
        })
        
    except Exception as e:
        logger.error(f"Erreur lors de la récupération du marché: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }), 500

@app.route('/market/token/<symbol>', methods=['GET'])
def get_token_details(symbol):
    """
    Récupère les détails d'un token spécifique
    GET /market/token/<symbol>
    """
    try:
        logger.info(f"GET /market/token/{symbol} - Récupération des détails du token")
        
        token_details = market_agent.get_token_details(symbol)
        
        if not token_details:
            return jsonify({
                "success": False,
                "error": f"Token {symbol} non trouvé",
                "timestamp": datetime.now().isoformat()
            }), 404
        
        return jsonify({
            "success": True,
            "data": token_details,
            "timestamp": datetime.now().isoformat()
        })
        
    except Exception as e:
        logger.error(f"Erreur lors de la récupération du token {symbol}: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }), 500

@app.route('/market/stats', methods=['GET'])
def get_market_stats():
    """
    Récupère les statistiques globales du marché
    GET /market/stats
    """
    try:
        logger.info("GET /market/stats - Récupération des statistiques du marché")
        
        stats = market_agent.get_market_stats()
        
        return jsonify({
            "success": True,
            "data": stats,
            "timestamp": datetime.now().isoformat()
        })
        
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des statistiques: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }), 500

@app.route('/market/orderbook/<symbol>', methods=['GET'])
def get_order_book(symbol):
    """
    Récupère l'order book d'un token spécifique
    GET /market/orderbook/<symbol>
    """
    try:
        logger.info(f"GET /market/orderbook/{symbol} - Récupération de l'order book")
        
        token = market_agent.get_token_details(symbol)
        if not token:
            return jsonify({
                "success": False,
                "error": f"Token {symbol} non trouvé",
                "timestamp": datetime.now().isoformat()
            }), 404
        
        order_book = token.get("order_book", {})
        
        return jsonify({
            "success": True,
            "data": {
                "symbol": symbol,
                "order_book": order_book,
                "timestamp": datetime.now().isoformat()
            }
        })
        
    except Exception as e:
        logger.error(f"Erreur lors de la récupération de l'order book: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }), 500

@app.route('/market/price-history/<symbol>', methods=['GET'])
def get_price_history(symbol):
    """
    Récupère l'historique des prix d'un token
    GET /market/price-history/<symbol>?days=30
    """
    try:
        days = request.args.get('days', 30, type=int)
        logger.info(f"GET /market/price-history/{symbol} - Récupération de l'historique sur {days} jours")
        
        token = market_agent.get_token_details(symbol)
        if not token:
            return jsonify({
                "success": False,
                "error": f"Token {symbol} non trouvé",
                "timestamp": datetime.now().isoformat()
            }), 404
        
        price_history = market_agent.generate_price_history(symbol, days)
        
        return jsonify({
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
        return jsonify({
            "success": False,
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }), 500

@app.errorhandler(404)
def not_found(error):
    """Gestionnaire d'erreur 404"""
    return jsonify({
        "success": False,
        "error": "Endpoint non trouvé",
        "timestamp": datetime.now().isoformat()
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Gestionnaire d'erreur 500"""
    return jsonify({
        "success": False,
        "error": "Erreur interne du serveur",
        "timestamp": datetime.now().isoformat()
    }), 500

if __name__ == '__main__':
    logger.info("🚀 Démarrage de l'API Startup Tokenization Marketplace")
    logger.info("📊 MarketAgent initialisé et prêt")
    logger.info("🌐 Serveur démarré sur http://localhost:5000")
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )