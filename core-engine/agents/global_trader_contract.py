from typing import Dict, List, Optional
from datetime import datetime
from utils.logger import log_event, log_success, log_warning, log_error

class GlobalTraderContract:
    def __init__(self):
        self.name = "GlobalTraderContract"
        self.supported_assets = {
            "startup_tokens": ["AI_Startup_1", "AI_Startup_2", "AI_Startup_3"],
            "crypto": ["BTC", "ETH", "AI_Token"],
            "stocks": ["NASDAQ_ETF", "S&P500_ETF", "Tech_ETF"],
            "commodities": ["Gold", "Oil", "Silver"],
            "forex": ["EUR/USD", "XAF/EUR"]
        }
        self.transaction_history = []
        self.positions = {}
        self.fees = {
            "startup_tokens": 0.01,  # 1%
            "crypto": 0.002,         # 0.2%
            "stocks": 0.001,         # 0.1%
            "commodities": 0.0015,   # 0.15%
            "forex": 0.0005          # 0.05%
        }
        
        log_event(self.name, "Initialized - Multi-asset trading contract")
    
    def buy(self, asset: str, amount: float, asset_type: str = None) -> dict:
        """
        Acheter un actif
        
        Args:
            asset: Nom de l'actif
            amount: Montant en euros
            asset_type: Type d'actif (optionnel, auto-détecté si non fourni)
            
        Returns:
            dict: Résultat de la transaction
        """
        try:
            # Détecter le type d'actif si non fourni
            if not asset_type:
                asset_type = self._detect_asset_type(asset)
            
            if not asset_type:
                raise ValueError(f"Asset type not recognized for {asset}")
            
            # Calculer les frais
            fee_rate = self.fees.get(asset_type, 0.01)
            fee_amount = amount * fee_rate
            net_amount = amount - fee_amount
            
            # Créer la transaction
            transaction = {
                "id": f"TX_{len(self.transaction_history) + 1:06d}",
                "timestamp": datetime.now().isoformat(),
                "action": "BUY",
                "asset": asset,
                "asset_type": asset_type,
                "amount": amount,
                "fee": fee_amount,
                "net_amount": net_amount,
                "status": "executed"
            }
            
            # Mettre à jour les positions
            if asset not in self.positions:
                self.positions[asset] = {"quantity": 0, "total_cost": 0}
            
            # Calculer la quantité (simulation)
            if asset_type == "startup_tokens":
                price = 1000  # Prix simulé par token
            elif asset_type == "crypto":
                price = 45000 if asset == "BTC" else 3200  # Prix simulés
            elif asset_type == "stocks":
                price = 100  # Prix simulé par action
            elif asset_type == "commodities":
                price = 1950 if asset == "Gold" else 75  # Prix simulés
            else:
                price = 1  # Prix par défaut
            
            quantity = net_amount / price
            self.positions[asset]["quantity"] += quantity
            self.positions[asset]["total_cost"] += amount
            
            # Ajouter à l'historique
            self.transaction_history.append(transaction)
            
            log_success(self.name, f"BUY executed: {asset} - {amount:,.0f} € (Fee: {fee_amount:,.0f} €)")
            
            return {
                "success": True,
                "transaction": transaction,
                "position_updated": self.positions[asset]
            }
            
        except Exception as e:
            log_error(self.name, f"BUY failed for {asset}: {str(e)}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def sell(self, asset: str, amount: float, asset_type: str = None) -> dict:
        """
        Vendre un actif
        
        Args:
            asset: Nom de l'actif
            amount: Montant en euros
            asset_type: Type d'actif (optionnel, auto-détecté si non fourni)
            
        Returns:
            dict: Résultat de la transaction
        """
        try:
            # Détecter le type d'actif si non fourni
            if not asset_type:
                asset_type = self._detect_asset_type(asset)
            
            if not asset_type:
                raise ValueError(f"Asset type not recognized for {asset}")
            
            # Vérifier si on a suffisamment de position
            if asset not in self.positions or self.positions[asset]["quantity"] <= 0:
                raise ValueError(f"Insufficient position for {asset}")
            
            # Calculer les frais
            fee_rate = self.fees.get(asset_type, 0.01)
            fee_amount = amount * fee_rate
            net_amount = amount - fee_amount
            
            # Créer la transaction
            transaction = {
                "id": f"TX_{len(self.transaction_history) + 1:06d}",
                "timestamp": datetime.now().isoformat(),
                "action": "SELL",
                "asset": asset,
                "asset_type": asset_type,
                "amount": amount,
                "fee": fee_amount,
                "net_amount": net_amount,
                "status": "executed"
            }
            
            # Mettre à jour les positions
            current_position = self.positions[asset]
            current_value = current_position["quantity"] * self._get_asset_price(asset, asset_type)
            
            # Calculer la quantité à vendre
            sell_ratio = amount / current_value
            quantity_to_sell = current_position["quantity"] * sell_ratio
            
            current_position["quantity"] -= quantity_to_sell
            current_position["total_cost"] *= (1 - sell_ratio)
            
            # Si position vide, la supprimer
            if current_position["quantity"] <= 0:
                del self.positions[asset]
            
            # Ajouter à l'historique
            self.transaction_history.append(transaction)
            
            log_success(self.name, f"SELL executed: {asset} - {amount:,.0f} € (Fee: {fee_amount:,.0f} €)")
            
            return {
                "success": True,
                "transaction": transaction,
                "position_updated": self.positions.get(asset, {"quantity": 0, "total_cost": 0})
            }
            
        except Exception as e:
            log_error(self.name, f"SELL failed for {asset}: {str(e)}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def rebalance_macro(self, target_allocations: dict, current_portfolio_value: float) -> dict:
        """
        Rééquilibrer le portefeuille selon les allocations macro cibles
        
        Args:
            target_allocations: Dict des allocations cibles
            current_portfolio_value: Valeur actuelle du portefeuille
            
        Returns:
            dict: Résumé des rééquilibrages effectués
        """
        log_event(self.name, "Starting macro portfolio rebalancing")
        
        rebalancing_actions = []
        total_trades = 0
        
        try:
            for asset, target_weight in target_allocations.items():
                current_value = self._get_asset_current_value(asset)
                target_value = target_weight * current_portfolio_value
                
                if abs(current_value - target_value) > current_portfolio_value * 0.01:  # Seuil 1%
                    if current_value < target_value:
                        # Acheter
                        buy_amount = target_value - current_value
                        result = self.buy(asset, buy_amount)
                        if result["success"]:
                            rebalancing_actions.append({
                                "action": "BUY",
                                "asset": asset,
                                "amount": buy_amount,
                                "reason": "Macro rebalancing"
                            })
                            total_trades += 1
                    else:
                        # Vendre
                        sell_amount = current_value - target_value
                        result = self.sell(asset, sell_amount)
                        if result["success"]:
                            rebalancing_actions.append({
                                "action": "SELL",
                                "asset": asset,
                                "amount": sell_amount,
                                "reason": "Macro rebalancing"
                            })
                            total_trades += 1
            
            log_success(self.name, f"Macro rebalancing completed - {total_trades} trades executed")
            
            return {
                "success": True,
                "rebalancing_actions": rebalancing_actions,
                "total_trades": total_trades,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            log_error(self.name, f"Macro rebalancing failed: {str(e)}")
            return {
                "success": False,
                "error": str(e),
                "rebalancing_actions": rebalancing_actions,
                "total_trades": total_trades
            }
    
    def _detect_asset_type(self, asset: str) -> Optional[str]:
        """Détecte automatiquement le type d'actif"""
        # Mapping direct pour les noms d'actifs génériques
        asset_mapping = {
            "IA Startups": "startup_tokens",
            "ETF IA": "stocks",
            "Crypto": "crypto",
            "Stocks": "stocks",
            "Commodities": "commodities"
        }
        
        if asset in asset_mapping:
            return asset_mapping[asset]
        
        # Vérification dans les listes d'actifs spécifiques
        for asset_type, assets in self.supported_assets.items():
            if asset in assets:
                return asset_type
        return None
    
    def _get_asset_price(self, asset: str, asset_type: str) -> float:
        """Récupère le prix d'un actif (simulation)"""
        if asset_type == "startup_tokens":
            return 1000
        elif asset_type == "crypto":
            return 45000 if asset == "BTC" else 3200
        elif asset_type == "stocks":
            return 100
        elif asset_type == "commodities":
            return 1950 if asset == "Gold" else 75
        else:
            return 1
    
    def _get_asset_current_value(self, asset: str) -> float:
        """Calcule la valeur actuelle d'un actif dans le portefeuille"""
        if asset not in self.positions:
            return 0
        
        asset_type = self._detect_asset_type(asset)
        price = self._get_asset_price(asset, asset_type)
        return self.positions[asset]["quantity"] * price
    
    def get_portfolio_summary(self) -> dict:
        """Retourne un résumé du portefeuille"""
        total_value = 0
        asset_values = {}
        
        for asset, position in self.positions.items():
            asset_type = self._detect_asset_type(asset)
            price = self._get_asset_price(asset, asset_type)
            value = position["quantity"] * price
            asset_values[asset] = {
                "quantity": position["quantity"],
                "price": price,
                "value": value,
                "cost_basis": position["total_cost"],
                "unrealized_pnl": value - position["total_cost"]
            }
            total_value += value
        
        return {
            "total_portfolio_value": total_value,
            "asset_values": asset_values,
            "total_trades": len(self.transaction_history),
            "last_transaction": self.transaction_history[-1] if self.transaction_history else None
        }
    
    def get_transaction_history(self, limit: int = 10) -> List[dict]:
        """Retourne l'historique des transactions"""
        return self.transaction_history[-limit:] if self.transaction_history else []