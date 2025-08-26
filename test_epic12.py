#!/usr/bin/env python3
"""
Script de test pour l'Epic 12: AI Portfolio Manager
Teste tous les composants du système
"""

import requests
import json
import time
from datetime import datetime

BASE_URL = "http://localhost:5000"

def test_api_health():
    """Test de l'endpoint de santé"""
    print("🔍 Test de l'endpoint /health...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API en ligne - Service: {data['service']}")
            return True
        else:
            print(f"❌ Erreur HTTP: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Erreur de connexion: {e}")
        return False

def test_portfolio_endpoint():
    """Test de l'endpoint principal /portfolio"""
    print("\n🔍 Test de l'endpoint /portfolio...")
    try:
        response = requests.get("http://localhost:5000/portfolio")
        if response.status_code == 200:
            data = response.json()
            if data['success']:
                portfolio = data['data']
                print(f"✅ Portfolio récupéré avec succès")
                print(f"   📊 Total startups: {portfolio['total_startups']}")
                print(f"   💰 Valeur portefeuille: {portfolio['portfolio_value']}")
                print(f"   🏆 Best startup: {portfolio['best_startup']['name']} ({portfolio['best_startup']['valuation']})")
                print(f"   📈 Résumé: {portfolio['startups_summary']['invest']} invest, {portfolio['startups_summary']['hold']} hold, {portfolio['startups_summary']['drop']} drop")
                return True
            else:
                print(f"❌ Erreur dans la réponse: {data.get('error', 'Unknown')}")
                return False
        else:
            print(f"❌ Erreur HTTP: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Erreur de connexion: {e}")
        return False

def test_startups_endpoint():
    """Test de l'endpoint /portfolio/startups"""
    print("\n🔍 Test de l'endpoint /portfolio/startups...")
    try:
        response = requests.get("http://localhost:5000/portfolio/startups")
        if response.status_code == 200:
            data = response.json()
            if data['success']:
                startups = data['data']['startups']
                print(f"✅ {len(startups)} startups récupérées")
                print("   Top 3 startups:")
                for i, startup in enumerate(startups[:3], 1):
                    print(f"   {i}. {startup['name']} - {startup['valuation']} (MRR: {startup['mrr']:,}€)")
                return True
            else:
                print(f"❌ Erreur dans la réponse: {data.get('error', 'Unknown')}")
                return False
        else:
            print(f"❌ Erreur HTTP: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Erreur de connexion: {e}")
        return False

def test_startup_detail():
    """Test de l'endpoint /portfolio/startup/<id>"""
    print("\n🔍 Test de l'endpoint /portfolio/startup/startup001...")
    try:
        response = requests.get("http://localhost:5000/portfolio/startup/startup001")
        if response.status_code == 200:
            data = response.json()
            if data['success']:
                startup = data['data']
                print(f"✅ Startup détaillée récupérée")
                print(f"   🏢 {startup['name']} - {startup['idea']}")
                print(f"   💰 Valuation: {startup['valuation']}")
                print(f"   📊 MRR: {startup['mrr']:,}€, Churn: {startup['churn']:.1%}")
                print(f"   🎯 Status: {startup['status']}")
                return True
            else:
                print(f"❌ Erreur dans la réponse: {data.get('error', 'Unknown')}")
                return False
        else:
            print(f"❌ Erreur HTTP: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Erreur de connexion: {e}")
        return False

def test_analysis_endpoint():
    """Test de l'endpoint POST /portfolio/analysis"""
    print("\n🔍 Test de l'endpoint POST /portfolio/analysis...")
    try:
        response = requests.post("http://localhost:5000/portfolio/analysis")
        if response.status_code == 200:
            data = response.json()
            if data['success']:
                print(f"✅ Nouvelle analyse déclenchée avec succès")
                print(f"   📊 {data['data']['total_startups']} startups analysées")
                print(f"   💰 Valeur mise à jour: {data['data']['portfolio_value']}")
                return True
            else:
                print(f"❌ Erreur dans la réponse: {data.get('error', 'Unknown')}")
                return False
        else:
            print(f"❌ Erreur HTTP: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Erreur de connexion: {e}")
        return False

def test_portfolio_agent():
    """Test direct du PortfolioAgent"""
    print("\n🔍 Test direct du PortfolioAgent...")
    try:
        import sys
        sys.path.append('./core-engine')
        from agents.portfolio_agent import PortfolioAgent
        
        agent = PortfolioAgent()
        result = agent.run()
        
        if 'error' not in result:
            print(f"✅ PortfolioAgent fonctionne correctement")
            print(f"   📊 {result['total_startups']} startups analysées")
            print(f"   💰 Valeur: {result['portfolio_value']}")
            print(f"   🏆 Best: {result['best_startup']['name']} (Score: {result['best_startup']['score']})")
            return True
        else:
            print(f"❌ Erreur dans PortfolioAgent: {result['error']}")
            return False
    except Exception as e:
        print(f"❌ Erreur lors du test du PortfolioAgent: {e}")
        return False

def main():
    """Fonction principale de test"""
    print("🚀 Test de l'Epic 12: AI Portfolio Manager")
    print("=" * 50)
    print(f"⏰ Démarrage des tests: {datetime.now().strftime('%H:%M:%S')}")
    
    tests = [
        test_api_health,
        test_portfolio_endpoint,
        test_startups_endpoint,
        test_startup_detail,
        test_analysis_endpoint,
        test_portfolio_agent
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
            time.sleep(0.5)  # Pause entre les tests
        except Exception as e:
            print(f"❌ Erreur lors du test {test.__name__}: {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 Résumé des tests: {passed}/{total} réussis")
    
    if passed == total:
        print("🎉 Tous les tests sont passés avec succès !")
        print("✅ L'Epic 12 est prêt à être utilisé")
    else:
        print("⚠️  Certains tests ont échoué")
        print("🔧 Vérifiez la configuration et les logs")
    
    print(f"⏰ Fin des tests: {datetime.now().strftime('%H:%M:%S')}")

if __name__ == "__main__":
    main()