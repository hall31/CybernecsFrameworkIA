# Epic6 - Core Engine avec Persistance

## 🎯 Vue d'ensemble

Epic6 est une plateforme complète de génération de startups avec un backend FastAPI robuste et persistant, une interface React moderne, et une architecture WebSocket pour les logs en temps réel.

## 🏗️ Architecture

```
epic6/
├── core-engine/          # Backend FastAPI + PostgreSQL
│   ├── api/             # Routes et schémas API
│   ├── core/            # Configuration et base de données
│   ├── models/          # Modèles SQLAlchemy
│   ├── utils/           # Utilitaires (logger)
│   ├── generated/       # Code généré des projets
│   └── main.py          # Point d'entrée FastAPI
├── frontend/            # Interface React
│   ├── src/
│   │   ├── components/  # Composants React
│   │   └── ...
│   └── package.json
└── README.md
```

## 🚀 Fonctionnalités Principales

### Backend (Core Engine)
- **API REST complète** avec FastAPI
- **Persistance PostgreSQL** avec SQLAlchemy async
- **WebSockets** pour les logs en temps réel
- **Gestion des projets** avec CRUD complet
- **Téléchargement ZIP** des projets générés
- **Logs persistants** avec niveaux et timestamps
- **Migrations Alembic** pour la base de données

### Frontend (React)
- **Dashboard Startups** avec table responsive
- **Modal de détails** pour roadmap et stack
- **Téléchargement direct** des projets
- **Composant Logs** avec WebSocket en temps réel
- **Interface moderne** et responsive

## 📋 Prérequis

- Docker et Docker Compose
- Node.js 16+ (pour le frontend)
- Python 3.11+ (pour le développement backend)

## 🚀 Démarrage Rapide

### 1. Démarrer le Backend

```bash
cd core-engine
./start.sh
```

Le backend sera disponible sur `http://localhost:8000`

### 2. Démarrer le Frontend

```bash
cd frontend
npm install
npm start
```

Le frontend sera disponible sur `http://localhost:3000`

### 3. Vérifier l'Installation

```bash
# Test de l'API
cd core-engine
python test_api.py

# Ouverture de la documentation
open http://localhost:8000/docs
```

## 🌐 API Endpoints

### Projets
- `POST /api/v1/create-startup` - Créer un projet
- `GET /api/v1/projects` - Lister les projets
- `GET /api/v1/projects/{id}` - Détails d'un projet
- `GET /api/v1/projects/{id}/download` - Télécharger le code

### WebSocket
- `WS /ws/logs/{project_id}` - Logs en temps réel

### Santé
- `GET /health` - Vérification de l'état

## 📊 Modèles de Données

### Project
```python
{
  "id": "uuid",
  "idea": "Description de l'idée",
  "roadmap": {"phase1": "MVP", "phase2": "Beta"},
  "stack": {"frontend": "React", "backend": "FastAPI"},
  "created_at": "2024-01-01T00:00:00Z",
  "path": "/generated/uuid"
}
```

### Log
```python
{
  "id": "uuid",
  "project_id": "uuid",
  "message": "Message du log",
  "timestamp": "2024-01-01T00:00:00Z"
}
```

## 🎨 Interface Utilisateur

### Dashboard Startups
- Table responsive avec hover effects
- Boutons d'action (Voir détails, Télécharger)
- Modal pour afficher roadmap et stack
- Formatage des dates en français

### Composant Logs
- Connexion WebSocket automatique
- Affichage en temps réel des logs
- Contrôles de navigation (haut/bas)
- Auto-scroll configurable
- Indicateur de statut de connexion

## 🔧 Configuration

### Variables d'Environnement Backend
```bash
DATABASE_URL=postgresql+asyncpg://admin:secret@db:5432/appdb
SECRET_KEY=your-secret-key-here
```

### Variables d'Environnement Frontend
```bash
REACT_APP_API_URL=http://localhost:8000/api/v1
REACT_APP_WS_URL=ws://localhost:8000
```

## 📝 Utilisation

### 1. Créer une Startup
```bash
curl -X POST "http://localhost:8000/api/v1/create-startup" \
  -H "Content-Type: application/json" \
  -d '{"idea": "SaaS marketplace"}'
```

### 2. Consulter les Projets
- Ouvrir `http://localhost:3000`
- Naviguer vers le dashboard Startups
- Voir la liste des projets créés

### 3. Télécharger un Projet
- Cliquer sur "Télécharger" dans le dashboard
- Le fichier ZIP sera téléchargé automatiquement

### 4. Suivre les Logs
- Utiliser le composant Logs avec un project_id
- Les logs s'affichent en temps réel via WebSocket

## 🛠️ Développement

### Backend
```bash
cd core-engine

# Installer les dépendances
pip install -r requirements.txt

# Lancer en mode développement
uvicorn main:app --reload

# Migrations
alembic upgrade head
```

### Frontend
```bash
cd frontend

# Installer les dépendances
npm install

# Lancer en mode développement
npm start

# Build de production
npm run build
```

## 🧪 Tests

### Tests API
```bash
cd core-engine
python test_api.py
```

### Tests Frontend
```bash
cd frontend
npm test
```

## 📚 Documentation

- **API**: http://localhost:8000/docs (Swagger UI)
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

## 🚨 Dépannage

### Problèmes Courants

1. **Base de données non accessible**
   ```bash
   docker-compose logs db
   docker-compose restart db
   ```

2. **WebSocket non connecté**
   - Vérifier l'URL WebSocket
   - Contrôler les CORS

3. **Erreurs de migration**
   ```bash
   docker-compose down -v
   docker-compose up --build
   ```

### Logs
```bash
# Backend
docker-compose logs -f app

# Base de données
docker-compose logs -f db

# Frontend
npm start
```

## 🔮 Roadmap

- [ ] Authentification JWT
- [ ] Gestion des rôles utilisateurs
- [ ] API de génération de code
- [ ] Intégration CI/CD
- [ ] Monitoring et métriques
- [ ] Tests automatisés
- [ ] Documentation utilisateur

## 🤝 Contribution

1. Fork le projet
2. Créer une branche feature
3. Commit les changements
4. Push vers la branche
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est sous licence MIT.

## 🆘 Support

- **Issues**: GitHub Issues
- **Documentation**: README et /docs
- **API**: Swagger UI sur /docs

---

**Epic6** - Transformez vos idées en startups fonctionnelles 🚀
