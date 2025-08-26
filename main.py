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
    allow_origins=["*"],  # En production, restreindre aux domaines autorisés
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
        "timestamp": "2024-01-15T10:30:00Z",
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