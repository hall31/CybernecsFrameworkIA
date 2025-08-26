# Configuration des agents et épics pour l'orchestration
# Ce fichier centralise la configuration de tous les agents et épics du système

AGENTS_CONFIG = {
    "CEOAgent": True,
    "CTOAgent": True,
    "DevBackendAgent": True,
    "DevFrontendAgent": True,
    "MarketingAgent": True,
    "FinanceAgent": False,
    "LegalAgent": False,
    "GrowthAgent": False
}

EPICS = {
    "epic1": ["CEOAgent"],
    "epic2": ["CTOAgent"],
    "epic3": ["DevBackendAgent", "DevFrontendAgent"],
    "epic4": ["MarketingAgent"],
    "epic7": ["FinanceAgent", "LegalAgent", "GrowthAgent"]
}

# Statut des agents basé sur leur configuration
AGENT_STATUS = {name: "active" if enabled else "disabled" for name, enabled in AGENTS_CONFIG.items()}

# Statut des épics (tous en idle par défaut)
EPIC_STATUS = {eid: "idle" for eid in EPICS.keys()}

# Configuration des ports et URLs
ADMIN_API_PORT = 8000
ADMIN_API_HOST = "0.0.0.0"

# Configuration CORS pour le frontend React
CORS_ORIGINS = [
    "http://localhost:3000",  # React dev server
    "http://localhost:5173",  # Vite dev server
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173",
    "*"  # En développement, autoriser toutes les origines
]