#!/bin/bash

echo "🚀 Démarrage de l'API Startup Tokenization Marketplace"
echo "=================================================="

# Vérifier que Python est installé
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 n'est pas installé"
    exit 1
fi

# Vérifier que les fichiers nécessaires existent
if [ ! -f "main.py" ]; then
    echo "❌ main.py non trouvé"
    exit 1
fi

if [ ! -f "agents/market_agent.py" ]; then
    echo "❌ market_agent.py non trouvé"
    exit 1
fi

echo "✅ Fichiers vérifiés"
echo "📊 MarketAgent prêt"
echo "🌐 Démarrage du serveur Flask..."

# Démarrer l'API
python3 main.py