import logging
import json
from typing import Dict, Any
from core_engine.agents.finance_agent import FinanceAgent
from core_engine.agents.legal_agent import LegalAgent
from core_engine.agents.growth_agent import GrowthAgent

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

class StartupOrchestrator:
    """Orchestrateur principal qui coordonne tous les agents pour créer une startup complète"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.finance_agent = FinanceAgent()
        self.legal_agent = LegalAgent()
        self.growth_agent = GrowthAgent()
    
    def create_startup(self, idea: str) -> Dict[str, Any]:
        """
        Crée une startup complète en exécutant tous les agents
        
        Args:
            idea (str): Description de l'idée de startup
            
        Returns:
            Dict contenant tous les éléments de la startup
        """
        try:
            self.logger.info(f"Démarrage de la création de startup pour l'idée: {idea}")
            
            # Exécution de tous les agents
            self.logger.info("Exécution du FinanceAgent...")
            finance = self.finance_agent.run(idea)
            
            self.logger.info("Exécution du LegalAgent...")
            legal = self.legal_agent.run(idea)
            
            self.logger.info("Exécution du GrowthAgent...")
            growth = self.growth_agent.run(idea)
            
            # Génération des éléments de base (simulation des agents existants)
            roadmap = self._generate_roadmap(idea)
            stack = self._generate_stack(idea)
            backend = self._generate_backend(idea)
            frontend = self._generate_frontend(idea)
            marketing = self._generate_marketing(idea)
            
            # Construction de la réponse complète
            result = {
                "idea": idea,
                "roadmap": roadmap,
                "stack": stack,
                "backend": backend,
                "frontend": frontend,
                "marketing": marketing,
                "finance": finance,
                "legal": self._extract_legal_files(legal),
                "growth": growth,
                "generated_at": "2024-08-19",
                "status": "success"
            }
            
            self.logger.info("Création de startup terminée avec succès")
            return result
            
        except Exception as e:
            self.logger.error(f"Erreur lors de la création de startup: {str(e)}")
            return {
                "error": f"Erreur lors de la création de startup: {str(e)}",
                "status": "error"
            }
    
    def _extract_legal_files(self, legal_result: Dict[str, Any]):
        """Retourne la liste des fichiers légaux si la génération a réussi."""
        try:
            if isinstance(legal_result, dict) and legal_result.get("status") == "success":
                return legal_result.get("generated_files", [])
            return []
        except Exception:
            return []
    
    def _generate_roadmap(self, idea: str) -> Dict[str, Any]:
        """Génère une roadmap de développement (simulation)"""
        return {
            "phase1": {
                "duration": "3 mois",
                "objectives": ["MVP", "Premiers utilisateurs", "Validation marché"],
                "deliverables": ["Prototype fonctionnel", "Landing page", "Base utilisateurs"]
            },
            "phase2": {
                "duration": "6 mois",
                "objectives": ["Produit complet", "Croissance utilisateurs", "Monétisation"],
                "deliverables": ["Application complète", "Système de paiement", "100 utilisateurs payants"]
            },
            "phase3": {
                "duration": "12 mois",
                "objectives": ["Scaling", "Expansion fonctionnalités", "International"],
                "deliverables": ["Version enterprise", "API publique", "Présence internationale"]
            }
        }
    
    def _generate_stack(self, idea: str) -> Dict[str, Any]:
        """Génère la stack technique (simulation)"""
        return {
            "frontend": ["React", "TypeScript", "Tailwind CSS"],
            "backend": ["Node.js", "Express", "PostgreSQL"],
            "infrastructure": ["AWS", "Docker", "Kubernetes"],
            "monitoring": ["Sentry", "DataDog", "Grafana"]
        }
    
    def _generate_backend(self, idea: str) -> Dict[str, Any]:
        """Génère l'architecture backend (simulation)"""
        return {
            "architecture": "Microservices",
            "database": "PostgreSQL + Redis",
            "api": "REST + GraphQL",
            "security": ["JWT", "OAuth2", "Rate limiting"],
            "deployment": "CI/CD avec GitHub Actions"
        }
    
    def _generate_frontend(self, idea: str) -> Dict[str, Any]:
        """Génère l'architecture frontend (simulation)"""
        return {
            "framework": "React 18",
            "state_management": "Redux Toolkit",
            "styling": "Tailwind CSS + Headless UI",
            "testing": "Jest + React Testing Library",
            "build_tool": "Vite"
        }
    
    def _generate_marketing(self, idea: str) -> Dict[str, Any]:
        """Génère la stratégie marketing (simulation)"""
        return {
            "positioning": f"Solution innovante pour {idea}",
            "target_audience": "Professionnels et entreprises",
            "channels": ["Content marketing", "SEO", "Social media", "Email"],
            "budget": "5000€/mois",
            "goals": ["Brand awareness", "Lead generation", "Conversion"]
        }

def main():
    """Fonction principale pour tester l'orchestrateur"""
    orchestrator = StartupOrchestrator()
    
    # Test avec une idée
    idea = "SaaS marketplace pour freelances"
    result = orchestrator.create_startup(idea)
    
    # Affichage du résultat
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()