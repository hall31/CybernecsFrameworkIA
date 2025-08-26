#!/usr/bin/env python3
"""
Script de démonstration pour l'API Startup Tokenization Marketplace
"""

import requests
import json
import time

# Configuration
BASE_URL = "http://localhost:5000"

def test_api_endpoint(endpoint, description):
    """Test un endpoint de l'API"""
    try:
        print(f"\n🔍 Test: {description}")
        print(f"   URL: {BASE_URL}{endpoint}")
        
        response = requests.get(f"{BASE_URL}{endpoint}", timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Statut: {response.status_code}")
            print(f"   📊 Données: {len(str(data))} caractères")
            
            if 'data' in data and 'listed_tokens' in data['data']:
                tokens = data['data']['listed_tokens']
                print(f"   🪙 Tokens listés: {len(tokens)}")
                for token in tokens[:3]:  # Afficher les 3 premiers
                    print(f"      - {token['symbol']}: {token['name']} @ {token['price_eur']}")
            
            return True
        else:
            print(f"   ❌ Erreur: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print(f"   ❌ Erreur de connexion: L'API n'est pas démarrée")
        return False
    except Exception as e:
        print(f"   ❌ Erreur: {str(e)}")
        return False

def main():
    """Fonction principale de démonstration"""
    print("🚀 Démonstration de l'API Startup Tokenization Marketplace")
    print("=" * 60)
    
    # Attendre que l'API soit prête
    print("\n⏳ Vérification de la disponibilité de l'API...")
    max_attempts = 10
    for attempt in range(max_attempts):
        try:
            response = requests.get(f"{BASE_URL}/health", timeout=2)
            if response.status_code == 200:
                print("✅ API prête!")
                break
        except:
            if attempt < max_attempts - 1:
                print(f"   Tentative {attempt + 1}/{max_attempts}...")
                time.sleep(1)
            else:
                print("❌ L'API n'est pas accessible")
                print("💡 Assurez-vous que l'API est démarrée avec: python3 main.py")
                return
    
    # Tests des endpoints
    endpoints = [
        ("/health", "Vérification de santé"),
        ("/market", "Données du marketplace"),
        ("/market/stats", "Statistiques du marché"),
        ("/market/token/STK001", "Détails du token STK001"),
        ("/market/orderbook/STK001", "Order book du token STK001"),
        ("/market/price-history/STK001", "Historique des prix STK001")
    ]
    
    success_count = 0
    for endpoint, description in endpoints:
        if test_api_endpoint(endpoint, description):
            success_count += 1
    
    # Résumé
    print(f"\n📊 Résumé des tests:")
    print(f"   ✅ Succès: {success_count}/{len(endpoints)}")
    print(f"   ❌ Échecs: {len(endpoints) - success_count}/{len(endpoints)}")
    
    if success_count == len(endpoints):
        print("\n🎉 Tous les tests sont passés avec succès!")
        print("🌐 L'API est prête pour le dashboard React")
    else:
        print("\n⚠️  Certains tests ont échoué")
        print("🔧 Vérifiez la configuration de l'API")

if __name__ == "__main__":
    main()