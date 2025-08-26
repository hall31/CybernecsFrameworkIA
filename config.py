#!/usr/bin/env python3
"""
Configuration du système d'agents IA pour création de startup
"""

# Configuration générale
GENERAL_CONFIG = {
    "project_name": "StartupGenerator",
    "version": "1.0.0",
    "author": "AI Development Team",
    "description": "Système d'agents IA pour création automatique de startup"
}

# Configuration des agents
AGENTS_CONFIG = {
    "ceo_agent": {
        "enabled": True,
        "vision_templates": [
            "Révolutionner le marché avec {idea}",
            "Créer la plateforme leader de {idea}",
            "Transformer l'industrie de {idea}",
            "Démocratiser l'accès à {idea}"
        ],
        "objectifs_default": [
            "Créer une plateforme innovante et intuitive",
            "Atteindre 10,000 utilisateurs dans la première année",
            "Générer 1M€ de revenus récurrents",
            "Devenir la référence du secteur"
        ],
        "etapes_default": [
            "Phase 1: MVP et validation marché (3 mois)",
            "Phase 2: Développement des fonctionnalités avancées (6 mois)",
            "Phase 3: Expansion et internationalisation (12 mois)",
            "Phase 4: Optimisation et scaling (18 mois)"
        ]
    },
    
    "cto_agent": {
        "enabled": True,
        "stacks_available": {
            "laravel_react": {
                "name": "Laravel + React",
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
                }
            },
            "node_react": {
                "name": "Node.js + React",
                "backend": {
                    "framework": "Express.js",
                    "database": "MongoDB",
                    "authentication": "JWT",
                    "api": "REST API",
                    "deployment": "Docker + Nginx"
                },
                "frontend": {
                    "framework": "React 18",
                    "styling": "Tailwind CSS",
                    "routing": "React Router",
                    "state_management": "Redux Toolkit",
                    "build_tool": "Vite"
                }
            },
            "python_react": {
                "name": "Python + React",
                "backend": {
                    "framework": "FastAPI",
                    "database": "PostgreSQL",
                    "authentication": "JWT",
                    "api": "REST API + GraphQL",
                    "deployment": "Docker + Nginx"
                },
                "frontend": {
                    "framework": "React 18",
                    "styling": "Tailwind CSS",
                    "routing": "React Router",
                    "state_management": "Zustand",
                    "build_tool": "Vite"
                }
            }
        },
        "default_stack": "laravel_react"
    },
    
    "dev_backend_agent": {
        "enabled": True,
        "frameworks": {
            "laravel": {
                "version": "10.0",
                "features": [
                    "Authentication avec Sanctum",
                    "API REST complète",
                    "Validation des données",
                    "Tests unitaires",
                    "Configuration CORS",
                    "Middleware de sécurité"
                ],
                "models_default": ["User", "Product"],
                "api_endpoints_default": [
                    "POST /api/login",
                    "POST /api/register",
                    "GET /api/products",
                    "POST /api/products",
                    "PUT /api/products/{id}",
                    "DELETE /api/products/{id}"
                ]
            },
            "express": {
                "version": "4.18",
                "features": [
                    "Authentication JWT",
                    "API REST complète",
                    "Validation avec Joi",
                    "Tests avec Jest",
                    "CORS configuré",
                    "Rate limiting"
                ]
            },
            "fastapi": {
                "version": "0.104",
                "features": [
                    "Authentication JWT",
                    "API REST + GraphQL",
                    "Validation Pydantic",
                    "Tests avec pytest",
                    "Documentation auto",
                    "Async support"
                ]
            }
        }
    },
    
    "dev_frontend_agent": {
        "enabled": True,
        "frameworks": {
            "react": {
                "version": "18.2",
                "features": [
                    "Authentication complète",
                    "Dashboard avec navigation",
                    "Gestion des produits (CRUD)",
                    "Design moderne avec Tailwind",
                    "Routing avec React Router",
                    "Intégration API"
                ],
                "pages_default": [
                    "/login",
                    "/register",
                    "/dashboard",
                    "/products"
                ],
                "components_default": [
                    "Sidebar",
                    "Topbar",
                    "ProductList",
                    "ProductForm",
                    "LoginPage",
                    "RegisterPage"
                ]
            },
            "vue": {
                "version": "3.3",
                "features": [
                    "Authentication complète",
                    "Dashboard responsive",
                    "Gestion des données",
                    "Design avec Tailwind",
                    "Routing avec Vue Router",
                    "Composition API"
                ]
            },
            "angular": {
                "version": "17.0",
                "features": [
                    "Authentication avec Guards",
                    "Dashboard Material Design",
                    "Gestion des données",
                    "Styling avec Angular Material",
                    "Routing avec Angular Router",
                    "Services et interceptors"
                ]
            }
        }
    }
}

