#!/bin/bash

echo "🚀 Démarrage d'Epic6 Core Engine..."

# Vérifier si Docker est installé
if ! command -v docker &> /dev/null; then
    echo "❌ Docker n'est pas installé. Veuillez l'installer d'abord."
    exit 1
fi

# Vérifier si Docker Compose est installé
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose n'est pas installé. Veuillez l'installer d'abord."
    exit 1
fi

# Arrêter les conteneurs existants
echo "🛑 Arrêt des conteneurs existants..."
docker-compose down

# Construire et démarrer les services
echo "🔨 Construction et démarrage des services..."
docker-compose up --build -d

# Attendre que la base de données soit prête
echo "⏳ Attente de la base de données..."
sleep 10

# Vérifier le statut des services
echo "📊 Statut des services:"
docker-compose ps

echo ""
echo "✅ Epic6 Core Engine est démarré!"
echo "🌐 API disponible sur: http://localhost:8000"
echo "📚 Documentation API: http://localhost:8000/docs"
echo "🔍 Health check: http://localhost:8000/health"
echo ""
echo "Pour voir les logs: docker-compose logs -f app"
echo "Pour arrêter: docker-compose down"