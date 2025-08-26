#!/bin/bash
# Script de démarrage de l'API Admin FastAPI

echo "🚀 Démarrage de l'API Admin FastAPI..."
echo "📍 Port: 8000"
echo "📚 Documentation: http://localhost:8000/docs"
echo "=" * 50

# Activation de l'environnement virtuel
source venv/bin/activate

# Lancement de l'API
python launch_admin_api.py