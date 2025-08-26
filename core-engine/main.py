#!/usr/bin/env python3
"""
Orchestrateur principal pour l'Epic10 - IA Autonome
Coordonne les 3 agents: ProductFeedbackAgent, AutoIterationAgent, BusinessOptimizerAgent
"""

import json
import logging
import asyncio
from typing import Dict, List, Any, Optional
from datetime import datetime
import os

# Import des agents
from agents.product_feedback_agent import ProductFeedbackAgent
from agents.auto_iteration_agent import AutoIterationAgent
from agents.business_optimizer_agent import BusinessOptimizerAgent

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class Epic10Orchestrator:
    """
    Orchestrateur principal pour l'Epic10 - IA Autonome
    """
    
    def __init__(self, openai_api_key: str = None):
        self.openai_api_key = openai_api_key or os.getenv("OPENAI_API_KEY")
        
        # Initialisation des agents
        self.product_feedback_agent = ProductFeedbackAgent(self.openai_api_key)
        self.auto_iteration_agent = AutoIterationAgent(self.openai_api_key)
        self.business_optimizer_agent = BusinessOptimizerAgent(self.openai_api_key)
        
        logger.info("Epic10Orchestrator initialisé avec succès")
    
    def log_event(self, event_type: str, message: str, data: Dict[str, Any] = None):
        """Log un événement avec timestamp et données"""
        timestamp = datetime.now().isoformat()
        log_entry = {
            "timestamp": timestamp,
            "event_type": event_type,
            "message": message,
            "data": data or {}
        }
        
        logger.info(f"[{timestamp}] {event_type}: {message}")
        
        # TODO: Sauvegarder dans base de données ou système de monitoring
        return log_entry
    
    async def run_product_feedback_analysis(self, project_id: str) -> Dict[str, Any]:
        """
        Exécute l'analyse du feedback produit
        """
        try:
            logger.info(f"Démarrage analyse feedback pour projet {project_id}")
            
            # Exécution de l'agent
            feedback_result = self.product_feedback_agent.run(project_id)
            
            if feedback_result.get("status") == "failed":
                raise Exception(f"Échec analyse feedback: {feedback_result.get('error')}")
            
            self.log_event(
                "ProductFeedbackAgent", 
                "Analyse feedback terminée avec succès",
                {"project_id": project_id, "issues_count": len(feedback_result.get("issues", []))}
            )
            
            return feedback_result
            
        except Exception as e:
            error_msg = f"Erreur dans analyse feedback: {str(e)}"
            logger.error(error_msg)
            self.log_event("ProductFeedbackAgent", f"ERREUR: {error_msg}")
            
            return {
                "error": error_msg,
                "timestamp": datetime.now().isoformat(),
                "status": "failed"
            }
    
    async def run_auto_iteration(self, project_id: str, feedback: Dict[str, Any]) -> Dict[str, Any]:
        """
        Exécute l'itération automatique basée sur le feedback
        """
        try:
            logger.info(f"Démarrage itération automatique pour projet {project_id}")
            
            # Exécution de l'agent
            iteration_result = self.auto_iteration_agent.run(project_id, feedback)
            
            if iteration_result.get("status") == "failed":
                raise Exception(f"Échec itération automatique: {iteration_result.get('error')}")
            
            self.log_event(
                "AutoIterationAgent",
                "Itération automatique terminée avec succès",
                {
                    "project_id": project_id,
                    "user_stories_count": len(iteration_result.get("user_stories", [])),
                    "sprints_count": len(iteration_result.get("roadmap", {}).get("sprints", []))
                }
            )
            
            return iteration_result
            
        except Exception as e:
            error_msg = f"Erreur dans itération automatique: {str(e)}"
            logger.error(error_msg)
            self.log_event("AutoIterationAgent", f"ERREUR: {error_msg}")
            
            return {
                "error": error_msg,
                "timestamp": datetime.now().isoformat(),
                "status": "failed"
            }
    
    async def run_business_optimization(self, project_id: str, finance: Dict[str, Any] = None, growth: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Exécute l'optimisation business
        """
        try:
            logger.info(f"Démarrage optimisation business pour projet {project_id}")
            
            # Exécution de l'agent
            optimization_result = self.business_optimizer_agent.run(project_id, finance, growth)
            
            if optimization_result.get("status") == "failed":
                raise Exception(f"Échec optimisation business: {optimization_result.get('error')}")
            
            self.log_event(
                "BusinessOptimizerAgent",
                "Optimisation business terminée avec succès",
                {
                    "project_id": project_id,
                    "pricing_changes_count": len(optimization_result.get("pricing_changes", [])),
                    "budget_recommendations_count": len(optimization_result.get("ads_budget_shift", []))
                }
            )
            
            return optimization_result
            
        except Exception as e:
            error_msg = f"Erreur dans optimisation business: {str(e)}"
            logger.error(error_msg)
            self.log_event("BusinessOptimizerAgent", f"ERREUR: {error_msg}")
            
            return {
                "error": error_msg,
                "timestamp": datetime.now().isoformat(),
                "status": "failed"
            }
    
    async def run_complete_epic10(self, project_id: str, idea: str, finance: Dict[str, Any] = None, growth: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Exécute l'Epic10 complet avec les 3 agents
        """
        try:
            start_time = datetime.now()
            logger.info(f"Démarrage Epic10 complet pour projet {project_id}: {idea}")
            
            self.log_event("Epic10Orchestrator", f"Démarrage Epic10 pour: {idea}", {"project_id": project_id, "idea": idea})
            
            # 1. Analyse du feedback produit
            logger.info("Étape 1/3: Analyse du feedback produit")
            feedback_result = await self.run_product_feedback_analysis(project_id)
            
            if feedback_result.get("status") == "failed":
                raise Exception("Échec de l'analyse du feedback")
            
            # 2. Itération automatique
            logger.info("Étape 2/3: Itération automatique")
            iteration_result = await self.run_auto_iteration(project_id, feedback_result)
            
            if iteration_result.get("status") == "failed":
                raise Exception("Échec de l'itération automatique")
            
            # 3. Optimisation business
            logger.info("Étape 3/3: Optimisation business")
            optimization_result = await self.run_business_optimization(project_id, finance, growth)
            
            if optimization_result.get("status") == "failed":
                raise Exception("Échec de l'optimisation business")
            
            # 4. Résultat final
            end_time = datetime.now()
            execution_time = (end_time - start_time).total_seconds()
            
            epic10_result = {
                "project_id": project_id,
                "idea": idea,
                "timestamp": datetime.now().isoformat(),
                "execution_time_seconds": execution_time,
                "status": "completed",
                "epic10_version": "1.0.0",
                "agents_executed": [
                    "ProductFeedbackAgent",
                    "AutoIterationAgent", 
                    "BusinessOptimizerAgent"
                ],
                "results": {
                    "feedback": feedback_result,
                    "iteration": iteration_result,
                    "optimizer": optimization_result
                },
                "summary": {
                    "total_issues_identified": len(feedback_result.get("issues", [])),
                    "total_user_stories_generated": len(iteration_result.get("user_stories", [])),
                    "total_optimizations_proposed": len(optimization_result.get("pricing_changes", [])) + len(optimization_result.get("ads_budget_shift", [])),
                    "estimated_roi_improvement": optimization_result.get("roi_projection", "N/A")
                }
            }
            
            self.log_event(
                "Epic10Orchestrator",
                "Epic10 terminé avec succès",
                {
                    "project_id": project_id,
                    "execution_time": execution_time,
                    "total_improvements": epic10_result["summary"]["total_user_stories_generated"]
                }
            )
            
            logger.info(f"Epic10 terminé avec succès en {execution_time:.2f} secondes")
            return epic10_result
            
        except Exception as e:
            error_msg = f"Erreur dans Epic10 complet: {str(e)}"
            logger.error(error_msg)
            self.log_event("Epic10Orchestrator", f"ERREUR: {error_msg}")
            
            return {
                "error": error_msg,
                "timestamp": datetime.now().isoformat(),
                "status": "failed",
                "project_id": project_id,
                "idea": idea
            }
    
    def create_startup_with_epic10(self, idea: str, project_id: str = None) -> Dict[str, Any]:
        """
        Crée une startup complète avec l'Epic10
        """
        if not project_id:
            project_id = f"startup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        try:
            logger.info(f"Création startup avec Epic10: {idea}")
            
            # Simulation des données financières et de croissance
            mock_finance = {
                "revenue": {"mrr": 5000, "ltv": 150, "cac": 40, "churn_rate": 0.06},
                "pricing": {"starter": {"price": 25}, "pro": {"price": 69}}
            }
            
            mock_growth = {
                "advertising": {
                    "google_ads": {"budget": 2000, "roas": 2.5},
                    "linkedin_ads": {"budget": 1000, "roas": 3.0}
                }
            }
            
            # Exécution synchrone pour la compatibilité
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            
            try:
                epic10_result = loop.run_until_complete(
                    self.run_complete_epic10(project_id, idea, mock_finance, mock_growth)
                )
            finally:
                loop.close()
            
            # Résultat final pour /create-startup
            startup_result = {
                "project_id": project_id,
                "idea": idea,
                "status": "startup_created_with_epic10",
                "timestamp": datetime.now().isoformat(),
                "epic10_results": epic10_result,
                "next_steps": [
                    "Analyser le feedback utilisateur",
                    "Implémenter les améliorations prioritaires",
                    "Appliquer les optimisations business",
                    "Monitorer les métriques de performance"
                ]
            }
            
            return startup_result
            
        except Exception as e:
            error_msg = f"Erreur création startup avec Epic10: {str(e)}"
            logger.error(error_msg)
            
            return {
                "error": error_msg,
                "timestamp": datetime.now().isoformat(),
                "status": "failed",
                "project_id": project_id,
                "idea": idea
            }

# API endpoints pour l'intégration
def create_startup_endpoint(idea: str, project_id: str = None) -> Dict[str, Any]:
    """
    Endpoint principal pour créer une startup avec Epic10
    """
    orchestrator = Epic10Orchestrator()
    return orchestrator.create_startup_with_epic10(idea, project_id)

# Test et démonstration
if __name__ == "__main__":
    print("🚀 Epic10 - IA Autonome pour Mon ShipFast")
    print("=" * 50)
    
    # Test de l'orchestrateur
    orchestrator = Epic10Orchestrator()
    
    # Création d'une startup test
    test_idea = "SaaS marketplace pour freelances"
    result = orchestrator.create_startup_with_epic10(test_idea)
    
    if result.get("status") == "startup_created_with_epic10":
        print(f"✅ Startup créée avec succès: {test_idea}")
        print(f"📊 Résultats Epic10:")
        print(f"   - Issues identifiées: {result['epic10_results']['summary']['total_issues_identified']}")
        print(f"   - User stories générées: {result['epic10_results']['summary']['total_user_stories_generated']}")
        print(f"   - Optimisations proposées: {result['epic10_results']['summary']['total_optimizations_proposed']}")
        print(f"   - ROI attendu: {result['epic10_results']['summary']['estimated_roi_improvement']}")
    else:
        print(f"❌ Erreur: {result.get('error')}")
    
    print("\n🎯 Epic10 prêt pour l'intégration dans /create-startup!")