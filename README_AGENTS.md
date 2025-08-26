# 🚀 Epic3 - Agents IA Fullstack pour Création de Startup

Ce projet implémente un système d'agents IA qui créent automatiquement une startup complète avec backend Laravel et frontend React + Tailwind.

## 📋 Architecture

```
core-engine/
├── agents/
│   ├── __init__.py
│   ├── dev_backend_agent.py    # Agent développement Laravel
│   └── dev_frontend_agent.py   # Agent développement React
├── main.py                     # Orchestrateur principal
└── generated/                  # Code généré
    ├── backend/               # API Laravel
    ├── frontend/              # App React
    ├── nginx/                 # Configuration Nginx
    └── docker-compose.yml     # Infrastructure Docker
```

## 🎯 Agents Disponibles

### 1. DevBackendAgent (Laravel)

**Responsabilités :**
- Initialise un projet Laravel complet
- Configure l'authentification avec Sanctum
- Crée les modèles User et Product
- Implémente une API REST complète
- Ajoute des tests unitaires
- Configure CORS et middleware

**Fonctionnalités :**
- ✅ Authentication (login/register/logout)
- ✅ Users CRUD avec rôles
- ✅ Products CRUD complet
- ✅ API REST avec validation
- ✅ Tests unitaires
- ✅ Configuration CORS

**Endpoints API :**
```
POST   /api/login
POST   /api/register
GET    /api/products
POST   /api/products
PUT    /api/products/{id}
DELETE /api/products/{id}
```

### 2. DevFrontendAgent (React + Tailwind)

**Responsabilités :**
- Crée une application React moderne
- Configure Tailwind CSS pour un design SaaS
- Implémente l'authentification complète
- Crée un dashboard avec navigation
- Gère les produits (CRUD)
- Intègre l'API Laravel

**Fonctionnalités :**
- ✅ Pages Login/Register
- ✅ Dashboard avec Sidebar + Topbar
- ✅ Gestion des produits (list/add/edit/delete)
- ✅ Design moderne avec Tailwind CSS
- ✅ Routing avec React Router
- ✅ Intégration API Laravel

**Pages disponibles :**
- `/login` - Connexion utilisateur
- `/register` - Inscription utilisateur
- `/dashboard` - Tableau de bord principal
- `/products` - Gestion des produits

## 🚀 Utilisation

### 1. Exécution Simple

```bash
python main.py
```

### 2. Utilisation Programmée

```python
from main import StartupOrchestrator

orchestrator = StartupOrchestrator()
result = orchestrator.create_startup("SaaS marketplace pour freelances")

if result["status"] == "success":
    print(f"Startup créée dans: {result['generated_path']}")
```

### 3. Utilisation des Agents Individuels

```python
from core_engine.agents.dev_backend_agent import DevBackendAgent
from core_engine.agents.dev_frontend_agent import DevFrontendAgent

# Développer le backend
backend_agent = DevBackendAgent()
backend_result = backend_agent.run(stack_config)

# Développer le frontend
frontend_agent = DevFrontendAgent()
frontend_result = frontend_agent.run(stack_config)
```

## 📁 Structure Générée

Après exécution, le dossier `generated/` contient :

```
generated/
├── backend/                    # API Laravel
│   ├── app/
│   │   ├── Http/Controllers/  # Contrôleurs API
│   │   └── Models/            # Modèles Eloquent
│   ├── database/migrations/   # Migrations DB
│   ├── routes/api.php         # Routes API
│   ├── tests/                 # Tests unitaires
│   └── composer.json          # Dépendances PHP
├── frontend/                   # App React
│   ├── src/
│   │   ├── components/        # Composants réutilisables
│   │   ├── pages/             # Pages de l'application
│   │   ├── services/          # Services API
│   │   ├── App.jsx            # Composant principal
│   │   └── index.js           # Point d'entrée
│   ├── public/index.html      # Template HTML
│   ├── package.json           # Dépendances Node.js
│   └── tailwind.config.js     # Configuration Tailwind
├── nginx/                      # Configuration Nginx
│   └── nginx.conf             # Reverse proxy
├── docker-compose.yml          # Infrastructure Docker
└── startup_result.json         # Résultat de la génération
```

## 🐳 Démarrage avec Docker

### 1. Prérequis
- Docker et Docker Compose installés
- Ports 80, 3000, 3306, 6379 disponibles

### 2. Démarrage
```bash
cd generated
docker-compose up -d
```

### 3. Accès
- **Frontend React** : http://localhost
- **Backend API** : http://localhost/api
- **Base de données** : localhost:3306
- **Redis** : localhost:6379

## 🔧 Configuration

### Variables d'Environnement

Le système utilise des variables d'environnement par défaut :

```bash
# Database
DB_HOST=mysql
DB_DATABASE=startup_db
DB_USERNAME=startup_user
DB_PASSWORD=startup_password

# Frontend
REACT_APP_API_URL=http://localhost:8000/api
```

### Personnalisation

Pour personnaliser la génération :

1. **Modifier les agents** dans `core-engine/agents/`
2. **Ajuster la stack** dans `main.py`
3. **Configurer Docker** dans `docker-compose.yml`

## 🧪 Tests

### Backend Laravel
```bash
cd generated/backend
composer install
php artisan test
```

### Frontend React
```bash
cd generated/frontend
npm install
npm test
```

## 📊 Monitoring

- **Laravel Telescope** : Monitoring des requêtes et erreurs
- **Logs** : Chaque agent log ses actions
- **Métriques** : Dashboard avec statistiques

## 🔒 Sécurité

- **Authentication** : Laravel Sanctum avec tokens
- **Validation** : Validation des données côté serveur
- **CORS** : Configuration sécurisée pour les origines
- **Middleware** : Protection des routes API

## 🚀 Roadmap

### Phase 1 - MVP (Actuel)
- ✅ Backend Laravel avec API REST
- ✅ Frontend React avec Tailwind
- ✅ Authentication complète
- ✅ Gestion des produits
- ✅ Infrastructure Docker

### Phase 2 - Fonctionnalités Avancées
- 🔄 Système de rôles et permissions
- 🔄 Notifications en temps réel
- 🔄 Upload de fichiers
- 🔄 API documentation (Swagger)
- 🔄 Tests d'intégration

### Phase 3 - Production
- 🔄 CI/CD avec GitHub Actions
- 🔄 Monitoring et alerting
- 🔄 Backup automatisé
- 🔄 Scaling horizontal
- 🔄 CDN et optimisation

## 🤝 Contribution

1. Fork le projet
2. Créez une branche feature (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 🆘 Support

Pour toute question ou problème :

1. Consultez la documentation
2. Vérifiez les logs des agents
3. Ouvrez une issue sur GitHub
4. Contactez l'équipe de développement

---

**🚀 Prêt à créer votre startup ? Lancez `python main.py` et laissez la magie opérer !**