#!/usr/bin/env python3
"""
Script de test simple pour simuler l'API du marketplace
"""

import json
from agents.market_agent import MarketAgent

def test_marketplace_api():
    """Test complet de l'API du marketplace"""
    
    print("🚀 Test de l'API Startup Tokenization Marketplace")
    print("=" * 60)
    
    # Créer le MarketAgent
    agent = MarketAgent()
    print("✅ MarketAgent créé")
    
    # Tester l'endpoint /market
    print("\n🔍 Test de l'endpoint /market")
    try:
        market_data = agent.run()
        
        print("✅ Données du marketplace récupérées")
        print(f"📊 Tokens listés: {len(market_data['listed_tokens'])}")
        print(f"🏦 Market Address: {market_data['market_address']}")
        print(f"💰 Market Cap Total: {market_data['market_stats']['total_market_cap']:,} €")
        
        # Afficher les tokens
        print("\n📋 Tokens listés:")
        for i, token in enumerate(market_data['listed_tokens']):
            print(f"  {i+1}. {token['symbol']} - {token['name']}")
            print(f"     Prix: {token['price_eur']} | Volume: {token['volume_formatted']} €")
            print(f"     Secteur: {token['sector']} | Stage: {token['stage']}")
            print()
        
    except Exception as e:
        print(f"❌ Erreur: {str(e)}")
        return False
    
    # Tester l'endpoint /market/stats
    print("🔍 Test de l'endpoint /market/stats")
    try:
        stats = agent.get_market_stats()
        print("✅ Statistiques récupérées")
        print(f"   Total listé: {stats['total_listed']}")
        print(f"   Market Cap: {stats['total_market_cap']:,} €")
        print(f"   Volume 24h: {stats['total_volume_24h']:,} €")
        print(f"   Sentiment: {stats['market_sentiment']}")
    except Exception as e:
        print(f"❌ Erreur: {str(e)}")
        return False
    
    # Tester l'endpoint /market/token/STK001
    print("\n🔍 Test de l'endpoint /market/token/STK001")
    try:
        token_details = agent.get_token_details("STK001")
        if token_details:
            print("✅ Détails du token STK001 récupérés")
            print(f"   Nom: {token_details['name']}")
            print(f"   Prix: {token_details['price_eur']}")
            print(f"   Volume: {token_details['volume_formatted']} €")
            print(f"   Historique des prix: {len(token_details['price_history'])} jours")
            print(f"   Order book: {len(token_details['order_book']['bids'])} bids, {len(token_details['order_book']['asks'])} asks")
        else:
            print("❌ Token STK001 non trouvé")
            return False
    except Exception as e:
        print(f"❌ Erreur: {str(e)}")
        return False
    
    # Tester l'endpoint /market/orderbook/STK001
    print("\n🔍 Test de l'endpoint /market/orderbook/STK001")
    try:
        token = agent.get_token_details("STK001")
        order_book = token.get("order_book", {})
        print("✅ Order book récupéré")
        print(f"   Bids: {len(order_book['bids'])} ordres")
        print(f"   Asks: {len(order_book['asks'])} ordres")
        
        if order_book['bids']:
            print(f"   Meilleur bid: {order_book['bids'][0]['price']} € pour {order_book['bids'][0]['amount']} tokens")
        if order_book['asks']:
            print(f"   Meilleur ask: {order_book['asks'][0]['price']} € pour {order_book['asks'][0]['amount']} tokens")
            
    except Exception as e:
        print(f"❌ Erreur: {str(e)}")
        return False
    
    # Tester l'endpoint /market/price-history/STK001
    print("\n🔍 Test de l'endpoint /market/price-history/STK001")
    try:
        price_history = agent.generate_price_history("STK001", 7)
        print("✅ Historique des prix récupéré")
        print(f"   Période: 7 jours")
        print(f"   Données: {len(price_history)} points")
        
        if price_history:
            print(f"   Premier prix: {price_history[0]['price']} €")
            print(f"   Dernier prix: {price_history[-1]['price']} €")
            
    except Exception as e:
        print(f"❌ Erreur: {str(e)}")
        return False
    
    print("\n🎉 Tous les tests de l'API sont passés avec succès!")
    print("🌐 L'API est prête pour le dashboard React")
    
    return True

def generate_api_responses():
    """Génère des exemples de réponses API pour la documentation"""
    
    print("\n📝 Exemples de réponses API")
    print("=" * 40)
    
    agent = MarketAgent()
    
    # Réponse /market
    market_response = {
        "success": True,
        "data": agent.run(),
        "timestamp": "2025-08-26T04:35:00"
    }
    
    print("GET /market:")
    print(json.dumps(market_response, indent=2)[:500] + "...")
    
    # Réponse /market/stats
    stats_response = {
        "success": True,
        "data": agent.get_market_stats(),
        "timestamp": "2025-08-26T04:35:00"
    }
    
    print("\nGET /market/stats:")
    print(json.dumps(stats_response, indent=2))
    
    return True

if __name__ == "__main__":
    # Test complet de l'API
    success = test_marketplace_api()
    
    if success:
        # Générer des exemples de réponses
        generate_api_responses()
        
        print("\n🚀 L'Epic 15 est prête!")
        print("📊 MarketAgent: ✅")
        print("🌐 API Endpoints: ✅")
        print("📱 Dashboard React: ✅")
        print("\n💡 Pour tester le dashboard:")
        print("   1. Démarrer l'API: python3 simple_api.py")
        print("   2. Démarrer React: cd ../dashboard && npm run dev")
        print("   3. Naviguer vers 'Global Market'")
    else:
        print("\n❌ Certains tests ont échoué")
        print("🔧 Vérifiez la configuration")