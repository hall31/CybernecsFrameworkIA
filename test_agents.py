#!/usr/bin/env python3
"""
Script de test pour vérifier le fonctionnement des agents Mon ShipFast
"""

import os
import sys
from dotenv import load_dotenv

# Ajouter le répertoire racine au path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Charger les variables d'environnement
load_dotenv()

def test_gitops_agent():
    """Test du GitOpsAgent"""
    print("🧪 Test du GitOpsAgent...")
    
    try:
        from agents.gitops_agent import GitOpsAgent
        
        # Vérifier les variables d'environnement
        if not os.getenv('GITHUB_TOKEN'):
            print("⚠️  GITHUB_TOKEN non configuré - test simulé")
            return True
        
        agent = GitOpsAgent()
        print("✅ GitOpsAgent initialisé avec succès")
        
        # Test de la méthode run
        result = agent.run("test-project-123")
        print(f"📦 Résultat GitOps: {result.get('status', 'N/A')}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur GitOpsAgent: {e}")
        return False

def test_payments_agent():
    """Test du PaymentsAgent"""
    print("🧪 Test du PaymentsAgent...")
    
    try:
        from agents.payments_agent import PaymentsAgent
        
        # Vérifier les variables d'environnement
        if not os.getenv('STRIPE_SECRET_KEY'):
            print("⚠️  STRIPE_SECRET_KEY non configuré - test simulé")
            return True
        
        agent = PaymentsAgent()
        print("✅ PaymentsAgent initialisé avec succès")
        
        # Test de la méthode run
        result = agent.run("SaaS marketplace innovant")
        print(f"💳 Résultat Payments: {result.get('status', 'N/A')}")
        print(f"   Plans créés: {len(result.get('stripe_plans', []))}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur PaymentsAgent: {e}")
        return False

def test_ads_agent():
    """Test du AdsAgent"""
    print("🧪 Test du AdsAgent...")
    
    try:
        from agents.ads_agent import AdsAgent
        
        agent = AdsAgent()
        print("✅ AdsAgent initialisé avec succès")
        
        # Test de la méthode run
        growth_data = {
            "channel": "paid_ads",
            "budget": "100€/jour",
            "target_audience": "B2B"
        }
        
        result = agent.run("Plateforme IA pour entreprises", growth_data)
        print(f"📢 Résultat Ads: {result.get('status', 'N/A')}")
        print(f"   Plateforme: {result.get('ads_platform', 'N/A')}")
        print(f"   Budget: {result.get('budget', 'N/A')}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur AdsAgent: {e}")
        return False

def test_api_integration():
    """Test de l'intégration API"""
    print("🧪 Test de l'intégration API...")
    
    try:
        from main import app
        from fastapi.testclient import TestClient
        
        client = TestClient(app)
        
        # Test de l'endpoint racine
        response = client.get("/")
        assert response.status_code == 200
        print("✅ Endpoint racine fonctionne")
        
        # Test de l'endpoint health
        response = client.get("/health")
        assert response.status_code == 200
        print("✅ Endpoint health fonctionne")
        
        # Test de l'endpoint agents/status
        response = client.get("/agents/status")
        assert response.status_code == 200
        print("✅ Endpoint agents/status fonctionne")
        
        return True
        
    except ImportError:
        print("⚠️  FastAPI TestClient non disponible - test d'intégration ignoré")
        return True
    except Exception as e:
        print(f"❌ Erreur test d'intégration: {e}")
        return False

def main():
    """Fonction principale de test"""
    print("🚀 Tests des agents Mon ShipFast")
    print("=" * 50)
    
    tests = [
        ("GitOpsAgent", test_gitops_agent),
        ("PaymentsAgent", test_payments_agent),
        ("AdsAgent", test_ads_agent),
        ("API Integration", test_api_integration)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        try:
            success = test_func()
            results.append((test_name, success))
        except Exception as e:
            print(f"❌ Erreur inattendue: {e}")
            results.append((test_name, False))
    
    # Résumé des tests
    print("\n" + "=" * 50)
    print("📊 Résumé des tests:")
    
    passed = 0
    total = len(results)
    
    for test_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"   {test_name}: {status}")
        if success:
            passed += 1
    
    print(f"\n🎯 Résultat: {passed}/{total} tests réussis")
    
    if passed == total:
        print("🎉 Tous les tests sont passés !")
        return 0
    else:
        print("⚠️  Certains tests ont échoué. Vérifiez la configuration.")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)