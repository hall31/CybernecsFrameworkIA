#!/usr/bin/env python3
"""
Orchestrateur principal pour la création de startup
Exécute tous les agents dans l'ordre : CEO → CTO → DevBackend → DevFrontend
"""

import logging
import json
from pathlib import Path
from typing import Dict, Any

# Import des agents
from core_engine.agents.dev_backend_agent import DevBackendAgent
from core_engine.agents.dev_frontend_agent import DevFrontendAgent

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
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