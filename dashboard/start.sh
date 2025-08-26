#!/bin/bash

echo "🚀 Démarrage du Dashboard ShipFast..."
echo "=================================="

# Vérifier si Node.js est installé
if ! command -v node &> /dev/null; then
    echo "❌ Node.js n'est pas installé. Veuillez l'installer d'abord."
    exit 1
fi

# Vérifier si Python est installé
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 n'est pas installé. Veuillez l'installer d'abord."
    exit 1
fi

# Installer les dépendances du dashboard
echo "📦 Installation des dépendances du dashboard..."
npm install

# Installer les dépendances Python
echo "🐍 Installation des dépendances Python..."
pip3 install -r requirements.txt

echo ""
echo "✅ Toutes les dépendances sont installées!"
echo ""
echo "🌐 Pour lancer le dashboard:"
echo "   npm run dev"
echo ""
echo "🔌 Pour lancer le backend:"
echo "   python3 backend-example.py"
echo ""
echo "📊 Dashboard: http://localhost:3000"
echo "🔌 API: http://localhost:8000"
echo "📡 WebSocket: ws://localhost:8000/ws/logs"
echo ""
echo "🎯 Ou utilisez Docker Compose:"
echo "   docker-compose up"