#!/usr/bin/env python3
"""
Démonstration du FundAgent sans dépendances externes
"""

import sys
import os

# Ajouter le répertoire parent au path pour les imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.fund_agent import FundAgent
from utils.logger import log_event

def demo_fund_creation():
    """Démonstration de la création de fonds"""
    print("🚀 Démonstration du FundAgent")
    print("=" * 50)
    
    # Initialiser l'agent
    fund_agent = FundAgent()
    
    # Créer plusieurs fonds
    startups_list = [
        ["STK001", "STK002"],
        ["STK001", "STK002", "STK003"],
        ["STK001", "STK002", "STK003", "STK004"],
        ["STK001", "STK002", "STK003", "STK004", "STK005"]
    ]
    
    created_funds = []
    
    for i, startups in enumerate(startups_list, 1):
        print(f"\n📊 Création du fonds {i} avec {len(startups)} startups...")
        print(f"   Startups: {', '.join(startups)}")
        
        try:
            fund = fund_agent.run(startups)
            created_funds.append(fund)
            
            print(f"   ✅ Fonds créé: {fund['fund_symbol']}")
            print(f"   📍 Adresse: {fund['fund_address']}")
            print(f"   💰 NAV: {fund['nav']}")
            print(f"   📈 Composition:")
            for item in fund['composition']:
                print(f"      - {item['token']}: {item['weight']}")
                
        except Exception as e:
            print(f"   ❌ Erreur: {e}")
    
    # Afficher tous les fonds
    print(f"\n📋 Résumé des fonds créés:")
    print("=" * 50)
    
    all_funds = fund_agent.get_all_funds()
    for fund in all_funds:
        print(f"🏦 {fund['fund_symbol']}")
        print(f"   NAV: {fund['nav']}")
        print(f"   Statut: {fund['status']}")
        print(f"   Startups: {len(fund['composition'])}")
        print()
    
    # Test des méthodes utilitaires
    print("🔍 Tests des méthodes utilitaires:")
    print("=" * 50)
    
    if created_funds:
        first_fund = created_funds[0]
        symbol = first_fund['fund_symbol']
        
        # Test get_fund_by_symbol
        fund_by_symbol = fund_agent.get_fund_by_symbol(symbol)
        if fund_by_symbol:
            print(f"✅ Récupération par symbole {symbol}: OK")
        
        # Test update_fund_nav
        success = fund_agent.update_fund_nav(symbol, "110.50 €")
        if success:
            print(f"✅ Mise à jour NAV pour {symbol}: OK")
        
        # Test get_fund_by_address
        address = first_fund['fund_address']
        fund_by_address = fund_agent.get_fund_by_address(address)
        if fund_by_address:
            print(f"✅ Récupération par adresse {address[:10]}...: OK")
    
    print("\n🎉 Démonstration terminée avec succès!")

if __name__ == "__main__":
    demo_fund_creation()