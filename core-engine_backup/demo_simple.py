#!/usr/bin/env python3
"""
Démonstration simple de l'orchestrateur StartupAI
"""

import time
from main import create_startup_endpoint, get_startup_endpoint

def analyze_investment_decision(startup_data):
    """Analyse et affiche la décision d'investissement"""
    print("\n" + "="*60)
    print("💰 ANALYSE D'INVESTISSEMENT")
    print("="*60)
    
    if "error" in startup_data:
        print(f"❌ Erreur: {startup_data['error']}")
        return
    
    # Extraction des données
    project_id = startup_data.get("project_id", "N/A")
    idea = startup_data.get("idea", "N/A")
    
    if "agents" in startup_data and "investor" in startup_data["agents"]:
        investor_data = startup_data["agents"]["investor"]
        
        print(f"🆔 Projet: {project_id}")
        print(f"💡 Idée: {idea}")
        print(f"📊 Valorisation: {investor_data.get('valuation', 'N/A')}")
        print(f"🎯 Décision: {investor_data.get('decision', 'N/A')}")
        print(f"📈 Score confiance: {investor_data.get('confidence_score', 0):.1%}")
        print(f"💰 Financement: {investor_data.get('next_funding', 'N/A')}")
        
        print("\n📊 KPIs Business:")
        kpis = investor_data.get('kpis', {})
        for kpi, value in kpis.items():
            print(f"  - {kpi}: {value}")
        
        print(f"\n📅 Date d'analyse: {investor_data.get('analysis_date', 'N/A')}")
        
    else:
        print("⚠️  Données d'investissement non disponibles")

def run_demo_scenarios():
    """Lance plusieurs scénarios de démonstration"""
    print("🎬 DÉMONSTRATION STARTUP AI - INVESTISSEUR IA")
    print("="*60)
    
    # Scénario 1: SaaS Marketplace
    print("\n📱 SCÉNARIO 1: SaaS Marketplace")
    print("-" * 40)
    saas_result = create_startup_endpoint("SaaS marketplace pour freelances")
    analyze_investment_decision(saas_result)
    
    time.sleep(1)
    
    # Scénario 2: Fintech
    print("\n💳 SCÉNARIO 2: Fintech")
    print("-" * 40)
    fintech_result = create_startup_endpoint("Plateforme de prêts P2P avec IA")
    analyze_investment_decision(fintech_result)
    
    time.sleep(1)
    
    # Scénario 3: IA/ML
    print("\n🤖 SCÉNARIO 3: Intelligence Artificielle")
    print("-" * 40)
    ai_result = create_startup_endpoint("Assistant IA pour la gestion de projet")
    analyze_investment_decision(ai_result)
    
    # Récupération des détails d'une startup
    if saas_result.get("project_id"):
        print("\n🔍 RÉCUPÉRATION DÉTAILS STARTUP")
        print("-" * 40)
        details = get_startup_endpoint(saas_result["project_id"])
        print(f"📋 Statut: {details.get('status', 'N/A')}")
        print(f"📅 Créée le: {details.get('created_at', 'N/A')}")
    
    print("\n" + "="*60)
    print("🎉 DÉMONSTRATION TERMINÉE")
    print("="*60)

def main():
    """Fonction principale de démonstration"""
    
    try:
        # Lancement des scénarios
        run_demo_scenarios()
        
    except KeyboardInterrupt:
        print("\n\n⏹️  Démonstration interrompue par l'utilisateur")
    except Exception as e:
        print(f"\n❌ Erreur lors de la démonstration: {str(e)}")

if __name__ == "__main__":
    main()