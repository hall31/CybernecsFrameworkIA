#!/bin/bash

# 🚀 Script de démarrage Epic 12: AI Portfolio Manager
# Auteur: AI Assistant
# Date: $(date)

echo "🚀 Démarrage de l'Epic 12: AI Portfolio Manager"
echo "=================================================="

# Vérification de Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 n'est pas installé"
    exit 1
fi

# Vérification de Node.js
if ! command -v node &> /dev/null; then
    echo "⚠️  Node.js n'est pas installé. Le frontend ne pourra pas démarrer."
    echo "   Installez Node.js depuis: https://nodejs.org/"
fi

# Vérification de l'environnement virtuel
if [ ! -d "venv" ]; then
    echo "🔧 Création de l'environnement virtuel Python..."
    python3 -m venv venv
fi

# Activation de l'environnement virtuel
echo "🔧 Activation de l'environnement virtuel..."
source venv/bin/activate

# Installation des dépendances Python
echo "📦 Installation des dépendances Python..."
pip install -r requirements.txt

# Vérification de l'installation
if [ $? -eq 0 ]; then
    echo "✅ Dépendances Python installées avec succès"
else
    echo "❌ Erreur lors de l'installation des dépendances Python"
    exit 1
fi

# Démarrage du backend
echo "🚀 Démarrage du backend Flask..."
cd core-engine
python3 main.py &
BACKEND_PID=$!
cd ..

# Attendre que le backend démarre
echo "⏳ Attente du démarrage du backend..."
sleep 5

# Test de l'API
echo "🔍 Test de l'API backend..."
if curl -s http://localhost:5000/health > /dev/null; then
    echo "✅ Backend démarré avec succès sur http://localhost:5000"
else
    echo "❌ Erreur lors du démarrage du backend"
    kill $BACKEND_PID 2>/dev/null
    exit 1
fi

# Démarrage du frontend (si Node.js est disponible)
if command -v node &> /dev/null; then
    echo "🚀 Démarrage du frontend React..."
    cd frontend
    
    # Installation des dépendances Node.js
    if [ ! -d "node_modules" ]; then
        echo "📦 Installation des dépendances Node.js..."
        npm install
    fi
    
    # Démarrage du frontend
    npm start &
    FRONTEND_PID=$!
    cd ..
    
    echo "✅ Frontend démarré sur http://localhost:3000"
else
    echo "⚠️  Frontend non démarré (Node.js manquant)"
fi

echo ""
echo "🎉 Epic 12 démarré avec succès !"
echo "=================================================="
echo "📊 Backend API: http://localhost:5000"
echo "🎨 Frontend Dashboard: http://localhost:3000"
echo "📚 Documentation: README_EPIC12.md"
echo "🧪 Tests: python3 test_epic12.py"
echo ""
echo "🛑 Pour arrêter: Ctrl+C ou 'kill $BACKEND_PID $FRONTEND_PID'"
echo ""

# Fonction de nettoyage
cleanup() {
    echo ""
    echo "🛑 Arrêt de l'Epic 12..."
    kill $BACKEND_PID 2>/dev/null
    if [ ! -z "$FRONTEND_PID" ]; then
        kill $FRONTEND_PID 2>/dev/null
    fi
    echo "✅ Epic 12 arrêté"
    exit 0
}

# Capture du signal d'interruption
trap cleanup SIGINT SIGTERM

# Attendre indéfiniment
wait