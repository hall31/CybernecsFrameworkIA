#!/bin/bash

# Script de déploiement rapide pour StartupAI - Epic 11
# Usage: ./deploy.sh [development|production]

set -e

# Couleurs pour l'affichage
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
ENVIRONMENT=${1:-development}
PROJECT_NAME="startupai-epic11"
VERSION="1.0.0"

echo -e "${BLUE}🚀 Déploiement StartupAI - Epic 11: Investisseur IA${NC}"
echo "=================================================="
echo -e "${YELLOW}Environnement: ${ENVIRONMENT}${NC}"
echo -e "${YELLOW}Version: ${VERSION}${NC}"
echo ""

# Fonction de vérification des prérequis
check_prerequisites() {
    echo -e "${BLUE}🔍 Vérification des prérequis...${NC}"
    
    # Vérification de Docker
    if ! command -v docker &> /dev/null; then
        echo -e "${RED}❌ Docker n'est pas installé${NC}"
        exit 1
    fi
    
    # Vérification de Docker Compose
    if ! command -v docker-compose &> /dev/null; then
        echo -e "${RED}❌ Docker Compose n'est pas installé${NC}"
        exit 1
    fi
    
    # Vérification de Node.js (pour le build frontend)
    if ! command -v node &> /dev/null; then
        echo -e "${YELLOW}⚠️  Node.js n'est pas installé, utilisation du build Docker${NC}"
    fi
    
    echo -e "${GREEN}✅ Prérequis vérifiés${NC}"
    echo ""
}

# Fonction de build du frontend
build_frontend() {
    echo -e "${BLUE}🏗️  Build du frontend...${NC}"
    
    if command -v node &> /dev/null && command -v npm &> /dev/null; then
        echo "📦 Installation des dépendances..."
        cd frontend
        npm install
        
        echo "🔨 Build de l'application..."
        npm run build
        
        cd ..
        echo -e "${GREEN}✅ Frontend buildé avec succès${NC}"
    else
        echo -e "${YELLOW}⚠️  Build du frontend différé au Docker${NC}"
    fi
    
    echo ""
}

# Fonction de déploiement Docker
deploy_docker() {
    echo -e "${BLUE}🐳 Déploiement Docker...${NC}"
    
    # Arrêt des conteneurs existants
    echo "🛑 Arrêt des conteneurs existants..."
    docker-compose down --remove-orphans
    
    # Nettoyage des images
    echo "🧹 Nettoyage des images..."
    docker system prune -f
    
    # Build et démarrage
    echo "🔨 Build et démarrage des services..."
    if [ "$ENVIRONMENT" = "production" ]; then
        docker-compose -f docker-compose.yml up --build -d
    else
        # Mode développement - seulement le backend
        docker-compose -f docker-compose.yml up --build -d startupai-backend
    fi
    
    echo -e "${GREEN}✅ Services déployés avec succès${NC}"
    echo ""
}

# Fonction de vérification de la santé
health_check() {
    echo -e "${BLUE}🏥 Vérification de la santé des services...${NC}"
    
    # Attendre que les services démarrent
    echo "⏳ Attente du démarrage des services..."
    sleep 30
    
    # Vérification du backend
    if curl -f ${PROTOCOL}://localhost:8000/health &> /dev/null; then
        echo -e "${GREEN}✅ Backend opérationnel${NC}"
    else
        echo -e "${RED}❌ Backend non accessible${NC}"
    fi
    
    # Vérification du frontend (si en production)
    if [ "$ENVIRONMENT" = "production" ]; then
        if curl -f http://localhost:3000/health &> /dev/null; then
            echo -e "${GREEN}✅ Frontend opérationnel${NC}"
        else
            echo -e "${RED}❌ Frontend non accessible${NC}"
        fi
    fi
    
    echo ""
}

# Fonction d'affichage des informations
show_info() {
    echo -e "${BLUE}📊 Informations de déploiement${NC}"
    echo "=================================================="
    
    if [ "$ENVIRONMENT" = "production" ]; then
        echo -e "${GREEN}🌐 Frontend: http://localhost:3000${NC}"
        echo -e "${GREEN}🔌 Backend: http://localhost:8000${NC}"
        echo -e "${GREEN}📊 Prometheus: http://localhost:9090${NC}"
        echo -e "${GREEN}📈 Grafana: http://localhost:3001 (admin/admin)${NC}"
    else
        echo -e "${GREEN}🔌 Backend: http://localhost:8000${NC}"
        echo -e "${YELLOW}🌐 Frontend: Mode développement (npm start)${NC}"
    fi
    
    echo ""
    echo -e "${BLUE}📋 Commandes utiles:${NC}"
    echo "  - Voir les logs: docker-compose logs -f"
    echo "  - Arrêter: docker-compose down"
    echo "  - Redémarrer: docker-compose restart"
    echo "  - Status: docker-compose ps"
    echo ""
}

# Fonction principale
main() {
    echo -e "${BLUE}🚀 Démarrage du déploiement...${NC}"
    echo ""
    
    check_prerequisites
    build_frontend
    deploy_docker
    health_check
    show_info
    
    echo -e "${GREEN}🎉 Déploiement terminé avec succès!${NC}"
    echo ""
    
    if [ "$ENVIRONMENT" = "development" ]; then
        echo -e "${YELLOW}💡 Pour démarrer le frontend en mode développement:${NC}"
        echo "  cd frontend && npm start"
        echo ""
    fi
}

# Gestion des erreurs
trap 'echo -e "\n${RED}❌ Erreur lors du déploiement${NC}"; exit 1' ERR

# Exécution
main "$@"