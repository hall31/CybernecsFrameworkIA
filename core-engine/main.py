import logging
import json
from typing import Dict, Any, Optional
from datetime import datetime
import uuid

# Import des agents
from agents.investor_agent import InvestorAgent

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class StartupOrchestrator:
    """
    Orchestrateur principal pour la création et l'évaluation de startups
    """
    
    def __init__(self):
        self.investor_agent = InvestorAgent()
        self.logger = logging.getLogger(__name__)
    
    def create_startup(self, idea: str, project_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Création complète d'une startup avec évaluation investisseur
        
        Args:
            idea: Idée de startup
            project_id: ID du projet (généré automatiquement si non fourni)
            
        Returns:
            Dict complet avec tous les résultats des agents
        """
        try:
            if not project_id:
                project_id = str(uuid.uuid4())
            
            self.logger.info(f"Début création startup: {idea} (ID: {project_id})")
            
            # Simulation des données des autres agents (en production, ces données viendraient des vrais agents)
            finance_data = self._simulate_finance_agent(idea)
            growth_data = self._simulate_growth_agent(idea)
            optimizer_data = self._simulate_business_optimizer(idea)
            
            # Appel de l'InvestorAgent pour évaluation et décision
            self.logger.info(f"Appel InvestorAgent pour le projet {project_id}")
            investor_result = self.investor_agent.run(
                project_id=project_id,
                finance=finance_data,
                growth=growth_data,
                optimizer=optimizer_data
            )
            
            # Construction du résultat final
            result = {
                "project_id": project_id,
                "idea": idea,
                "created_at": datetime.now().isoformat(),
                "status": "completed",
                "agents": {
                    "finance": finance_data,
                    "growth": growth_data,
                    "optimizer": optimizer_data,
                    "investor": investor_result
                },
                "summary": {
                    "valuation": investor_result.get("valuation", "N/A"),
                    "decision": investor_result.get("decision", "N/A"),
                    "confidence": investor_result.get("confidence_score", 0.0),
                    "next_funding": investor_result.get("next_funding", "N/A")
                }
            }
            
            self.logger.info(f"Startup créée avec succès: {project_id}")
            return result
            
        except Exception as e:
            self.logger.error(f"Erreur création startup: {str(e)}")
            return self._get_error_response(idea, project_id, str(e))
    
    def _simulate_finance_agent(self, idea: str) -> Dict[str, Any]:
        """Simulation des données du FinanceAgent"""
        # En production, ces données viendraient du vrai FinanceAgent
        return {
            "current_revenue": 12000,  # 12k € par mois
            "projected_revenue": 180000,  # 180k € par an
            "stripe_revenue": 15000,  # Données Stripe réelles
            "monthly_costs": 8000,
            "profit_margin": 0.33,
            "cash_flow": 4000
        }
    
    def _simulate_growth_agent(self, idea: str) -> Dict[str, Any]:
        """Simulation des données du GrowthAgent"""
        # En production, ces données viendraient du vrai GrowthAgent
        return {
            "cac": 45,  # Customer Acquisition Cost
            "ltv": 500,  # Lifetime Value
            "ctr": 0.08,  # Click Through Rate
            "conversion_rate": 0.025,  # 2.5%
            "monthly_growth": 0.15,  # 15% par mois
            "user_retention": 0.85
        }
    
    def _simulate_business_optimizer(self, idea: str) -> Dict[str, Any]:
        """Simulation des données du BusinessOptimizerAgent"""
        # En production, ces données viendraient du vrai BusinessOptimizerAgent
        return {
            "churn_rate": 0.03,  # 3% de churn
            "optimization_score": 0.78,
            "recommended_actions": [
                "Augmenter le budget marketing de 20%",
                "Optimiser la page de conversion",
                "Améliorer l'onboarding utilisateur"
            ],
            "predicted_improvement": 0.25  # 25% d'amélioration
        }
    
    def _get_error_response(self, idea: str, project_id: str, error_message: str) -> Dict[str, Any]:
        """Retourne une réponse d'erreur standardisée"""
        return {
            "project_id": project_id,
            "idea": idea,
            "created_at": datetime.now().isoformat(),
            "status": "error",
            "error": error_message,
            "agents": {
                "finance": {},
                "growth": {},
                "optimizer": {},
                "investor": {
                    "valuation": "Erreur",
                    "kpis": {"MRR": "N/A", "CAC": "N/A", "LTV": "N/A", "Churn": "N/A"},
                    "decision": "Erreur d'évaluation",
                    "next_funding": "Non disponible"
                }
            }
        }
    
    def get_startup_details(self, project_id: str) -> Dict[str, Any]:
        """
        Récupère les détails d'une startup existante
        
        Args:
            project_id: ID du projet
            
        Returns:
            Dict avec les détails de la startup
        """
        # En production, cette méthode récupérerait les données depuis une base de données
        self.logger.info(f"Récupération détails startup: {project_id}")
        
        # Simulation d'une startup existante
        return {
            "project_id": project_id,
            "idea": "SaaS marketplace innovant",
            "created_at": datetime.now().isoformat(),
            "status": "active",
            "agents": {
                "finance": self._simulate_finance_agent("SaaS marketplace"),
                "growth": self._simulate_growth_agent("SaaS marketplace"),
                "optimizer": self._simulate_business_optimizer("SaaS marketplace"),
                "investor": {
                    "valuation": "2.5M €",
                    "kpis": {
                        "MRR": "15k €",
                        "CAC": "45 €",
                        "LTV": "500 €",
                        "Churn": "3%"
                    },
                    "decision": "Investir",
                    "next_funding": "100k € en crédits cloud + pub",
                    "confidence_score": 0.85
                }
            }
        }

# Instance globale de l'orchestrateur
orchestrator = StartupOrchestrator()

def create_startup_endpoint(idea: str) -> Dict[str, Any]:
    """
    Endpoint principal pour créer une startup
    
    Args:
        idea: Idée de startup
        
    Returns:
        Résultat complet de la création
    """
    return orchestrator.create_startup(idea)

def get_startup_endpoint(project_id: str) -> Dict[str, Any]:
    """
    Endpoint pour récupérer les détails d'une startup
    
    Args:
        project_id: ID du projet
        
    Returns:
        Détails de la startup
    """
    return orchestrator.get_startup_details(project_id)

if __name__ == "__main__":
    # Test de l'orchestrateur
    test_idea = "SaaS marketplace pour freelances"
    result = create_startup_endpoint(test_idea)
    
    print("=== Résultat de création de startup ===")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    
    # Test de récupération
    if result.get("project_id"):
        details = get_startup_endpoint(result["project_id"])
        print("\n=== Détails de la startup ===")
        print(json.dumps(details, indent=2, ensure_ascii=False))