# Configuration de l'infrastructure
INFRASTRUCTURE_CONFIG = {
    "docker": {
        "enabled": True,
        "services": {
            "backend": {
                "ports": ["8000:8000"],
                "volumes": ["./backend:/var/www"],
                "environment": {
                    "APP_ENV": "local",
                    "APP_DEBUG": "true"
                }
            },
            "frontend": {
                "ports": ["3000:3000"],
                "volumes": ["./frontend:/app"],
                "environment": {
                    "REACT_APP_API_URL": "http://localhost:8000/api"
                }
            },
            "database": {
                "ports": ["3306:3306"],
                "environment": {
                    "MYSQL_DATABASE": "startup_db",
                    "MYSQL_USER": "startup_user",
                    "MYSQL_PASSWORD": "startup_password"
                }
            },
            "redis": {
                "ports": ["6379:6379"],
                "volumes": ["redis_data:/data"]
            },
            "nginx": {
                "ports": ["80:80", "443:443"],
                "volumes": ["./nginx:/etc/nginx"]
            }
        }
    },
    
    "monitoring": {
        "enabled": True,
        "tools": {
            "laravel_telescope": True,
            "log_monitoring": True,
            "performance_metrics": True,
            "error_tracking": True
        }
    }
}

# Configuration des tests
TESTING_CONFIG = {
    "backend": {
        "framework": "PHPUnit",
        "coverage": True,
        "tests_default": [
            "User authentication",
            "Product CRUD operations",
            "API endpoints validation",
            "Database migrations"
        ]
    },
    "frontend": {
        "framework": "Jest + React Testing Library",
        "coverage": True,
        "tests_default": [
            "Component rendering",
            "User interactions",
            "API integration",
            "Routing navigation"
        ]
    }
}

# Configuration de la sécurité
SECURITY_CONFIG = {
    "authentication": {
        "method": "token_based",
        "expiration": "24h",
        "refresh_tokens": True,
        "password_policy": {
            "min_length": 8,
            "require_uppercase": True,
            "require_numbers": True,
            "require_special": True
        }
    },
    "cors": {
        "allowed_origins": ["*"],
        "allowed_methods": ["GET", "POST", "PUT", "DELETE"],
        "allowed_headers": ["*"],
        "expose_headers": ["Authorization"]
    },
    "rate_limiting": {
        "enabled": True,
        "max_requests": 100,
        "window_minutes": 15
    }
}

# Configuration du déploiement
DEPLOYMENT_CONFIG = {
    "environments": {
        "development": {
            "debug": True,
            "logging": "debug",
            "database": "local",
            "cache": "file"
        },
        "staging": {
            "debug": False,
            "logging": "info",
            "database": "staging",
            "cache": "redis"
        },
        "production": {
            "debug": False,
            "logging": "error",
            "database": "production",
            "cache": "redis_cluster"
        }
    },
    "ci_cd": {
        "enabled": True,
        "platform": "github_actions",
        "stages": [
            "test",
            "build",
            "deploy_staging",
            "deploy_production"
        ]
    }
}

# Configuration des métriques
METRICS_CONFIG = {
    "business": [
        "Utilisateurs actifs mensuels",
        "Taux de rétention",
        "Revenus mensuels récurrents",
        "Taux de conversion",
        "Temps de session moyen"
    ],
    "technical": [
        "Temps de réponse API",
        "Taux d'erreur",
        "Disponibilité du service",
        "Temps de chargement",
        "Utilisation des ressources"
    ]
}

def get_config(section=None):
    """
    Récupère la configuration complète ou une section spécifique
    
    Args:
        section: Section de configuration à récupérer
        
    Returns:
        Dict de configuration
    """
    if section:
        return globals().get(f"{section.upper()}_CONFIG", {})
    
    return {
        "general": GENERAL_CONFIG,
        "agents": AGENTS_CONFIG,
        "infrastructure": INFRASTRUCTURE_CONFIG,
        "testing": TESTING_CONFIG,
        "security": SECURITY_CONFIG,
        "deployment": DEPLOYMENT_CONFIG,
        "metrics": METRICS_CONFIG
    }

def get_agent_config(agent_name):
    """
    Récupère la configuration d'un agent spécifique
    
    Args:
        agent_name: Nom de l'agent
        
    Returns:
        Dict de configuration de l'agent
    """
    return AGENTS_CONFIG.get(agent_name, {})

def is_agent_enabled(agent_name):
    """
    Vérifie si un agent est activé
    
    Args:
        agent_name: Nom de l'agent
        
    Returns:
        bool: True si l'agent est activé
    """
    agent_config = get_agent_config(agent_name)
    return agent_config.get("enabled", False)

def get_available_stacks():
    """
    Récupère les stacks techniques disponibles
    
    Returns:
        Dict des stacks disponibles
    """
    return AGENTS_CONFIG["cto_agent"]["stacks_available"]

def get_default_stack():
    """
    Récupère la stack technique par défaut
    
    Returns:
        str: Nom de la stack par défaut
    """
    return AGENTS_CONFIG["cto_agent"]["default_stack"]

if __name__ == "__main__":
    # Affichage de la configuration
    config = get_config()
    print("🔧 CONFIGURATION DU SYSTÈME D'AGENTS")
    print("=" * 50)
    
    for section, data in config.items():
        print(f"\n📋 {section.upper()}:")
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, (list, dict)):
                    print(f"   {key}: {type(value).__name__} ({len(value)} items)")
                else:
                    print(f"   {key}: {value}")
        else:
            print(f"   {data}")
    
    print(f"\n✅ Configuration chargée avec succès")
    print(f"🚀 Agents activés: {sum(1 for agent in AGENTS_CONFIG.values() if agent.get('enabled', False))}")
    print(f"🔧 Stacks disponibles: {len(get_available_stacks())}")
    print(f"🎯 Stack par défaut: {get_default_stack()}")