.PHONY: help install test run build up down logs clean

# Variables
PYTHON = python3
PIP = pip3
DOCKER = docker
COMPOSE = docker-compose

# Couleurs pour l'affichage
GREEN = \033[0;32m
YELLOW = \033[1;33m
BLUE = \033[0;34m
RED = \033[0;31m
NC = \033[0m # No Color

help: ## Affiche cette aide
	@echo "$(BLUE)🧩 Core Engine - Startup Orchestrator$(NC)"
	@echo ""
	@echo "$(YELLOW)Commandes disponibles:$(NC)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-15s$(NC) %s\n", $$1, $$2}'

install: ## Installe les dépendances Python
	@echo "$(BLUE)📦 Installation des dépendances...$(NC)"
	$(PYTHON) -m pip install -r requirements.txt

test-local: ## Teste le CEO Agent localement
	@echo "$(BLUE)🧪 Test local du CEO Agent...$(NC)"
	$(PYTHON) test_local.py

test-api: ## Teste l'API (nécessite que l'API soit en cours d'exécution)
	@echo "$(BLUE)🧪 Test de l'API...$(NC)"
	$(PYTHON) test_api.py

run: ## Lance l'application FastAPI localement
	@echo "$(BLUE)🚀 Lancement de l'application...$(NC)"
	$(PYTHON) main.py

build: ## Construit l'image Docker
	@echo "$(BLUE)🐳 Construction de l'image Docker...$(NC)"
	$(DOCKER) build -t core-engine .

up: ## Lance les services avec Docker Compose
	@echo "$(BLUE)🚀 Lancement des services...$(NC)"
	$(COMPOSE) up -d

up-build: ## Lance les services avec rebuild
	@echo "$(BLUE)🚀 Lancement des services avec rebuild...$(NC)"
	$(COMPOSE) up --build -d

down: ## Arrête les services Docker Compose
	@echo "$(BLUE)🛑 Arrêt des services...$(NC)"
	$(COMPOSE) down

logs: ## Affiche les logs des services
	@echo "$(BLUE)📝 Affichage des logs...$(NC)"
	$(COMPOSE) logs -f

clean: ## Nettoie les fichiers temporaires
	@echo "$(BLUE)🧹 Nettoyage...$(NC)"
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type f -name "*.log" -delete

status: ## Affiche le statut des services
	@echo "$(BLUE)📊 Statut des services...$(NC)"
	$(COMPOSE) ps

restart: ## Redémarre les services
	@echo "$(BLUE)🔄 Redémarrage des services...$(NC)"
	$(COMPOSE) restart

shell: ## Ouvre un shell dans le container
	@echo "$(BLUE)🐚 Ouverture du shell...$(NC)"
	$(COMPOSE) exec core-engine /bin/bash

# Commandes de développement
dev-install: install ## Installation pour le développement
	@echo "$(GREEN)✅ Installation terminée$(NC)"

dev-test: test-local ## Tests de développement
	@echo "$(GREEN)✅ Tests terminés$(NC)"

dev-run: run ## Lancement en mode développement
	@echo "$(GREEN)✅ Application lancée$(NC)"

# Commandes de production
prod-build: build ## Build de production
	@echo "$(GREEN)✅ Build terminé$(NC)"

prod-up: up-build ## Déploiement en production
	@echo "$(GREEN)✅ Déploiement terminé$(NC)"

prod-down: down ## Arrêt de production
	@echo "$(GREEN)✅ Arrêt terminé$(NC)"