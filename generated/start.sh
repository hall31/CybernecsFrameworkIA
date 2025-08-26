#!/bin/bash

echo "🚀 Lancement de la startup avec Docker..."
echo "=========================================="

# Vérification de Docker
if ! command -v docker &> /dev/null; then
    echo "❌ Docker n'est pas installé. Veuillez l'installer d'abord."
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose n'est pas installé. Veuillez l'installer d'abord."
    exit 1
fi

echo "✅ Docker et Docker Compose sont disponibles"

# Construction et lancement des services
echo "🔨 Construction des images Docker..."
docker-compose build

echo "🚀 Lancement des services..."
docker-compose up -d

echo ""
echo "🎉 Services lancés avec succès!"
echo ""
echo "📱 Accès aux services:"
echo "   • Frontend React: http://localhost:3000"
echo "   • Backend Laravel: http://localhost:9000"
echo "   • Base de données: localhost:5432"
echo ""
echo "📋 Commandes utiles:"
echo "   • Voir les logs: docker-compose logs -f"
echo "   • Arrêter: docker-compose down"
echo "   • Redémarrer: docker-compose restart"
echo ""
echo "🔍 Statut des services:"
docker-compose ps