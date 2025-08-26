#!/usr/bin/env python3
"""
Test de l'InvestorAgent
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.investor_agent import InvestorAgent
import json

def test_investor_agent():
    """Test complet de l'InvestorAgent"""
    
    print("🧪 Test de l'InvestorAgent")
    print("=" * 50)
    
    # Création de l'agent
    investor = InvestorAgent()
    print("✅ InvestorAgent créé avec succès")
    
    # Données de test
    project_id = "test-startup-001"
    
    finance_data = {
        "current_revenue": 12000,
        "projected_revenue": 180000,
        "stripe_revenue": 15000,
        "monthly_costs": 8000,
        "profit_margin": 0.33,
        "cash_flow": 4000
    }
    
    growth_data = {
        "cac": 45,
        "ltv": 500,
        "ctr": 0.08,
        "conversion_rate": 0.025,
        "monthly_growth": 0.15,
        "user_retention": 0.85
    }
    
    optimizer_data = {
        "churn_rate": 0.03,
        "optimization_score": 0.78,
        "recommended_actions": [
            "Augmenter le budget marketing de 20%",
            "Optimiser la page de conversion",
            "Améliorer l'onboarding utilisateur"
        ],
        "predicted_improvement": 0.25
    }
    
    print("\n📊 Données de test:")
    print(f"  - Projet: {project_id}")
    print(f"  - CA actuel: {finance_data['current_revenue']} €")
    print(f"  - CAC: {growth_data['cac']} €")
    print(f"  - LTV: {growth_data['ltv']} €")
    print(f"  - Churn: {optimizer_data['churn_rate'] * 100}%")
    
    # Test de l'évaluation
    print("\n🚀 Lancement de l'évaluation...")
    try:
        result = investor.run(project_id, finance_data, growth_data, optimizer_data)
        print("✅ Évaluation terminée avec succès")
        
        # Affichage des résultats
        print("\n📈 Résultats de l'évaluation:")
        print(f"  - Valorisation: {result['valuation']}")
        print(f"  - Décision: {result['decision']}")
        print(f"  - Score de confiance: {result['confidence_score']:.1%}")
        print(f"  - Prochain financement: {result['next_funding']}")
        
        print("\n📊 KPIs:")
        for kpi, value in result['kpis'].items():
            print(f"  - {kpi}: {value}")
        
        print(f"\n🆔 ID du projet: {result['project_id']}")
        print(f"📅 Date d'analyse: {result['analysis_date']}")
        
        # Test de formatage JSON
        json_result = json.dumps(result, indent=2, ensure_ascii=False)
        print("\n📄 Résultat JSON:")
        print(json_result)
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors de l'évaluation: {str(e)}")
        return False

def test_error_handling():
    """Test de la gestion d'erreurs"""
    
    print("\n🧪 Test de gestion d'erreurs")
    print("=" * 50)
    
    investor = InvestorAgent()
    
    # Test avec des données invalides
    try:
        result = investor.run("error-test", {}, {}, {})
        print("✅ Gestion d'erreur fonctionne")
        print(f"  - Résultat: {result['decision']}")
        return True
    except Exception as e:
        print(f"❌ Erreur inattendue: {str(e)}")
        return False

def test_business_types():
    """Test des différents types de business"""
    
    print("\n🧪 Test des types de business")
    print("=" * 50)
    
    investor = InvestorAgent()
    
    # Test SaaS
    finance_saas = {"stripe_revenue": 20000, "current_revenue": 20000}
    growth_saas = {"ltv_cac_ratio": 3, "cac": 50, "ltv": 150}
    
    result_saas = investor.run("saas-test", finance_saas, growth_saas, {"churn_rate": 0.02})
    print(f"✅ Test SaaS: {result_saas['valuation']}")
    
    # Test AI
    finance_ai = {"stripe_revenue": 25000, "current_revenue": 25000}
    growth_ai = {"ltv_cac_ratio": 8, "cac": 30, "ltv": 240}
    
    result_ai = investor.run("ai-test", finance_ai, growth_ai, {"churn_rate": 0.01})
    print(f"✅ Test AI: {result_ai['valuation']}")
    
    return True

if __name__ == "__main__":
    print("🚀 Démarrage des tests de l'InvestorAgent")
    print("=" * 60)
    
    success_count = 0
    total_tests = 3
    
    # Test principal
    if test_investor_agent():
        success_count += 1
    
    # Test gestion d'erreurs
    if test_error_handling():
        success_count += 1
    
    # Test types de business
    if test_business_types():
        success_count += 1
    
    print("\n" + "=" * 60)
    print(f"📊 Résultats des tests: {success_count}/{total_tests} réussis")
    
    if success_count == total_tests:
        print("🎉 Tous les tests sont passés avec succès!")
    else:
        print("⚠️  Certains tests ont échoué")
    
    print("=" * 60)