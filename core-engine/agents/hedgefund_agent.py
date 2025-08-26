import numpy as np
import pandas as pd
from typing import Dict, List, Optional
from datetime import datetime, timedelta
import random
from utils.logger import log_event, log_success, log_warning

class HedgeFundAgent:
    def __init__(self):
        self.name = "HedgeFundAgent"
        self.portfolio = {
            "long_positions": [],
            "short_positions": [],
            "cash_reserve": 100.0,  # 100% cash initial
            "total_value": 1000000,  # 1M USD initial
            "performance_history": []
        }
        
        # Configuration des stratégies
        self.strategies = {
            "momentum": {"weight": 0.4, "lookback_days": 30},
            "mean_reversion": {"weight": 0.3, "lookback_days": 60},
            "volatility": {"weight": 0.3, "lookback_days": 20}
        }
        
        # Tokens disponibles pour trading
        self.available_tokens = {
            "STK001": {"name": "FinTech Startup", "type": "startup", "current_price": 100.0},
            "STK002": {"name": "AI Startup", "type": "startup", "current_price": 150.0},
            "STK003": {"name": "DeFi Startup", "type": "startup", "current_price": 80.0},
            "STK004": {"name": "HealthTech Startup", "type": "startup", "current_price": 120.0},
            "STK005": {"name": "EduTech Startup", "type": "startup", "current_price": 90.0},
            "ETF001": {"name": "AI Technology ETF", "type": "etf", "current_price": 200.0},
            "ETF002": {"name": "DeFi Index ETF", "type": "etf", "current_price": 180.0},
            "ETF003": {"name": "Startup Growth ETF", "type": "etf", "current_price": 160.0}
        }
        
        log_event(self.name, "Initialized with $1M capital")
    
    def run(self) -> dict:
        """
        Exécute la stratégie de trading IA et retourne le portefeuille optimisé
        
        Returns:
            dict: Portefeuille optimisé avec positions long/short et cash
        """
        log_event(self.name, "Starting trading strategy execution")
        
        try:
            # 1. Récupération des données du marché
            market_data = self._get_market_data()
            
            # 2. Analyse ML et génération de signaux
            trading_signals = self._generate_trading_signals(market_data)
            
            # 3. Optimisation du portefeuille
            optimized_portfolio = self._optimize_portfolio(trading_signals)
            
            # 4. Mise à jour du portefeuille
            self._update_portfolio(optimized_portfolio)
            
            # 5. Calcul des performances
            performance = self._calculate_performance()
            
            # 6. Log de l'événement
            log_success(self.name, f"Portfolio updated - Total Value: ${self.portfolio['total_value']:,.2f}")
            
            return {
                "portfolio": self.portfolio,
                "performance": performance,
                "strategy_commentary": self._generate_strategy_commentary(),
                "last_update": datetime.now().isoformat()
            }
            
        except Exception as e:
            log_event(self.name, f"Error in trading strategy: {str(e)}", "ERROR")
            return {"error": str(e)}
    
    def _get_market_data(self) -> dict:
        """Simule la récupération des données du marché"""
        market_data = {}
        
        for token_id, token_info in self.available_tokens.items():
            # Simulation de données historiques
            base_price = token_info["current_price"]
            volatility = random.uniform(0.05, 0.20)  # 5-20% volatilité
            
            # Génération de prix historiques
            historical_prices = []
            for i in range(100):  # 100 jours d'historique
                change = random.gauss(0, volatility)
                price = base_price * (1 + change)
                historical_prices.append(max(price, 1.0))  # Prix minimum $1
            
            market_data[token_id] = {
                "current_price": base_price,
                "historical_prices": historical_prices,
                "volume": random.uniform(10000, 1000000),
                "volatility": np.std(historical_prices) / np.mean(historical_prices),
                "momentum": (historical_prices[-1] - historical_prices[-30]) / historical_prices[-30] if len(historical_prices) >= 30 else 0
            }
        
        return market_data
    
    def _generate_trading_signals(self, market_data: dict) -> dict:
        """Génère des signaux de trading basés sur l'analyse ML"""
        signals = {}
        
        for token_id, data in market_data.items():
            score = 0.0
            
            # Stratégie Momentum
            if data["momentum"] > 0.05:  # +5% sur 30 jours
                score += self.strategies["momentum"]["weight"] * 0.8
            elif data["momentum"] < -0.05:  # -5% sur 30 jours
                score += self.strategies["momentum"]["weight"] * -0.6
            
            # Stratégie Mean Reversion
            current_price = data["current_price"]
            avg_price = np.mean(data["historical_prices"])
            if current_price < avg_price * 0.9:  # 10% sous la moyenne
                score += self.strategies["mean_reversion"]["weight"] * 0.7
            elif current_price > avg_price * 1.1:  # 10% au-dessus de la moyenne
                score += self.strategies["mean_reversion"]["weight"] * -0.5
            
            # Stratégie Volatilité
            if data["volatility"] > 0.15:  # Haute volatilité
                score += self.strategies["volatility"]["weight"] * 0.3
            
            signals[token_id] = {
                "score": score,
                "recommendation": "buy" if score > 0.3 else "sell" if score < -0.3 else "hold",
                "confidence": abs(score)
            }
        
        return signals
    
    def _optimize_portfolio(self, trading_signals: dict) -> dict:
        """Optimise le portefeuille basé sur les signaux de trading"""
        # Tri des tokens par score
        sorted_tokens = sorted(trading_signals.items(), key=lambda x: x[1]["score"], reverse=True)
        
        # Allocation du capital
        total_capital = self.portfolio["total_value"]
        long_allocation = 0.0
        short_allocation = 0.0
        
        long_positions = []
        short_positions = []
        
        for token_id, signal in sorted_tokens:
            if signal["recommendation"] == "buy" and signal["confidence"] > 0.4:
                # Position long
                allocation = min(signal["confidence"] * 0.15, 0.25)  # Max 25% par position
                if long_allocation + allocation <= 0.6:  # Max 60% en positions long
                    long_positions.append({
                        "token": token_id,
                        "allocation": f"{allocation * 100:.1f}%",
                        "amount_usd": allocation * total_capital,
                        "confidence": signal["confidence"]
                    })
                    long_allocation += allocation
            
            elif signal["recommendation"] == "sell" and signal["confidence"] > 0.4:
                # Position short
                allocation = min(signal["confidence"] * 0.10, 0.20)  # Max 20% par position short
                if short_allocation + allocation <= 0.3:  # Max 30% en positions short
                    short_positions.append({
                        "token": token_id,
                        "allocation": f"{allocation * 100:.1f}%",
                        "amount_usd": allocation * total_capital,
                        "confidence": signal["confidence"]
                    })
                    short_allocation += allocation
        
        cash_reserve = max(0.1, 1.0 - long_allocation - short_allocation)  # Min 10% cash
        
        return {
            "long_positions": long_positions,
            "short_positions": short_positions,
            "cash_reserve": f"{cash_reserve * 100:.1f}%",
            "long_allocation": long_allocation,
            "short_allocation": short_allocation
        }
    
    def _update_portfolio(self, optimized_portfolio: dict):
        """Met à jour le portefeuille avec les nouvelles positions"""
        self.portfolio["long_positions"] = optimized_portfolio["long_positions"]
        self.portfolio["short_positions"] = optimized_portfolio["short_positions"]
        self.portfolio["cash_reserve"] = optimized_portfolio["cash_reserve"]
        
        # Calcul de la nouvelle valeur totale
        total_long = sum(pos["amount_usd"] for pos in self.portfolio["long_positions"])
        total_short = sum(pos["amount_usd"] for pos in self.portfolio["short_positions"])
        cash_value = float(optimized_portfolio["cash_reserve"].rstrip('%')) / 100 * self.portfolio["total_value"]
        
        # Simulation de performance (gains/pertes)
        performance_change = random.uniform(-0.02, 0.03)  # -2% à +3% par jour
        self.portfolio["total_value"] *= (1 + performance_change)
        
        # Ajout à l'historique des performances
        self.portfolio["performance_history"].append({
            "date": datetime.now().isoformat(),
            "total_value": self.portfolio["total_value"],
            "long_value": total_long,
            "short_value": total_short,
            "cash_value": cash_value,
            "daily_return": performance_change
        })
    
    def _calculate_performance(self) -> dict:
        """Calcule les métriques de performance du portefeuille"""
        if len(self.portfolio["performance_history"]) < 2:
            return {"roi": 0.0, "volatility": 0.0, "sharpe_ratio": 0.0}
        
        # Calcul du ROI
        initial_value = 1000000  # 1M USD initial
        current_value = self.portfolio["total_value"]
        roi = ((current_value - initial_value) / initial_value) * 100
        
        # Calcul de la volatilité
        daily_returns = [entry["daily_return"] for entry in self.portfolio["performance_history"]]
        volatility = np.std(daily_returns) * np.sqrt(252) * 100  # Annualisée
        
        # Calcul du Sharpe ratio (simplifié)
        avg_return = np.mean(daily_returns) * 252  # Annualisé
        risk_free_rate = 0.02  # 2% taux sans risque
        sharpe_ratio = (avg_return - risk_free_rate) / (np.std(daily_returns) * np.sqrt(252)) if volatility > 0 else 0
        
        return {
            "roi": round(roi, 2),
            "volatility": round(volatility, 2),
            "sharpe_ratio": round(sharpe_ratio, 2),
            "total_return": round((current_value - initial_value), 2),
            "current_value": round(current_value, 2)
        }
    
    def _generate_strategy_commentary(self) -> str:
        """Génère un commentaire sur la stratégie actuelle"""
        long_count = len(self.portfolio["long_positions"])
        short_count = len(self.portfolio["short_positions"])
        
        if long_count > short_count:
            if long_count >= 3:
                return "Nous renforçons notre position long sur les startups technologiques avec une approche momentum agressive."
            else:
                return "Nous maintenons une position long modérée en attendant des signaux plus clairs du marché."
        elif short_count > long_count:
            return "Nous adoptons une stratégie défensive avec des positions short sur les actifs surévalués."
        else:
            return "Portefeuille équilibré avec une approche conservatrice et une forte réserve de liquidités."
    
    def get_current_portfolio(self) -> dict:
        """Retourne le portefeuille actuel"""
        return {
            "portfolio": self.portfolio,
            "performance": self._calculate_performance(),
            "strategy_commentary": self._generate_strategy_commentary(),
            "last_update": datetime.now().isoformat()
        }
    
    def rebalance_portfolio(self) -> dict:
        """Force le rebalancement du portefeuille"""
        log_event(self.name, "Manual portfolio rebalancing requested")
        return self.run()