#!/usr/bin/env python3
"""
Démonstration de l'API de l'orchestrateur StartupAI
"""

import json
import requests
from typing import Dict, Any
import time

class StartupAPIDemo:
    """
    Classe de démonstration pour tester l'API StartupAI
    """
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.session = requests.Session()
    
    def create_startup(self, idea: str) -> Dict[str, Any]:
        """
        Crée une startup via l'API
        
        Args:
            idea: Idée de startup
            
        Returns:
            Résultat de la création
        """
        try:
            print(f"🚀 Création de startup: {idea}")
            
            # En production, ceci serait un vrai appel HTTP
            # response = self.session.post(f"{self.base_url}/api/startup/create", 
            #                             json={"idea": idea})
            # return response.json()
            
            # Simulation pour la démo
            from main import create_startup_endpoint
            result = create_startup_endpoint(idea)
            
            print("✅ Startup créée avec succès!")
            return result
            
        except Exception as e:
            print(f"❌ Erreur création startup: {str(e)}")
            return {"error": str(e)}
    
    def get_startup_details(self, project_id: str) -> Dict[str, Any]:
        """
        Récupère les détails d'une startup
        
        Args:
            project_id: ID du projet
            
        Returns:
            Détails de la startup
        """
        try:
            print(f"📊 Récupération détails startup: {project_id}")
            
            # En production, ceci serait un vrai appel HTTP
            # response = self.session.get(f"{self.base_url}/api/startup/{project_id}")
            # return response.json()
            
            # Simulation pour la démo
            from main import get_startup_endpoint
            result = get_startup_endpoint(project_id)
            
            print("✅ Détails récupérés avec succès!")
            return result
            
        except Exception as e:
            print(f"❌ Erreur récupération détails: {str(e)}")
            return {"error": str(e)}
    
    def analyze_investment_decision(self, startup_data: Dict[str, Any]) -> None:
        """
        Analyse et affiche la décision d'investissement
        
        Args:
            startup_data: Données de la startup
        """
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
    
    def run_demo_scenarios(self) -> None:
        """
        Lance plusieurs scénarios de démonstration
        """
        print("🎬 DÉMONSTRATION STARTUP AI - INVESTISSEUR IA")
        print("="*60)
        
        # Scénario 1: SaaS Marketplace
        print("\n📱 SCÉNARIO 1: SaaS Marketplace")
        print("-" * 40)
        saas_result = self.create_startup("SaaS marketplace pour freelances")
        self.analyze_investment_decision(saas_result)
        
        time.sleep(2)
        
        # Scénario 2: Fintech
        print("\n💳 SCÉNARIO 2: Fintech")
        print("-" * 40)
        fintech_result = self.create_startup("Plateforme de prêts P2P avec IA")
        self.analyze_investment_decision(fintech_result)
        
        time.sleep(2)
        
        # Scénario 3: IA/ML
        print("\n🤖 SCÉNARIO 3: Intelligence Artificielle")
        print("-" * 40)
        ai_result = self.create_startup("Assistant IA pour la gestion de projet")
        self.analyze_investment_decision(ai_result)
        
        # Récupération des détails d'une startup
        if saas_result.get("project_id"):
            print("\n🔍 RÉCUPÉRATION DÉTAILS STARTUP")
            print("-" * 40)
            details = self.get_startup_details(saas_result["project_id"])
            print(f"📋 Statut: {details.get('status', 'N/A')}")
            print(f"📅 Créée le: {details.get('created_at', 'N/A')}")
        
        print("\n" + "="*60)
        print("🎉 DÉMONSTRATION TERMINÉE")
        print("="*60)

def main():
    """Fonction principale de démonstration"""
    
    # Création de la démo
    demo = StartupAPIDemo()
    
    try:
        # Lancement des scénarios
        demo.run_demo_scenarios()
        
    except KeyboardInterrupt:
        print("\n\n⏹️  Démonstration interrompue par l'utilisateur")
    except Exception as e:
        print(f"\n❌ Erreur lors de la démonstration: {str(e)}")

if __name__ == "__main__":
    main()