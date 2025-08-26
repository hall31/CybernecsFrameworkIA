import asyncio
import aiohttp
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from utils.logger import log_event, log_success, log_warning, log_error

class MacroFundAgent:
    def __init__(self):
        self.name = "MacroFundAgent"
        self.portfolio_value = 50000000  # 50M €
        self.current_allocations = {
            "IA Startups": 0.40,
            "ETF IA": 0.20,
            "Crypto": 0.25,
            "Stocks": 0.10,
            "Commodities": 0.05
        }
        self.hedges = {
            "Short Nasdaq ETF": {"active": True, "size": 0.05},
            "Long Gold": {"active": True, "size": 0.03}
        }
        self.recent_arbitrages = []
        self.market_data = {}
        
        log_event(self.name, "Initialized - Multi-asset global fund manager")
    
    async def run(self) -> dict:
        """
        Execute macro fund analysis and rebalancing
        
        Returns:
            dict: Complete macro portfolio allocation and actions
        """
        log_event(self.name, "Starting macro fund analysis")
        
        try:
            # 1. Récupération des données internes et externes
            await self._fetch_internal_data()
            await self._fetch_external_data()
            
            # 2. Analyse des corrélations
            correlations = self._analyze_correlations()
            
            # 3. Création de l'allocation macro globale
            allocation = self._create_macro_allocation(correlations)
            
            # 4. Exécution des arbitrages
            arbitrages = await self._execute_arbitrages(allocation)
            
            # 5. Mise à jour du portefeuille
            self._update_portfolio(allocation, arbitrages)
            
            result = {
                "portfolio_value": f"{self.portfolio_value:,.0f} €",
                "allocations": self.current_allocations,
                "hedges": self.hedges,
                "recent_arbitrages": self.recent_arbitrages[-5:],  # 5 derniers
                "market_correlations": correlations,
                "timestamp": datetime.now().isoformat()
            }
            
            log_success(self.name, f"Macro allocation completed - NAV: {result['portfolio_value']}")
            return result
            
        except Exception as e:
            log_error(self.name, f"Error in macro fund analysis: {str(e)}")
            raise
    
    async def _fetch_internal_data(self):
        """Récupère les données internes (tokens startups, ETF IA, positions hedge fund)"""
        log_event(self.name, "Fetching internal data")
        
        # Simulation des données internes
        self.market_data["internal"] = {
            "startup_tokens": {
                "AI_Startup_1": {"value": 15000000, "performance": 0.25},
                "AI_Startup_2": {"value": 12000000, "performance": 0.18},
                "AI_Startup_3": {"value": 8000000, "performance": 0.32}
            },
            "etf_ia": {
                "Global_AI_ETF": {"value": 10000000, "performance": 0.15},
                "Tech_Innovation_ETF": {"value": 10000000, "performance": 0.22}
            },
            "hedge_positions": {
                "Short_Nasdaq": {"value": -2500000, "performance": -0.08},
                "Long_Gold": {"value": 1500000, "performance": 0.12}
            }
        }
        
        log_event(self.name, "Internal data fetched successfully")
    
    async def _fetch_external_data(self):
        """Récupère les données externes via APIs"""
        log_event(self.name, "Fetching external market data")
        
        # Simulation des données externes (en production, utiliser de vraies APIs)
        self.market_data["external"] = {
            "crypto": {
                "BTC": {"price": 45000, "change_24h": 0.05, "market_cap": 850000000000},
                "ETH": {"price": 3200, "change_24h": 0.03, "market_cap": 380000000000}
            },
            "stocks": {
                "NASDAQ": {"value": 14500, "change_24h": -0.02, "volatility": 0.25},
                "S&P500": {"value": 4200, "change_24h": -0.01, "volatility": 0.20}
            },
            "commodities": {
                "Gold": {"price": 1950, "change_24h": 0.02, "volatility": 0.15},
                "Oil": {"price": 75, "change_24h": -0.03, "volatility": 0.30}
            },
            "forex": {
                "EUR/USD": {"rate": 1.08, "change_24h": 0.01},
                "XAF/EUR": {"rate": 0.0015, "change_24h": -0.005}
            }
        }
        
        log_event(self.name, "External market data fetched successfully")
    
    def _analyze_correlations(self) -> dict:
        """Analyse les corrélations entre différents marchés"""
        log_event(self.name, "Analyzing market correlations")
        
        correlations = {
            "nasdaq_ai_correlation": -0.75,  # Si Nasdaq chute, réduire exposition SaaS
            "btc_ai_tokens_correlation": 0.60,  # Si BTC monte, arbitrer tokens IA vers crypto
            "gold_risk_off": 0.80,  # Or monte en période de risque
            "oil_inflation": 0.45,  # Pétrole et inflation
            "eur_usd_risk": -0.30  # EUR/USD et sentiment de risque
        }
        
        log_event(self.name, f"Correlation analysis completed - Key: Nasdaq-AI: {correlations['nasdaq_ai_correlation']:.2f}")
        return correlations
    
    def _create_macro_allocation(self, correlations: dict) -> dict:
        """Crée une allocation macro globale basée sur les corrélations"""
        log_event(self.name, "Creating macro allocation strategy")
        
        # Ajustements basés sur les corrélations
        adjustments = {}
        
        # Si Nasdaq chute, réduire exposition SaaS
        if correlations["nasdaq_ai_correlation"] < -0.7:
            adjustments["IA Startups"] = -0.05  # -5%
            adjustments["ETF IA"] = -0.03      # -3%
            adjustments["Crypto"] = 0.08       # +8%
        
        # Si BTC monte, augmenter exposition crypto
        if correlations["btc_ai_tokens_correlation"] > 0.5:
            adjustments["Crypto"] = adjustments.get("Crypto", 0) + 0.05  # +5%
            adjustments["IA Startups"] = adjustments.get("IA Startups", 0) - 0.03  # -3%
            adjustments["Stocks"] = adjustments.get("Stocks", 0) - 0.02  # -2%
        
        # Ajuster les hedges
        if correlations["gold_risk_off"] > 0.7:
            self.hedges["Long Gold"]["active"] = True
            self.hedges["Long Gold"]["size"] = 0.05  # 5%
        else:
            self.hedges["Long Gold"]["active"] = False
            self.hedges["Long Gold"]["size"] = 0.02  # 2%
        
        # Appliquer les ajustements
        new_allocations = self.current_allocations.copy()
        for asset, adjustment in adjustments.items():
            if asset in new_allocations:
                new_allocations[asset] = max(0, min(1, new_allocations[asset] + adjustment))
        
        # Normaliser à 100%
        total = sum(new_allocations.values())
        for asset in new_allocations:
            new_allocations[asset] = new_allocations[asset] / total
        
        log_event(self.name, f"Macro allocation adjusted - New Crypto: {new_allocations['Crypto']:.1%}")
        return new_allocations
    
    async def _execute_arbitrages(self, new_allocation: dict) -> List[dict]:
        """Exécute les arbitrages via TraderContract global"""
        log_event(self.name, "Executing macro arbitrages")
        
        arbitrages = []
        
        for asset, new_weight in new_allocation.items():
            current_weight = self.current_allocations[asset]
            if abs(new_weight - current_weight) > 0.02:  # Seuil de 2%
                if new_weight > current_weight:
                    # Achat
                    action = "BUY"
                    amount = (new_weight - current_weight) * self.portfolio_value
                    arbitrages.append({
                        "timestamp": datetime.now().isoformat(),
                        "action": action,
                        "asset": asset,
                        "amount": f"{amount:,.0f} €",
                        "reason": f"Macro rebalancing - increase allocation to {new_weight:.1%}"
                    })
                    log_event(self.name, f"Arbitrage: {action} {asset} - {amount:,.0f} €")
                else:
                    # Vente
                    action = "SELL"
                    amount = (current_weight - new_weight) * self.portfolio_value
                    arbitrages.append({
                        "timestamp": datetime.now().isoformat(),
                        "action": action,
                        "asset": asset,
                        "amount": f"{amount:,.0f} €",
                        "reason": f"Macro rebalancing - decrease allocation from {current_weight:.1%}"
                    })
                    log_event(self.name, f"Arbitrage: {action} {asset} - {amount:,.0f} €")
        
        # Ajouter aux arbitrages récents
        self.recent_arbitrages.extend(arbitrages)
        
        log_success(self.name, f"Executed {len(arbitrages)} arbitrages")
        return arbitrages
    
    def _update_portfolio(self, new_allocation: dict, arbitrages: List[dict]):
        """Met à jour le portefeuille après les arbitrages"""
        log_event(self.name, "Updating portfolio allocations")
        
        # Mettre à jour les allocations
        self.current_allocations = new_allocation
        
        # Calculer la nouvelle valeur du portefeuille (simulation de performance)
        total_return = 0
        for asset, weight in self.current_allocations.items():
            if asset in self.market_data.get("internal", {}).get("startup_tokens", {}):
                # Startups IA
                total_return += weight * 0.25  # 25% de performance moyenne
            elif asset == "Crypto":
                total_return += weight * 0.15  # 15% de performance crypto
            elif asset == "Stocks":
                total_return += weight * 0.08  # 8% de performance actions
            elif asset == "Commodities":
                total_return += weight * 0.12  # 12% de performance matières premières
        
        # Ajuster la valeur du portefeuille
        self.portfolio_value *= (1 + total_return)
        
        log_success(self.name, f"Portfolio updated - New NAV: {self.portfolio_value:,.0f} €")
    
    def get_portfolio_summary(self) -> dict:
        """Retourne un résumé du portefeuille"""
        return {
            "portfolio_value": f"{self.portfolio_value:,.0f} €",
            "allocations": self.current_allocations,
            "hedges": self.hedges,
            "recent_arbitrages": self.recent_arbitrages[-5:],
            "performance_ytd": 0.18,  # 18% YTD
            "sharpe_ratio": 1.25,
            "max_drawdown": -0.08
        }
    
    def get_hedge_status(self) -> dict:
        """Retourne le statut des hedges"""
        return {
            "hedges": self.hedges,
            "total_hedge_value": sum(
                hedge["size"] * self.portfolio_value 
                for hedge in self.hedges.values() 
                if hedge["active"]
            )
        }