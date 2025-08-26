#!/bin/bash

# Script d'entrée Docker pour StartupAI - Epic 11

set -e

echo "🚀 Démarrage de StartupAI - Epic 11: Investisseur IA"
echo "=================================================="

# Vérification de l'environnement
echo "🌍 Environnement: ${ENV:-development}"
echo "🐛 Debug: ${DEBUG:-false}"
echo "📝 Log Level: ${LOG_LEVEL:-INFO}"

# Vérification des variables d'environnement critiques
if [ -z "$ENV" ]; then
    export ENV=development
    echo "⚠️  ENV non défini, utilisation de la valeur par défaut: development"
fi

# Vérification de la configuration
if [ "$ENV" = "production" ]; then
    echo "🏭 Mode production activé"
    export DEBUG=false
    export LOG_LEVEL=WARNING
else
    echo "🔧 Mode développement activé"
    export DEBUG=true
    export LOG_LEVEL=INFO
fi

# Vérification des permissions
if [ ! -w /app ]; then
    echo "❌ Erreur: Répertoire /app non accessible en écriture"
    exit 1
fi

# Vérification des fichiers critiques
if [ ! -f "/app/core-engine/main.py" ]; then
    echo "❌ Erreur: Fichier main.py introuvable"
    exit 1
fi

if [ ! -f "/app/core-engine/agents/investor_agent.py" ]; then
    echo "❌ Erreur: Fichier investor_agent.py introuvable"
    exit 1
fi

echo "✅ Vérifications terminées avec succès"

# Affichage de la configuration
echo ""
echo "🔧 Configuration actuelle:"
echo "  - ENV: $ENV"
echo "  - DEBUG: $DEBUG"
echo "  - LOG_LEVEL: $LOG_LEVEL"
echo "  - PYTHONPATH: $PYTHONPATH"
echo ""

# Démarrage de l'application
echo "🚀 Lancement de l'application..."
echo "=================================================="

# Exécution de la commande passée en argument
exec "$@"