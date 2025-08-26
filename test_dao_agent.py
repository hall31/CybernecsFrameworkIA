#!/usr/bin/env python3
"""
Script de test pour l'agent DAO
Teste la création complète d'une DAO avec tokenisation, gouvernance et trésorerie
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'core-engine'))

from agents.dao_agent import TokenisationAgent, GovernanceAgent, TreasuryAgent, DAOOrchestrator

def test_tokenisation_agent():
    """Test du TokenisationAgent"""
    print("🧪 Test du TokenisationAgent...")
    
    try:
        agent = TokenisationAgent()
        result = agent.run("TEST123", 2_500_000)
        
        print(f"✅ Tokenisation réussie:")
        print(f"   📍 Adresse contrat: {result['contract_address']}")
        print(f"   🪙 Symbole: {result['token_symbol']}")
        print(f"   💰 Valorisation: {result['valuation']}")
        print(f"   💵 Prix par token: {result['price_per_token']}")
        print(f"   📊 Supply total: {result['total_supply']:,}")
        print(f"   🎯 Distribution:")
        print(f"      - Fondateur: {result['distribution']['founder']:,} tokens")
        print(f"      - Équipe: {result['distribution']['team']:,} tokens")
        print(f"      - Investisseurs: {result['distribution']['investors']:,} tokens")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur TokenisationAgent: {str(e)}")
        return False

def test_governance_agent():
    """Test du GovernanceAgent"""
    print("\n🧪 Test du GovernanceAgent...")
    
    try:
        agent = GovernanceAgent()
        result = agent.run("TEST123", "0xTOKEN123456789")
        
        print(f"✅ Gouvernance DAO créée:")
        print(f"   🏛️ Adresse DAO: {result['dao_address']}")
        print(f"   🗳️ Pouvoir de vote: {result['voting_power']}")
        print(f"   📊 Quorum: {result['quorum']}")
        print(f"   ⏱️ Période de vote: {result['voting_period']}")
        print(f"   📋 Règles ({len(result['rules'])}):")
        for i, rule in enumerate(result['rules'], 1):
            print(f"      {i}. {rule}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur GovernanceAgent: {str(e)}")
        return False

def test_treasury_agent():
    """Test du TreasuryAgent"""
    print("\n🧪 Test du TreasuryAgent...")
    
    try:
        agent = TreasuryAgent()
        result = agent.run("TEST123", "0xDAO123456789")
        
        print(f"✅ Trésorerie DAO créée:")
        print(f"   💰 Adresse trésorerie: {result['treasury_address']}")
        print(f"   💵 Fonds disponibles: {result['funds']}")
        print(f"   📅 Distribution: {result['distribution_schedule']}")
        print(f"   🚫 Limite retrait: {result['withdrawal_limit']}")
        print(f"   📋 Règles ({len(result['rules'])}):")
        for i, rule in enumerate(result['rules'], 1):
            print(f"      {i}. {rule}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur TreasuryAgent: {str(e)}")
        return False

def test_dao_orchestrator():
    """Test de l'orchestrateur DAO complet"""
    print("\n🧪 Test du DAOOrchestrator (création complète)...")
    
    try:
        orchestrator = DAOOrchestrator()
        result = orchestrator.create_complete_dao("TEST123", 5_000_000)
        
        print(f"🎉 DAO complète créée avec succès!")
        print(f"   📊 Projet ID: {result['project_id']}")
        print(f"   🪙 Token: {result['dao']['token']['token_symbol']}")
        print(f"   🏛️ DAO: {result['dao']['dao']['dao_address']}")
        print(f"   💰 Treasury: {result['dao']['treasury']['treasury_address']}")
        print(f"   ⏰ Timestamp: {result['timestamp']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur DAOOrchestrator: {str(e)}")
        return False

def test_api_endpoint():
    """Test de l'endpoint API simulé"""
    print("\n🧪 Test de l'endpoint API...")
    
    try:
        from core_engine.main import create_startup_endpoint
        
        result = create_startup_endpoint("SaaS marketplace pour freelances")
        
        if result["success"]:
            print(f"✅ API Endpoint réussi:")
            print(f"   📊 Projet ID: {result['data']['project_id']}")
            print(f"   💡 Idée: {result['data']['idea']}")
            print(f"   💰 Valorisation: {result['data']['valuation']:,.0f} €")
            print(f"   🪙 Token: {result['data']['dao']['token']['token_symbol']}")
            print(f"   🏛️ DAO: {result['data']['dao']['dao']['dao_address']}")
            print(f"   💰 Treasury: {result['data']['dao']['treasury']['treasury_address']}")
            return True
        else:
            print(f"❌ API Endpoint échoué: {result['error']}")
            return False
            
    except Exception as e:
        print(f"❌ Erreur API Endpoint: {str(e)}")
        return False

def main():
    """Fonction principale de test"""
    print("🚀 Démarrage des tests de l'agent DAO...\n")
    
    tests = [
        ("TokenisationAgent", test_tokenisation_agent),
        ("GovernanceAgent", test_governance_agent),
        ("TreasuryAgent", test_treasury_agent),
        ("DAOOrchestrator", test_dao_orchestrator),
        ("API Endpoint", test_api_endpoint)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            success = test_func()
            results.append((test_name, success))
        except Exception as e:
            print(f"❌ Test {test_name} a échoué avec une exception: {str(e)}")
            results.append((test_name, False))
    
    # Résumé des tests
    print("\n" + "="*50)
    print("📊 RÉSUMÉ DES TESTS")
    print("="*50)
    
    passed = sum(1 for _, success in results if success)
    total = len(results)
    
    for test_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"   {status} {test_name}")
    
    print(f"\n🎯 Résultat: {passed}/{total} tests réussis")
    
    if passed == total:
        print("🎉 Tous les tests sont passés avec succès!")
        return 0
    else:
        print("⚠️ Certains tests ont échoué")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)