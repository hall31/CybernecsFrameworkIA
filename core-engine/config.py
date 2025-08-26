"""
Configuration pour l'Epic 11: Investisseur IA
"""

import os
from typing import Dict, Any

class Config:
    """Configuration de l'application"""
    
    # Environnement
    ENV = os.getenv("ENV", "development")
    DEBUG = os.getenv("DEBUG", "true").lower() == "true"
    
    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Paramètres de l'InvestorAgent
    INVESTOR_CONFIG = {
        "vc_multiples": {
            "saas": float(os.getenv("VC_MULTIPLE_SAAS", "8.0")),
            "marketplace": float(os.getenv("VC_MULTIPLE_MARKETPLACE", "6.0")),
            "fintech": float(os.getenv("VC_MULTIPLE_FINTECH", "10.0")),
            "ai": float(os.getenv("VC_MULTIPLE_AI", "12.0")),
            "default": float(os.getenv("VC_MULTIPLE_DEFAULT", "7.0"))
        },
        "investment_thresholds": {
            "mrr_min": float(os.getenv("INVESTMENT_MRR_MIN", "5000")),
            "cac_max": float(os.getenv("INVESTMENT_CAC_MAX", "100")),
            "ltv_min": float(os.getenv("INVESTMENT_LTV_MIN", "300")),
            "churn_max": float(os.getenv("INVESTMENT_CHURN_MAX", "0.05"))
        }
    }
    
    # Paramètres de l'orchestrateur
    ORCHESTRATOR_CONFIG = {
        "max_concurrent_evaluations": int(os.getenv("MAX_CONCURRENT_EVALUATIONS", "10")),
        "evaluation_timeout": int(os.getenv("EVALUATION_TIMEOUT", "300")),  # 5 minutes
        "cache_ttl": int(os.getenv("CACHE_TTL", "3600"))  # 1 heure
    }
    
    # API Configuration
    API_CONFIG = {
        "host": os.getenv("API_HOST", "0.0.0.0"),
        "port": int(os.getenv("API_PORT", "8000")),
        "cors_origins": os.getenv("CORS_ORIGINS", "*").split(","),
        "rate_limit": int(os.getenv("RATE_LIMIT", "100"))  # requêtes par minute
    }
    
    # Base de données (pour les évolutions futures)
    DATABASE_CONFIG = {
        "url": os.getenv("DATABASE_URL", "sqlite:///startupai.db"),
        "pool_size": int(os.getenv("DB_POOL_SIZE", "10")),
        "max_overflow": int(os.getenv("DB_MAX_OVERFLOW", "20"))
    }
    
    # Monitoring et métriques
    MONITORING_CONFIG = {
        "enabled": os.getenv("MONITORING_ENABLED", "false").lower() == "true",
        "prometheus_port": int(os.getenv("PROMETHEUS_PORT", "9090")),
        "health_check_interval": int(os.getenv("HEALTH_CHECK_INTERVAL", "30"))
    }
    
    @classmethod
    def get_investor_config(cls) -> Dict[str, Any]:
        """Retourne la configuration de l'InvestorAgent"""
        return cls.INVESTOR_CONFIG
    
    @classmethod
    def get_orchestrator_config(cls) -> Dict[str, Any]:
        """Retourne la configuration de l'orchestrateur"""
        return cls.ORCHESTRATOR_CONFIG
    
    @classmethod
    def get_api_config(cls) -> Dict[str, Any]:
        """Retourne la configuration de l'API"""
        return cls.API_CONFIG
    
    @classmethod
    def is_production(cls) -> bool:
        """Vérifie si l'environnement est en production"""
        return cls.ENV.lower() == "production"
    
    @classmethod
    def is_development(cls) -> bool:
        """Vérifie si l'environnement est en développement"""
        return cls.ENV.lower() == "development"

# Instance globale de configuration
config = Config()

# Variables d'environnement par défaut
DEFAULT_ENV_VARS = {
    "ENV": "development",
    "DEBUG": "true",
    "LOG_LEVEL": "INFO",
    "API_HOST": "0.0.0.0",
    "API_PORT": "8000",
    "CORS_ORIGINS": "*",
    "RATE_LIMIT": "100",
    "MAX_CONCURRENT_EVALUATIONS": "10",
    "EVALUATION_TIMEOUT": "300",
    "CACHE_TTL": "3600",
    "VC_MULTIPLE_SAAS": "8.0",
    "VC_MULTIPLE_MARKETPLACE": "6.0",
    "VC_MULTIPLE_FINTECH": "10.0",
    "VC_MULTIPLE_AI": "12.0",
    "VC_MULTIPLE_DEFAULT": "7.0",
    "INVESTMENT_MRR_MIN": "5000",
    "INVESTMENT_CAC_MAX": "100",
    "INVESTMENT_LTV_MIN": "300",
    "INVESTMENT_CHURN_MAX": "0.05"
}

def print_config():
    """Affiche la configuration actuelle"""
    print("🔧 Configuration StartupAI - Epic 11")
    print("=" * 50)
    print(f"🌍 Environnement: {config.ENV}")
    print(f"🐛 Debug: {config.DEBUG}")
    print(f"📝 Log Level: {config.LOG_LEVEL}")
    print(f"🌐 API Host: {config.API_CONFIG['host']}")
    print(f"🔌 API Port: {config.API_CONFIG['port']}")
    print(f"📊 Max Evaluations: {config.ORCHESTRATOR_CONFIG['max_concurrent_evaluations']}")
    print(f"⏱️  Timeout: {config.ORCHESTRATOR_CONFIG['evaluation_timeout']}s")
    print("=" * 50)

if __name__ == "__main__":
    print_config()