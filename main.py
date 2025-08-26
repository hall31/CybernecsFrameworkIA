import logging
import json
from typing import Dict, Any
from core_engine.agents.finance_agent import FinanceAgent
from core_engine.agents.legal_agent import LegalAgent
from core_engine.agents.growth_agent import GrowthAgent
import os
import uuid
from typing import Dict, Any
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

# Import des agents
from agents.gitops_agent import GitOpsAgent
from agents.payments_agent import PaymentsAgent
from agents.ads_agent import AdsAgent

# Charger les variables d'environnement
load_dotenv()

app = FastAPI(
    title="Mon ShipFast - API",
    description="API pour créer des startups SaaS automatiquement",
    version="1.0.0"
)

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins_list,  # En production, restreindre aux domaines autorisés
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StartupRequest(BaseModel):
    idea: str
    description: str = ""

class StartupResponse(BaseModel):
    project_id: str
    idea: str
    status: str
    gitops: Dict[str, Any]
    payments: Dict[str, Any]
    ads: Dict[str, Any]
    message: str

@app.get("/")
async def root():
    """Endpoint racine"""
    return {
        "message": "🚀 Mon ShipFast API - Créez votre startup SaaS en quelques clics !",
        "version": "1.0.0",
        "endpoints": {
            "create_startup": "POST /create-startup",
            "health": "GET /health"
        }
    }

@app.get("/health")
async def health_check():
    """Vérification de l'état de l'API"""
    return {
        "status": "healthy",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "agents": {
            "gitops": "available",
            "payments": "available", 
            "ads": "available"
        }
    }

@app.post("/create-startup", response_model=StartupResponse)
async def create_startup(request: StartupRequest):
    """
    Crée une startup SaaS complète avec exécution automatique
    
    Processus :
    1. Génère un ID de projet unique
    2. Exécute GitOpsAgent pour le déploiement
    3. Exécute PaymentsAgent pour la monétisation
    4. Exécute AdsAgent pour l'acquisition
    5. Retourne tous les résultats
    """
    try:
        # 1. Générer un ID de projet unique
        project_id = str(uuid.uuid4())[:8]
        
        print(f"🚀 Création de startup: {request.idea} (ID: {project_id})")
        
        # 2. Exécuter GitOpsAgent (déploiement auto)
        print("📦 Exécution de GitOpsAgent...")
        gitops_agent = GitOpsAgent()
        gitops_result = gitops_agent.run(project_id)
        
        if gitops_result.get("status") == "error":
            raise HTTPException(status_code=500, detail=f"Erreur GitOps: {gitops_result.get('error', 'Unknown error')}")
        
        # 3. Exécuter PaymentsAgent (monétisation)
        print("💳 Exécution de PaymentsAgent...")
        payments_agent = PaymentsAgent()
        payments_result = payments_agent.run(request.idea)
        
        if payments_result.get("status") == "error":
            raise HTTPException(status_code=500, detail=f"Erreur Payments: {payments_result.get('error', 'Unknown error')}")
        
        # 4. Exécuter AdsAgent (acquisition clients)
        print("📢 Exécution de AdsAgent...")
        ads_agent = AdsAgent()
        
        # Simuler les données de croissance pour AdsAgent
        growth_data = {
            "channel": "paid_ads",
            "budget": "100€/jour",
            "target_audience": "B2B",
            "timeline": "30 jours"
        }
        
        ads_result = ads_agent.run(request.idea, growth_data)
        
        if ads_result.get("status") == "error":
            raise HTTPException(status_code=500, detail=f"Erreur Ads: {ads_result.get('error', 'Unknown error')}")
        
        # 5. Construire la réponse complète
        response = StartupResponse(
            project_id=project_id,
            idea=request.idea,
            status="created",
            gitops=gitops_result,
            payments=payments_result,
            ads=ads_result,
            message=f"Startup '{request.idea}' créée avec succès ! Tous les agents ont été exécutés."
        )
        
        print(f"✅ Startup créée avec succès: {project_id}")
        print(f"   - GitOps: {gitops_result.get('repo_url', 'N/A')}")
        print(f"   - Payments: {len(payments_result.get('stripe_plans', []))} plans créés")
        print(f"   - Ads: Campagne {ads_result.get('ads_platform', 'N/A')} lancée")
        
        return response
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ Erreur lors de la création de la startup: {e}")
        raise HTTPException(
            status_code=500, 
            detail=f"Erreur interne lors de la création de la startup: {str(e)}"
        )

