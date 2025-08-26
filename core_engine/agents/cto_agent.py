import os
import json
from typing import Dict, List
from .base_agent import BaseAgent


class CTOAgent(BaseAgent):
    """
    Agent CTO responsable de la définition de la stack technique
    et de la génération du scaffold du projet
    """
    
    def __init__(self):
        super().__init__("CTOAgent")
    
    def run(self, roadmap: Dict) -> Dict:
        """
        Génère la stack technique et le scaffold du projet
        
        Args:
            roadmap: Roadmap générée par le CEOAgent
            
        Returns:
            Dict contenant la stack technique et les services
        """
        self.log_event("CTOAgent", "Démarrage de la génération de la stack technique")
        
        # Définition de la stack technique
        stack_info = {
            "stack": "Laravel + React + PostgreSQL",
            "services": ["backend", "frontend", "db"],
            "files": ["docker-compose.yml", "backend/Dockerfile", "frontend/Dockerfile"]
        }
        
        # Création du dossier generated s'il n'existe pas
        os.makedirs("generated", exist_ok=True)
        
        # Génération des fichiers Docker
        self._generate_docker_compose()
        self._generate_backend_dockerfile()
        self._generate_frontend_dockerfile()
        
        # Mise à jour du roadmap avec la stack technique (sans modifier l'entrée)
        updated_roadmap = roadmap.copy()
        updated_roadmap["technical_stack"] = stack_info
        
        self.log_event("CTOAgent", "Stack technique générée avec succès")
        
        return stack_info
    
    def _generate_docker_compose(self):
        """Génère le fichier docker-compose.yml"""
        docker_compose_content = '''version: "3.8"
services:
  backend:
    build: ./backend
    ports:
      - "9000:9000"
    volumes:
      - ./backend:/app
    depends_on:
      - db
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    volumes:
      - ./frontend:/app
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: appdb
    ports:
      - "5432:5432"
'''
        
        with open("generated/docker-compose.yml", "w") as f:
            f.write(docker_compose_content)
        
        self.log_event("CTOAgent", "Docker-compose généré")
    
    def _generate_backend_dockerfile(self):
        """Génère le Dockerfile du backend"""
        os.makedirs("generated/backend", exist_ok=True)
        
        backend_dockerfile_content = '''FROM php:8.2-cli
RUN apt-get update && apt-get install -y unzip git curl libpq-dev \\\\
  && docker-php-ext-install pdo pdo_pgsql
WORKDIR /app
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN composer create-project laravel/laravel .
CMD ["php", "artisan", "serve", "--host=0.0.0.0", "--port=9000"]
'''
        
        with open("generated/backend/Dockerfile", "w") as f:
            f.write(backend_dockerfile_content)
        
        self.log_event("CTOAgent", "Backend Dockerfile généré")
    
    def _generate_frontend_dockerfile(self):
        """Génère le Dockerfile du frontend"""
        os.makedirs("generated/frontend", exist_ok=True)
        
        frontend_dockerfile_content = '''FROM node:18
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
CMD ["npm", "run", "dev"]
'''
        
        with open("generated/frontend/Dockerfile", "w") as f:
            f.write(frontend_dockerfile_content)
        
        self.log_event("CTOAgent", "Frontend Dockerfile généré")