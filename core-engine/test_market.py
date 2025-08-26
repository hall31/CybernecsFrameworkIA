#!/usr/bin/env python3
"""
Script de test pour le MarketAgent
"""

import sys
import os

# Ajouter le répertoire courant au path Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from agents.market_agent import MarketAgent
    
    print("🚀 Test du MarketAgent...")
    
    # Créer une instance
    agent = MarketAgent()
    print("✅ MarketAgent créé avec succès")
    
    # Exécuter le run
    result = agent.run()
    print("✅ Marketplace initialisé avec succès!")
    
    # Afficher les résultats
    print(f"📊 Tokens listés: {len(result['listed_tokens'])}")
    print(f"🏦 Market Address: {result['market_address']}")
    print(f"💰 Market Cap Total: {result['market_stats']['total_market_cap']:,} €")
    
    # Afficher les premiers tokens
    print("\n📋 Premiers tokens listés:")
    for i, token in enumerate(result['listed_tokens'][:3]):
        print(f"  {i+1}. {token['symbol']} - {token['name']} - {token['price_eur']}")
    
    print("\n🎉 Test réussi! Le MarketAgent fonctionne correctement.")
    
except ImportError as e:
    print(f"❌ Erreur d'import: {e}")
    print("💡 Assurez-vous que tous les fichiers sont présents")
except Exception as e:
    print(f"❌ Erreur lors du test: {e}")
    import traceback
    traceback.print_exc()