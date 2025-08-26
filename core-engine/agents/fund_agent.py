from utils.logger import log_event
from typing import Dict, List, Optional
import random
import string
from datetime import datetime

class FundAgent:
    def __init__(self):
        self.name = "Fund Agent"
        self.funds_created = []
        log_event(self.name, "Initialized")
    
    def run(self, selected_startups: List[str]) -> dict:
        """
        Create a decentralized AI Startup Fund (ETF)
        
        Args:
            selected_startups (List[str]): List of startup token symbols
            
        Returns:
            dict: Fund details including smart contract address and composition
        """
        log_event(self.name, f"Creating fund with {len(selected_startups)} startups: {selected_startups}")
        
        try:
            # Validate input
            if len(selected_startups) < 2:
                raise ValueError("Minimum 2 startups required to create a fund")
            
            # Generate unique fund symbol
            fund_symbol = self._generate_fund_symbol()
            
            # Create fund composition with weights
            composition = self._create_fund_composition(selected_startups)
            
            # Generate smart contract address (simulated)
            fund_address = self._generate_fund_address()
            
            # Calculate NAV (Net Asset Value)
            nav = self._calculate_nav(composition)
            
            # Create fund object
            fund = {
                "fund_address": fund_address,
                "fund_symbol": fund_symbol,
                "composition": composition,
                "nav": nav,
                "created_at": datetime.now().isoformat(),
                "status": "active"
            }
            
            # Store fund
            self.funds_created.append(fund)
            
            log_event(self.name, f"New AI fund ETF created: {fund_symbol}")
            
            return fund
            
        except Exception as e:
            log_event(self.name, f"Error creating fund: {str(e)}", "ERROR")
            raise
    
    def _generate_fund_symbol(self) -> str:
        """Generate unique fund symbol (ETF + 3 digits)"""
        # Generate random 3-digit number
        digits = ''.join(random.choices(string.digits, k=3))
        symbol = f"ETF{digits}"
        
        # Ensure uniqueness
        existing_symbols = [fund["fund_symbol"] for fund in self.funds_created]
        while symbol in existing_symbols:
            digits = ''.join(random.choices(string.digits, k=3))
            symbol = f"ETF{digits}"
        
        return symbol
    
    def _create_fund_composition(self, startups: List[str]) -> List[Dict]:
        """Create fund composition with balanced weights"""
        composition = []
        total_startups = len(startups)
        
        # Calculate weights (balanced distribution)
        if total_startups == 2:
            weights = [60, 40]  # 60% for first, 40% for second
        elif total_startups == 3:
            weights = [40, 30, 30]  # 40%, 30%, 30%
        elif total_startups == 4:
            weights = [30, 25, 25, 20]  # 30%, 25%, 25%, 20%
        else:
            # For more than 4 startups, use decreasing weights
            base_weight = 100 // total_startups
            weights = [base_weight] * total_startups
            # Distribute remaining percentage to first startup
            weights[0] += 100 - (base_weight * total_startups)
        
        for i, startup in enumerate(startups):
            composition.append({
                "token": startup,
                "weight": f"{weights[i]}%",
                "percentage": weights[i]
            })
        
        return composition
    
    def _generate_fund_address(self) -> str:
        """Generate simulated Ethereum smart contract address"""
        # Simulate Ethereum address format (0x + 40 hex characters)
        hex_chars = ''.join(random.choices('0123456789abcdef', k=40))
        return f"0x{hex_chars}"
    
    def _calculate_nav(self, composition: List[Dict]) -> str:
        """Calculate Net Asset Value (simulated)"""
        # Simulate NAV calculation based on composition
        base_nav = 100  # Base NAV in EUR
        # Add some variation based on number of startups
        variation = random.uniform(0.8, 1.2)
        nav = base_nav * variation
        
        return f"{nav:.2f} €"
    
    def get_all_funds(self) -> List[Dict]:
        """Get all created funds"""
        return self.funds_created
    
    def get_fund_by_symbol(self, symbol: str) -> Optional[Dict]:
        """Get fund by symbol"""
        for fund in self.funds_created:
            if fund["fund_symbol"] == symbol:
                return fund
        return None
    
    def get_fund_by_address(self, address: str) -> Optional[Dict]:
        """Get fund by smart contract address"""
        for fund in self.funds_created:
            if fund["fund_address"] == address:
                return fund
        return None
    
    def update_fund_nav(self, fund_symbol: str, new_nav: str) -> bool:
        """Update fund NAV (for market fluctuations)"""
        fund = self.get_fund_by_symbol(fund_symbol)
        if fund:
            fund["nav"] = new_nav
            fund["updated_at"] = datetime.now().isoformat()
            log_event(self.name, f"Updated NAV for {fund_symbol}: {new_nav}")
            return True
        return False
    
    def deactivate_fund(self, fund_symbol: str) -> bool:
        """Deactivate a fund"""
        fund = self.get_fund_by_symbol(fund_symbol)
        if fund:
            fund["status"] = "inactive"
            fund["deactivated_at"] = datetime.now().isoformat()
            log_event(self.name, f"Deactivated fund: {fund_symbol}")
            return True
        return False