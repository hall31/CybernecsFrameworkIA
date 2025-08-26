import json
import logging
from typing import Dict, List, Optional
from datetime import datetime
import random

class MarketAgent:
    """
    Agent responsable de la gestion du marketplace des startups tokenisées
    Gère l'échange, le pricing et la liquidité des tokens
    """
    
    def __init__(self):
        self.logger = self._setup_logger()
        self.market_address = "0xMARKET123456789abcdef"
        self.listed_tokens = []
        self.order_book = {}
        self.price_history = {}
        
    def _setup_logger(self) -> logging.Logger:
        """Configure le logger pour l'agent"""
        logger = logging.getLogger("MarketAgent")
        logger.setLevel(logging.INFO)
        
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            
        return logger
    
    def log_event(self, agent_name: str, message: str):
        """Log un événement du marketplace"""
        self.logger.info(f"[{agent_name}] {message}")
        
    def get_tokenised_startups(self) -> List[Dict]:
        """
        Récupère tous les tokens générés via TokenisationAgent
        Simulation des données pour l'instant
        """
        # Simulation des startups tokenisées
        startups = [
            {
                "symbol": "STK001",
                "name": "TechFlow Solutions",
                "token_address": "0xSTK001123456789",
                "total_supply": 1000000,
                "circulating_supply": 750000,
                "valuation": 2500000,  # en euros
                "sector": "SaaS",
                "stage": "Series A"
            },
            {
                "symbol": "STK002", 
                "name": "GreenEnergy Corp",
                "token_address": "0xSTK002123456789",
                "total_supply": 2000000,
                "circulating_supply": 1200000,
                "valuation": 1800000,
                "sector": "CleanTech",
                "stage": "Seed"
            },
            {
                "symbol": "STK003",
                "name": "HealthTech Innovations",
                "token_address": "0xSTK003123456789", 
                "total_supply": 1500000,
                "circulating_supply": 900000,
                "valuation": 3200000,
                "sector": "HealthTech",
                "stage": "Series B"
            },
            {
                "symbol": "STK004",
                "name": "FinTech Revolution",
                "token_address": "0xSTK004123456789",
                "total_supply": 3000000,
                "circulating_supply": 2100000,
                "valuation": 4500000,
                "sector": "FinTech",
                "stage": "Series A"
            },
            {
                "symbol": "STK005",
                "name": "AI Dynamics",
                "token_address": "0xSTK005123456789",
                "total_supply": 800000,
                "circulating_supply": 600000,
                "valuation": 2800000,
                "sector": "AI",
                "stage": "Seed"
            }
        ]
        
        self.log_event("MarketAgent", f"Récupération de {len(startups)} startups tokenisées")
        return startups
    
    def list_startup_on_exchange(self, startup: Dict) -> Dict:
        """
        Liste une startup sur le Startup Exchange interne
        """
        # Calcul du prix initial basé sur la valuation et l'offre
        initial_price = startup["valuation"] / startup["total_supply"]
        
        # Simulation de la volatilité du marché
        volatility = random.uniform(0.8, 1.2)
        current_price = initial_price * volatility
        
        # Simulation du volume échangé
        volume = random.randint(10000, 500000)
        
        listed_token = {
            "symbol": startup["symbol"],
            "name": startup["name"],
            "price": round(current_price, 4),
            "price_eur": f"{current_price:.2f} €",
            "volume": volume,
            "volume_formatted": f"{volume:,}",
            "market_cap": startup["valuation"],
            "change_24h": round(random.uniform(-15, 25), 2),
            "sector": startup["sector"],
            "stage": startup["stage"],
            "listed_at": datetime.now().isoformat()
        }
        
        self.listed_tokens.append(listed_token)
        self.log_event("MarketAgent", f"Startup {startup['symbol']} listée sur le marché global")
        
        return listed_token
    
    def create_marketplace_contract(self) -> Dict:
        """
        Crée un smart contract Marketplace pour l'achat/vente de tokens
        """
        contract_data = {
            "contract_address": self.market_address,
            "contract_type": "StartupTokenMarketplace",
            "features": [
                "Achat/Vente de tokens startup",
                "Order book simplifié",
                "Pricing basé sur l'offre/demande",
                "Gestion de la liquidité",
                "Settlement automatique"
            ],
            "created_at": datetime.now().isoformat()
        }
        
        self.log_event("MarketAgent", "Smart contract Marketplace créé")
        return contract_data
    
    def generate_price_history(self, symbol: str, days: int = 30) -> List[Dict]:
        """
        Génère un historique des prix pour un token donné
        """
        history = []
        base_price = next((token["price"] for token in self.listed_tokens if token["symbol"] == symbol), 1.0)
        
        for day in range(days):
            # Simulation de la volatilité quotidienne
            daily_change = random.uniform(-0.05, 0.05)
            price = base_price * (1 + daily_change)
            
            # Calcul de la date (simplifié)
            from datetime import timedelta
            date_obj = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=days-day-1)
            
            history.append({
                "date": date_obj.isoformat(),
                "price": round(price, 4),
                "volume": random.randint(5000, 100000)
            })
            
        return history
    
    def get_market_stats(self) -> Dict:
        """
        Récupère les statistiques globales du marché
        """
        total_market_cap = sum(token["market_cap"] for token in self.listed_tokens)
        total_volume = sum(token["volume"] for token in self.listed_tokens)
        
        return {
            "total_listed": len(self.listed_tokens),
            "total_market_cap": total_market_cap,
            "total_volume_24h": total_volume,
            "market_sentiment": "Bullish" if total_volume > 500000 else "Neutral",
            "last_updated": datetime.now().isoformat()
        }
    
    def run(self) -> Dict:
        """
        Méthode principale qui exécute toutes les actions du MarketAgent
        """
        self.log_event("MarketAgent", "Démarrage du MarketAgent")
        
        # 1. Récupération des startups tokenisées
        startups = self.get_tokenised_startups()
        
        # 2. Listing sur l'exchange
        for startup in startups:
            self.list_startup_on_exchange(startup)
        
        # 3. Création du smart contract Marketplace
        contract = self.create_marketplace_contract()
        
        # 4. Génération des données de marché
        market_stats = self.get_market_stats()
        
        # 5. Préparation de la réponse
        result = {
            "market_address": self.market_address,
            "listed_tokens": self.listed_tokens,
            "market_stats": market_stats,
            "contract_info": contract,
            "timestamp": datetime.now().isoformat()
        }
        
        self.log_event("MarketAgent", f"Marketplace initialisé avec {len(self.listed_tokens)} tokens")
        
        return result
    
    def get_token_details(self, symbol: str) -> Optional[Dict]:
        """
        Récupère les détails d'un token spécifique
        """
        token = next((t for t in self.listed_tokens if t["symbol"] == symbol), None)
        if token:
            token["price_history"] = self.generate_price_history(symbol)
            token["order_book"] = self._generate_order_book(symbol)
        return token
    
    def _generate_order_book(self, symbol: str) -> Dict:
        """
        Génère un order book simplifié pour un token
        """
        token = next((t for t in self.listed_tokens if t["symbol"] == symbol), None)
        if not token:
            return {}
            
        current_price = token["price"]
        
        # Bids (achats)
        bids = []
        for i in range(5):
            price = current_price * (1 - (i + 1) * 0.01)
            amount = random.randint(100, 1000)
            bids.append({
                "price": round(price, 4),
                "amount": amount,
                "total": round(price * amount, 2)
            })
        
        # Asks (ventes)
        asks = []
        for i in range(5):
            price = current_price * (1 + (i + 1) * 0.01)
            amount = random.randint(100, 1000)
            asks.append({
                "price": round(price, 4),
                "amount": amount,
                "total": round(price * amount, 2)
            })
        
        return {
            "bids": sorted(bids, key=lambda x: x["price"], reverse=True),
            "asks": sorted(asks, key=lambda x: x["price"])
        }

if __name__ == "__main__":
    # Test du MarketAgent
    agent = MarketAgent()
    result = agent.run()
    print(json.dumps(result, indent=2))