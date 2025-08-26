# Makefile pour l'API Admin FastAPI
# Usage: make <command>

.PHONY: help start test install clean docs

# Variables
VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
API_PORT = 8000

help: ## Affiche l'aide
	@echo "🚀 API Admin FastAPI - Commandes disponibles:"
	@echo ""
	@echo "  make start     - Démarre l'API admin"
	@echo "  make test      - Lance tous les tests"
	@echo "  make install   - Installe les dépendances"
	@echo "  make clean     - Nettoie les fichiers temporaires"
	@echo "  make docs      - Ouvre la documentation"
	@echo "  make status    - Vérifie le statut de l'API"
	@echo ""

install: ## Installe les dépendances
	@echo "📦 Installation des dépendances..."
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt
	@echo "✅ Dépendances installées !"

start: ## Démarre l'API admin
	@echo "🚀 Démarrage de l'API Admin FastAPI..."
	@echo "📍 Port: $(API_PORT)"
	@echo "📚 Documentation: http://localhost:$(API_PORT)/docs"
	@echo "=" * 50
	$(PYTHON) launch_admin_api.py

test: ## Lance tous les tests
	@echo "🧪 Lancement des tests..."
	$(PYTHON) test_admin_api.py

clean: ## Nettoie les fichiers temporaires
	@echo "🧹 Nettoyage..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	@echo "✅ Nettoyage terminé !"

docs: ## Ouvre la documentation
	@echo "📚 Ouverture de la documentation..."
	@echo "🌐 Documentation Swagger: http://localhost:$(API_PORT)/docs"
	@echo "🌐 Documentation ReDoc: http://localhost:$(API_PORT)/redoc"

status: ## Vérifie le statut de l'API
	@echo "🏥 Vérification du statut de l'API..."
	@curl -s http://localhost:$(API_PORT)/health | python3 -m json.tool 2>/dev/null || echo "❌ API non accessible sur le port $(API_PORT)"

agents: ## Liste tous les agents
	@echo "🤖 Liste des agents..."
	@curl -s http://localhost:$(API_PORT)/agents | python3 -m json.tool 2>/dev/null || echo "❌ API non accessible sur le port $(API_PORT)"

epics: ## Liste toutes les épics
	@echo "📋 Liste des épics..."
	@curl -s http://localhost:$(API_PORT)/epics | python3 -m json.tool 2>/dev/null || echo "❌ API non accessible sur le port $(API_PORT)"

# Commande par défaut
.DEFAULT_GOAL := help