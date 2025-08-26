from typing import Dict, List, Optional
from datetime import datetime
from utils.logger import log_event, log_success, log_warning

class TraderContract:
    """
    Smart Contract simplifié pour la gestion des trades du Hedge Fund
    """
    
    def __init__(self):
        self.name = "TraderContract"
        self.admin = "HedgeFundAgent"
        self.positions = {}  # Ledger on-chain des positions
        self.trade_history = []
        self.total_volume = 0.0
        self.fees_collected = 0.0
        self.fee_rate = 0.001  # 0.1% de frais par trade
        
        # Initialisation du ledger
        self._initialize_ledger()
        
        log_event(self.name, "Smart contract deployed and initialized")
    
    def _initialize_ledger(self):
        """Initialise le ledger avec des positions vides"""
        available_tokens = [
            "STK001", "STK002", "STK003", "STK004", "STK005",
            "ETF001", "ETF002", "ETF003"
        ]
        
        for token in available_tokens:
            self.positions[token] = {
                "long_amount": 0.0,
                "short_amount": 0.0,
                "avg_long_price": 0.0,
                "avg_short_price": 0.0,
                "last_trade": None,
                "total_trades": 0
            }
    
    def buy(self, token: str, amount: float, price: float, caller: str) -> dict:
        """
        Achète des tokens (position long)
        
        Args:
            token: Identifiant du token
            amount: Montant en USD
            price: Prix d'achat
            caller: Adresse de l'appelant
            
        Returns:
            dict: Résultat de l'opération
        """
        if caller != self.admin:
            log_warning(self.name, f"Unauthorized buy attempt by {caller}")
            return {"success": False, "error": "Unauthorized caller"}
        
        if token not in self.positions:
            return {"success": False, "error": "Token not supported"}
        
        if amount <= 0:
            return {"success": False, "error": "Invalid amount"}
        
        try:
            # Calcul des frais
            fees = amount * self.fee_rate
            net_amount = amount - fees
            
            # Mise à jour des positions
            current_position = self.positions[token]
            current_long = current_position["long_amount"]
            current_avg_price = current_position["avg_long_price"]
            
            # Calcul du nouveau prix moyen
            if current_long > 0:
                new_avg_price = ((current_long * current_avg_price) + (net_amount * price)) / (current_long + net_amount)
            else:
                new_avg_price = price
            
            # Mise à jour du ledger
            self.positions[token]["long_amount"] += net_amount
            self.positions[token]["avg_long_price"] = new_avg_price
            self.positions[token]["last_trade"] = datetime.now().isoformat()
            self.positions[token]["total_trades"] += 1
            
            # Mise à jour des statistiques
            self.total_volume += amount
            self.fees_collected += fees
            
            # Enregistrement du trade
            trade_record = {
                "id": f"TRADE_{len(self.trade_history) + 1:06d}",
                "timestamp": datetime.now().isoformat(),
                "token": token,
                "action": "BUY",
                "amount_usd": amount,
                "price": price,
                "fees": fees,
                "net_amount": net_amount,
                "caller": caller
            }
            self.trade_history.append(trade_record)
            
            log_success(self.name, f"BUY {token}: ${amount:,.2f} at ${price:.2f}")
            
            return {
                "success": True,
                "trade_id": trade_record["id"],
                "token": token,
                "action": "BUY",
                "amount_usd": amount,
                "price": price,
                "fees": fees,
                "net_amount": net_amount,
                "new_position": self.positions[token]["long_amount"]
            }
            
        except Exception as e:
            log_event(self.name, f"Error in buy operation: {str(e)}", "ERROR")
            return {"success": False, "error": str(e)}
    
    def sell(self, token: str, amount: float, price: float, caller: str) -> dict:
        """
        Vend des tokens (position short ou fermeture long)
        
        Args:
            token: Identifiant du token
            amount: Montant en USD
            price: Prix de vente
            caller: Adresse de l'appelant
            
        Returns:
            dict: Résultat de l'opération
        """
        if caller != self.admin:
            log_warning(self.name, f"Unauthorized sell attempt by {caller}")
            return {"success": False, "error": "Unauthorized caller"}
        
        if token not in self.positions:
            return {"success": False, "error": "Token not supported"}
        
        if amount <= 0:
            return {"success": False, "error": "Invalid amount"}
        
        try:
            current_position = self.positions[token]
            current_long = current_position["long_amount"]
            
            # Calcul des frais
            fees = amount * self.fee_rate
            net_amount = amount - fees
            
            # Déterminer le type de vente
            if current_long >= net_amount:
                # Fermeture de position long
                action = "CLOSE_LONG"
                remaining_long = current_long - net_amount
                self.positions[token]["long_amount"] = remaining_long
                
                # Calcul du P&L
                avg_price = current_position["avg_long_price"]
                pnl = (price - avg_price) * net_amount
                
            else:
                # Ouverture de position short
                action = "OPEN_SHORT"
                short_amount = net_amount - current_long
                self.positions[token]["short_amount"] += short_amount
                
                # Mise à jour du prix moyen short
                current_short = current_position["short_amount"] - short_amount
                current_avg_short = current_position["avg_short_price"]
                
                if current_short > 0:
                    new_avg_short = ((current_short * current_avg_short) + (short_amount * price)) / (current_short + short_amount)
                else:
                    new_avg_short = price
                
                self.positions[token]["avg_short_price"] = new_avg_short
                self.positions[token]["long_amount"] = 0
                
                pnl = 0  # Pas de P&L immédiat pour les shorts
            
            # Mise à jour du ledger
            self.positions[token]["last_trade"] = datetime.now().isoformat()
            self.positions[token]["total_trades"] += 1
            
            # Mise à jour des statistiques
            self.total_volume += amount
            self.fees_collected += fees
            
            # Enregistrement du trade
            trade_record = {
                "id": f"TRADE_{len(self.trade_history) + 1:06d}",
                "timestamp": datetime.now().isoformat(),
                "token": token,
                "action": action,
                "amount_usd": amount,
                "price": price,
                "fees": fees,
                "net_amount": net_amount,
                "pnl": pnl,
                "caller": caller
            }
            self.trade_history.append(trade_record)
            
            log_success(self.name, f"SELL {token}: ${amount:,.2f} at ${price:.2f} ({action})")
            
            return {
                "success": True,
                "trade_id": trade_record["id"],
                "token": token,
                "action": action,
                "amount_usd": amount,
                "price": price,
                "fees": fees,
                "net_amount": net_amount,
                "pnl": pnl,
                "new_position": {
                    "long": self.positions[token]["long_amount"],
                    "short": self.positions[token]["short_amount"]
                }
            }
            
        except Exception as e:
            log_event(self.name, f"Error in sell operation: {str(e)}", "ERROR")
            return {"success": False, "error": str(e)}
    
    def rebalance(self, caller: str) -> dict:
        """
        Exécute le rebalancement du portefeuille
        
        Args:
            caller: Adresse de l'appelant
            
        Returns:
            dict: Résultat du rebalancement
        """
        if caller != self.admin:
            log_warning(self.name, f"Unauthorized rebalance attempt by {caller}")
            return {"success": False, "error": "Unauthorized caller"}
        
        try:
            log_event(self.name, "Starting portfolio rebalancing")
            
            # Calcul des positions actuelles
            total_long_value = 0.0
            total_short_value = 0.0
            
            for token, position in self.positions.items():
                total_long_value += position["long_amount"]
                total_short_value += position["short_amount"]
            
            # Log du rebalancement
            rebalance_record = {
                "timestamp": datetime.now().isoformat(),
                "total_long_value": total_long_value,
                "total_short_value": total_short_value,
                "total_positions": len([p for p in self.positions.values() if p["long_amount"] > 0 or p["short_amount"] > 0])
            }
            
            log_success(self.name, f"Portfolio rebalanced - Long: ${total_long_value:,.2f}, Short: ${total_short_value:,.2f}")
            
            return {
                "success": True,
                "message": "Portfolio rebalanced successfully",
                "rebalance_data": rebalance_record,
                "current_positions": self.positions
            }
            
        except Exception as e:
            log_event(self.name, f"Error in rebalance operation: {str(e)}", "ERROR")
            return {"success": False, "error": str(e)}
    
    def get_positions(self) -> dict:
        """Retourne toutes les positions actuelles"""
        return {
            "positions": self.positions,
            "total_volume": self.total_volume,
            "fees_collected": self.fees_collected,
            "total_trades": len(self.trade_history)
        }
    
    def get_trade_history(self, limit: int = 50) -> dict:
        """Retourne l'historique des trades"""
        return {
            "trades": self.trade_history[-limit:] if limit > 0 else self.trade_history,
            "total_trades": len(self.trade_history)
        }
    
    def get_portfolio_summary(self) -> dict:
        """Retourne un résumé du portefeuille"""
        total_long = sum(pos["long_amount"] for pos in self.positions.values())
        total_short = sum(pos["short_amount"] for pos in self.positions.values())
        
        return {
            "total_long_value": total_long,
            "total_short_value": total_short,
            "net_exposure": total_long - total_short,
            "total_positions": len([p for p in self.positions.values() if p["long_amount"] > 0 or p["short_amount"] > 0]),
            "total_volume": self.total_volume,
            "fees_collected": self.fees_collected,
            "total_trades": len(self.trade_history)
        }