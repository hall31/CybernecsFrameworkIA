#!/usr/bin/env python3
"""
Main Orchestrator - Intégration des agents DAO avec le système existant
"""

import logging
from typing import Dict, Any
from agents.dao_agent import DAOOrchestrator

# Configuration logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class StartupOrchestrator:
    """Orchestrateur principal pour la création de startups avec DAO"""
    
    def __init__(self):
        self.dao_orchestrator = DAOOrchestrator()
        # Autres agents existants seraient initialisés ici
        
    def create_startup_with_dao(self, idea: str, project_id: str = None) -> Dict[str, Any]:
        """Crée une startup complète avec tokenisation, DAO et trésorerie"""
        try:
            logger.info(f"🚀 StartupOrchestrator: Création startup avec DAO pour '{idea}'")
            
            # Génération d'un ID de projet si non fourni
            if not project_id:
                project_id = self._generate_project_id(idea)
            
            # Simulation de la valorisation (en production, utiliser InvestorAgent)
            valuation = self._estimate_valuation(idea)
            
            # Création de la DAO complète
            dao_result = self.dao_orchestrator.create_complete_dao(project_id, valuation)
            
            # Résultat final
            result = {
                "project_id": project_id,
                "idea": idea,
                "valuation": valuation,
                "status": "startup_created",
                "dao": dao_result,
                "timestamp": self._get_timestamp()
            }
            
            logger.info(f"🎉 Startup avec DAO créée: {project_id}")
            return result
            
        except Exception as e:
            logger.error(f"❌ Erreur création startup: {str(e)}")
            raise
    
    def _generate_project_id(self, idea: str) -> str:
        """Génère un ID de projet unique basé sur l'idée"""
        import hashlib
        import time
        
        # Hash de l'idée + timestamp
        hash_input = f"{idea}{int(time.time())}"
        hash_object = hashlib.md5(hash_input.encode())
        return hash_object.hexdigest()[:8].upper()
    
    def _estimate_valuation(self, idea: str) -> float:
        """Estime la valorisation de la startup (simulation)"""
        # En production, utiliser InvestorAgent pour une vraie valorisation
        base_valuation = 2_500_000  # 2.5M € de base
        
        # Facteurs de valorisation basés sur le type d'idée
        multipliers = {
            "saas": 1.5,
            "marketplace": 2.0,
            "ai": 3.0,
            "fintech": 2.5,
            "healthtech": 2.8
        }
        
        idea_lower = idea.lower()
        multiplier = 1.0
        
        for key, value in multipliers.items():
            if key in idea_lower:
                multiplier = value
                break
        
        return base_valuation * multiplier
    
    def _get_timestamp(self) -> str:
        """Retourne le timestamp actuel"""
        from datetime import datetime
        return datetime.now().isoformat()


# API Endpoint Simulation
def create_startup_endpoint(idea: str) -> Dict[str, Any]:
    """Endpoint API pour créer une startup avec DAO"""
    try:
        orchestrator = StartupOrchestrator()
        result = orchestrator.create_startup_with_dao(idea)
        
        # Format de réponse pour l'API
        api_response = {
            "success": True,
            "data": result,
            "message": "Startup créée avec succès"
        }
        
        return api_response
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": "Erreur lors de la création de la startup"
        }


if __name__ == "__main__":
    # Test de l'orchestrateur
    print("🧪 Test de l'orchestrateur DAO...")
    
    # Test avec une idée
    test_idea = "SaaS marketplace pour freelances"
    result = create_startup_endpoint(test_idea)
    
    if result["success"]:
        print("✅ Test réussi!")
        print(f"📊 Résultat: {result['data']['project_id']}")
        print(f"💰 Valorisation: {result['data']['valuation']:,.0f} €")
        print(f"🪙 Token: {result['data']['dao']['token']['token_symbol']}")
        print(f"🏛️ DAO: {result['data']['dao']['dao']['dao_address']}")
        print(f"💰 Treasury: {result['data']['dao']['treasury']['treasury_address']}")
    else:
        print(f"❌ Test échoué: {result['error']}")