# 🚀 Startup Generated - Epic2

Ce dossier contient le scaffold complet de votre startup générée automatiquement par Epic2.

## 📁 Structure

```
generated/
├── docker-compose.yml          # Orchestration des services
├── backend/
│   └── Dockerfile             # Container PHP/Laravel
├── frontend/
│   ├── Dockerfile             # Container Node.js/React
│   ├── package.json           # Dépendances React
│   ├── vite.config.js         # Configuration Vite
│   └── src/                   # Code source React
├── start.sh                   # Script de lancement
└── README.md                  # Ce fichier
```

## 🚀 Lancement Rapide

### Prérequis
- Docker
- Docker Compose

### 1. Lancer avec le script automatique
```bash
./start.sh
```

### 2. Lancer manuellement
```bash
# Construction des images
docker-compose build

# Lancement des services
docker-compose up -d
```

## 📱 Accès aux Services

- **Frontend React**: http://localhost:3000
- **Backend Laravel**: http://localhost:9000
- **Base de données**: localhost:5432

## 🔧 Stack Technique

- **Backend**: Laravel (PHP 8.2) + PostgreSQL
- **Frontend**: React + Vite
- **Base de données**: PostgreSQL 15
- **Orchestration**: Docker Compose

## 📋 Commandes Utiles

```bash
# Voir les logs
docker-compose logs -f

# Arrêter les services
docker-compose down

# Redémarrer
docker-compose restart

# Statut des services
docker-compose ps

# Reconstruire après modification
docker-compose build --no-cache
```

## 🛠️ Développement

### Frontend
Le frontend React est configuré avec Vite pour un développement rapide. Les modifications sont automatiquement rechargées.

### Backend
Le backend Laravel est configuré avec les extensions PHP nécessaires pour PostgreSQL.

### Base de données
PostgreSQL est configuré avec les identifiants par défaut :
- User: admin
- Password: secret
- Database: appdb

## 🔍 Dépannage

### Ports déjà utilisés
Si les ports sont déjà utilisés, modifiez `docker-compose.yml` et les Dockerfiles.

### Problèmes de permissions
Assurez-vous d'avoir les droits d'exécution sur `start.sh`.

### Logs détaillés
```bash
docker-compose logs -f [service_name]
```

## 🚀 Prochaines Étapes

1. **Développement des fonctionnalités métier**
2. **Configuration de l'authentification**
3. **Implémentation de la logique de paiement**
4. **Tests et déploiement**

## 📞 Support

Ce scaffold a été généré automatiquement par Epic2 - Startup Creator.
Pour toute question, consultez la documentation principale du projet.