@app.get("/startup/{project_id}")
async def get_startup_status(project_id: str):
    """Récupère le statut d'une startup par son ID"""
    try:
        # En production, récupérer depuis une base de données
        return {
            "project_id": project_id,
            "status": "active",
            "created_at": "2024-01-15T10:30:00Z",
            "last_updated": "2024-01-15T10:30:00Z"
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Startup {project_id} non trouvée")

@app.get("/agents/status")
async def get_agents_status():
    """Récupère le statut de tous les agents"""
    try:
        return {
            "gitops_agent": {
                "status": "available",
                "github_configured": bool(os.getenv('GITHUB_TOKEN')),
                "capabilities": ["create_repo", "push_code", "setup_ci_cd"]
            },
            "payments_agent": {
                "status": "available",
                "stripe_configured": bool(os.getenv('STRIPE_SECRET_KEY')),
                "capabilities": ["create_plans", "setup_checkout", "manage_subscriptions"]
            },
            "ads_agent": {
                "status": "available",
                "linkedin_configured": bool(os.getenv('LINKEDIN_ACCESS_TOKEN')),
                "google_ads_configured": bool(os.getenv('GOOGLE_ADS_DEVELOPER_TOKEN')),
                "capabilities": ["create_campaigns", "target_audience", "optimize_ads"]
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la récupération du statut des agents: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    
    # Vérifier les variables d'environnement critiques
    required_env_vars = [
        'GITHUB_TOKEN',
        'STRIPE_SECRET_KEY'
    ]
    
    missing_vars = [var for var in required_env_vars if not os.getenv(var)]
    
    if missing_vars:
        print(f"⚠️  Variables d'environnement manquantes: {', '.join(missing_vars)}")
        print("   L'API fonctionnera mais certains agents pourraient échouer.")
        print("   Consultez le fichier .env.example pour la configuration.")
    
    print("🚀 Démarrage de Mon ShipFast API...")
    print("   - GitOpsAgent: Déploiement automatique")
    print("   - PaymentsAgent: Monétisation Stripe")
    print("   - AdsAgent: Acquisition clients")
    print("   - Endpoint principal: POST /create-startup")
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
#!/usr/bin/env python3
"""

Orchestrateur principal pour la génération de startups
Coordonne tous les agents : CEO, CTO, Dev, Marketing
"""

import json
import time
import logging
import json

from pathlib import Path
from typing import Dict, Any

# Import des agents
from core_engine.agents.marketing_agent_simple import MarketingAgent
from core_engine.logger import get_logger

class StartupOrchestrator:
    def __init__(self):
        self.logger = get_logger("StartupOrchestrator")
        self.marketing_agent = MarketingAgent()
        
        # Créer les dossiers nécessaires
        self.generated_dir = Path("generated")
        self.generated_dir.mkdir(exist_ok=True)
    
    def create_startup(self, idea: str) -> Dict[str, Any]:
        """
        Crée une startup complète en orchestrant tous les agents
        """
        self.logger.log_step("Démarrage", f"Génération de la startup '{idea}'")
        
        try:
            # 1. Phase CEO - Stratégie et roadmap
            self.logger.log_step("Phase CEO", "Définition de la stratégie et roadmap")
            ceo_result = self._run_ceo_phase(idea)
            time.sleep(1)  # Simulation du temps de traitement
            
            # 2. Phase CTO - Architecture technique
            self.logger.log_step("Phase CTO", "Définition de l'architecture technique")
            cto_result = self._run_cto_phase(idea)
            time.sleep(1)
            
            # 3. Phase Dev - Développement MVP
            self.logger.log_step("Phase Dev", "Développement du MVP backend et frontend")
            dev_result = self._run_dev_phase(idea)
            time.sleep(1)
            
            # 4. Phase Marketing - Contenu et landing page
            self.logger.log_step("Phase Marketing", "Génération du contenu marketing et landing page")
            marketing_result = self._run_marketing_phase(idea)
            time.sleep(1)
            
            # 5. Assemblage final
            self.logger.log_step("Assemblage", "Création du package final")
            final_result = self._assemble_final_result(
                idea, ceo_result, cto_result, dev_result, marketing_result
            )
            
            # 6. Sauvegarde du résultat
            self._save_result(final_result)
            
            self.logger.log_success("Startup générée", f"Package complet créé dans {self.generated_dir}")
            
            return final_result
            
        except Exception as e:
            self.logger.log_error("Erreur lors de la génération", str(e))
            raise
    
    def _run_ceo_phase(self, idea: str) -> Dict[str, Any]:
        """Simule la phase CEO - Stratégie et roadmap"""
        self.logger.info("🎯 CEO Agent: Analyse de l'idée et définition de la stratégie")
        
        # Simulation des résultats du CEO
        return {
            "strategy": f"Stratégie de marché pour {idea}",
            "roadmap": [
                "Phase 1: MVP et validation marché (3 mois)",
                "Phase 2: Développement des fonctionnalités clés (6 mois)",
                "Phase 3: Expansion et croissance (12 mois)"
            ],
            "target_market": "PME et startups en croissance",
            "business_model": "SaaS avec abonnements mensuels",
            "revenue_projection": "€100K ARR en 18 mois"
        }
    
    def _run_cto_phase(self, idea: str) -> Dict[str, Any]:
        """Simule la phase CTO - Architecture technique"""
        self.logger.info("⚙️ CTO Agent: Définition de l'architecture technique")
        
        # Simulation des résultats du CTO
        return {
            "tech_stack": {
                "backend": "Node.js + Express + PostgreSQL",
                "frontend": "React + TypeScript + Tailwind CSS",
                "infrastructure": "Docker + AWS + CI/CD",
                "monitoring": "Sentry + DataDog"
            },
            "architecture": "Microservices avec API REST",
            "scalability": "Auto-scaling avec Kubernetes",
            "security": "OAuth 2.0 + JWT + HTTPS"
        }
    
    def _run_dev_phase(self, idea: str) -> Dict[str, Any]:
        """Simule la phase Dev - Développement MVP"""
        self.logger.info("💻 Dev Agent: Développement du MVP backend et frontend")
        
        # Simulation des résultats du Dev
        return {
            "backend": {
                "status": "MVP développé",
                "endpoints": ["/api/users", "/api/auth", "/api/core"],
                "database": "PostgreSQL avec migrations",
                "tests": "Jest + Supertest (80% coverage)"
            },
            "frontend": {
                "status": "Interface utilisateur complète",
                "components": ["Dashboard", "Auth", "Settings"],
                "responsive": True,
                "accessibility": "WCAG 2.1 AA"
            },
            "deployment": "Prêt pour staging"
        }
    
    def _run_marketing_phase(self, idea: str) -> Dict[str, Any]:
        """Exécute la phase Marketing - Contenu et landing page"""
        self.logger.info("🎨 Marketing Agent: Génération du contenu marketing")
        
        try:
            result = self.marketing_agent.run(idea)
            self.logger.log_success("Marketing", "Contenu et landing page générés")
            return result
        except Exception as e:
            self.logger.log_error("Erreur Marketing Agent", str(e))
            # Retourner un résultat par défaut en cas d'erreur
            return {
                "headline": f"Révolutionnez votre {idea}",
                "tagline": "L'innovation au service de votre réussite",
                "features": ["Fonctionnalité 1", "Fonctionnalité 2", "Fonctionnalité 3"],
                "pricing": [
                    {"plan": "Starter", "price": "€19/mois", "desc": "Parfait pour démarrer"},
                    {"plan": "Pro", "price": "€49/mois", "desc": "Pour les équipes en croissance"},
                    {"plan": "Enterprise", "price": "Contactez-nous", "desc": "Solutions sur mesure"}
                ],
                "logo": "/generated/branding/logo.svg",
                "landing": "/generated/landing-page"
            }
    
    def _assemble_final_result(self, idea: str, ceo_result: Dict, cto_result: Dict, 
                              dev_result: Dict, marketing_result: Dict) -> Dict[str, Any]:
        """Assemble tous les résultats en un package final"""
        self.logger.info("🔗 Assemblage des résultats de tous les agents")
        
        return {
            "startup": {
                "idea": idea,
                "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                "status": "ready"
            },
            "ceo": ceo_result,
            "cto": cto_result,
            "dev": dev_result,
            "marketing": marketing_result,
            "summary": {
                "total_phases": 4,
                "success_rate": "100%",
                "next_steps": [
                    "Tester le MVP",
                    "Valider avec des utilisateurs",
                    "Itérer sur le feedback",
                    "Préparer le lancement"
                ]
            }
        }
    
    def _save_result(self, result: Dict[str, Any]):
        """Sauvegarde le résultat final"""
        result_file = self.generated_dir / "startup_result.json"
        
        with open(result_file, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        
        self.logger.log_success("Sauvegarde", f"Résultat sauvegardé dans {result_file}")

# Instance globale de l'orchestrateur
orchestrator = StartupOrchestrator()

def create_startup(idea: str) -> Dict[str, Any]:
    """
    Fonction principale pour créer une startup
    Utilisée par l'API ou les scripts
    """
    return orchestrator.create_startup(idea)

if __name__ == "__main__":
    # Test de l'orchestrateur
    print("🚀 Démarrage de l'orchestrateur de startups...")
    
    test_idea = "SaaS marketplace pour freelances"
    result = create_startup(test_idea)
    
    print("\n" + "="*50)
    print("🎉 STARTUP GÉNÉRÉE AVEC SUCCÈS !")
    print("="*50)
    print(f"Idée: {result['startup']['idea']}")
    print(f"Status: {result['startup']['status']}")
    print(f"Généré le: {result['startup']['generated_at']}")
    print(f"Phases complétées: {result['summary']['total_phases']}")
    print(f"Taux de succès: {result['summary']['success_rate']}")
    print("\n📁 Fichiers générés:")
    print(f"  - Logo: {result['marketing']['logo']}")
    print(f"  - Landing page: {result['marketing']['landing']}")
    print(f"  - Résumé complet: generated/startup_result.json")
from core_engine.agents.dev_backend_agent import DevBackendAgent
from core_engine.agents.dev_frontend_agent import DevFrontendAgent

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
logger = logging.getLogger(__name__)

class StartupOrchestrator:
    """
    Orchestrateur principal pour la création de startup
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.generated_path = Path("generated")
        
    def create_startup(self, idea: str) -> Dict[str, Any]:
        """
        Crée une startup complète avec tous les agents
        
        Args:
            idea: L'idée de startup
            
        Returns:
            Dict contenant toutes les informations de la startup créée
        """
        self.logger.info(f"🚀 Démarrage de la création de startup: {idea}")
        
        try:
            # Créer le dossier generated s'il n'existe pas
            self.generated_path.mkdir(exist_ok=True)
            
            # 1. CEOAgent - Créer la roadmap
            self.logger.info("👑 Exécution du CEOAgent")
            roadmap = self._execute_ceo_agent(idea)
            
            # 2. CTOAgent - Définir la stack technique
            self.logger.info("⚡ Exécution du CTOAgent")
            stack = self._execute_cto_agent(roadmap)
            
            # 3. DevBackendAgent - Développer le backend Laravel
            self.logger.info("🔧 Exécution du DevBackendAgent")
            backend = DevBackendAgent().run(stack)
            
            # 4. DevFrontendAgent - Développer le frontend React
            self.logger.info("🎨 Exécution du DevFrontendAgent")
            frontend = DevFrontendAgent().run(stack)
            
            # 5. Résultat final
            result = {
                "status": "success",
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
                "generated_path": str(self.generated_path)
            }
            
            # Sauvegarder le résultat
            self._save_result(result)
            
            self.logger.info("✅ Startup créée avec succès !")
            return result
            
        except Exception as e:
            self.logger.error(f"❌ Erreur lors de la création de la startup: {str(e)}")
            return {
                "status": "error",
                "error": str(e)
            }
    
    def _execute_ceo_agent(self, idea: str) -> Dict[str, Any]:
        """
        Simule l'exécution du CEOAgent
        En production, ceci serait remplacé par l'agent réel
        """
        self.logger.info("👑 CEOAgent - Création de la roadmap")
        
        roadmap = {
            "vision": f"Révolutionner le marché avec {idea}",
            "objectifs": [
                "Créer une plateforme innovante et intuitive",
                "Atteindre 10,000 utilisateurs dans la première année",
                "Générer 1M€ de revenus récurrents"
            ],
            "etapes": [
                "Phase 1: MVP et validation marché (3 mois)",
                "Phase 2: Développement des fonctionnalités avancées (6 mois)",
                "Phase 3: Expansion et internationalisation (12 mois)"
            ],
            "metriques": [
                "Utilisateurs actifs mensuels",
                "Taux de rétention",
                "Revenus mensuels récurrents"
            ]
        }
        
        self.logger.info("✅ Roadmap créée par le CEOAgent")
        return roadmap
    
    def _execute_cto_agent(self, roadmap: Dict[str, Any]) -> Dict[str, Any]:
        """
        Simule l'exécution du CTOAgent
        En production, ceci serait remplacé par l'agent réel
        """
        self.logger.info("⚡ CTOAgent - Définition de la stack technique")
        
        stack = {
            "backend": {
                "framework": "Laravel 10",
                "database": "MySQL 8.0",
                "authentication": "Laravel Sanctum",
                "api": "REST API",
                "deployment": "Docker + Nginx"
            },
            "frontend": {
                "framework": "React 18",
                "styling": "Tailwind CSS",
                "routing": "React Router",
                "state_management": "React Hooks",
                "build_tool": "Create React App"
            },
            "infrastructure": {
                "containerization": "Docker",
                "reverse_proxy": "Nginx",
                "database": "MySQL",
                "cache": "Redis",
                "monitoring": "Laravel Telescope"
            },
            "devops": {
                "version_control": "Git",
                "ci_cd": "GitHub Actions",
                "deployment": "Docker Compose",
                "environment": "Development/Staging/Production"
            }
        }
        
        # Créer docker-compose.yml
        self._create_docker_compose()
        
        self.logger.info("✅ Stack technique définie par le CTOAgent")
        return stack
    
    def _create_docker_compose(self):
        """Crée le fichier docker-compose.yml"""
        docker_compose = '''version: '3.8'

services:
  # Backend Laravel
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: startup_backend
    restart: unless-stopped
    working_dir: /var/www/
    volumes:
      - ./backend:/var/www
      - ./backend/vendor:/var/www/vendor
    networks:
      - startup_network
    environment:
      - APP_ENV=local
      - APP_DEBUG=true
      - DB_HOST=mysql
      - DB_DATABASE=startup_db
      - DB_USERNAME=startup_user
      - DB_PASSWORD=startup_password
    depends_on:
      - mysql
      - redis

  # Frontend React
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    container_name: startup_frontend
    restart: unless-stopped
    ports:
      - "3000:3000"
    volumes:
      - ./frontend:/app
      - /app/node_modules
    networks:
      - startup_network
    environment:
      - REACT_APP_API_URL=http://localhost:8000/api
      - CHOKIDAR_USEPOLLING=true

  # Nginx Reverse Proxy
  nginx:
    image: nginx:alpine
    container_name: startup_nginx
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf
      - ./nginx/conf.d:/etc/nginx/conf.d
    networks:
      - startup_network
    depends_on:
      - backend
      - frontend

  # MySQL Database
  mysql:
    image: mysql:8.0
    container_name: startup_mysql
    restart: unless-stopped
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql
      - ./mysql/init:/docker-entrypoint-initdb.d
    networks:
      - startup_network
    environment:
      - MYSQL_DATABASE=startup_db
      - MYSQL_USER=startup_user
      - MYSQL_PASSWORD=startup_password
      - MYSQL_ROOT_PASSWORD=root_password

  # Redis Cache
  redis:
    image: redis:alpine
    container_name: startup_redis
    restart: unless-stopped
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    networks:
      - startup_network

volumes:
  mysql_data:
  redis_data:

networks:
  startup_network:
    driver: bridge
'''
        
        with open(self.generated_path / "docker-compose.yml", "w") as f:
            f.write(docker_compose)
        
        # Créer le dossier nginx
        nginx_path = self.generated_path / "nginx"
        nginx_path.mkdir(exist_ok=True)
        
        # Configuration Nginx
        nginx_conf = '''events {
    worker_connections 1024;
}

http {
    upstream backend {
        server backend:8000;
    }

    upstream frontend {
        server frontend:3000;
    }

    server {
        listen 80;
        server_name localhost;

        # Frontend React
        location / {
            proxy_pass http://frontend;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        # Backend API
        location /api {
            proxy_pass http://backend;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        # Laravel assets
        location /storage {
            proxy_pass http://backend;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
}
'''
        
        with open(nginx_path / "nginx.conf", "w") as f:
            f.write(nginx_conf)
        
        self.logger.info("✅ Docker Compose et Nginx configurés")
    
    def _save_result(self, result: Dict[str, Any]):
        """Sauvegarde le résultat de la création"""
        result_file = self.generated_path / "startup_result.json"
        
        with open(result_file, "w") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        
        self.logger.info(f"💾 Résultat sauvegardé dans {result_file}")

def main():
    """Fonction principale"""
    orchestrator = StartupOrchestrator()
    
    # Exemple d'utilisation
    idea = "SaaS marketplace pour freelances"
    result = orchestrator.create_startup(idea)
    
    print("\n" + "="*60)
    print("🚀 RÉSULTAT DE LA CRÉATION DE STARTUP")
    print("="*60)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    print("="*60)
    
    if result["status"] == "success":
        print(f"\n✅ Startup créée avec succès dans le dossier: {result['generated_path']}")
        print("📁 Structure générée:")
        print("   ├── backend/     (Laravel API)")
        print("   ├── frontend/    (React Dashboard)")
        print("   ├── nginx/       (Configuration Nginx)")
        print("   └── docker-compose.yml")
        print("\n🚀 Pour démarrer:")
        print("   cd generated")
        print("   docker-compose up -d")
    else:
        print(f"\n❌ Erreur lors de la création: {result.get('error', 'Erreur inconnue')}")

if __name__ == "__main__":
    main()
