# Epic6 Core Engine

Backend FastAPI pour la gestion des projets startup avec persistance PostgreSQL et WebSockets.

## 🚀 Fonctionnalités

- **Gestion des projets startup** avec persistance en base de données
- **API REST** complète pour les opérations CRUD
- **WebSockets** pour les logs en temps réel
- **Téléchargement ZIP** des projets générés
- **Logs persistants** avec niveaux (INFO, WARNING, ERROR, DEBUG)
- **Base de données PostgreSQL** avec migrations Alembic

## 🏗️ Architecture

```
core-engine/
├── api/                 # Routes et schémas API
├── core/               # Configuration et base de données
├── models/             # Modèles SQLAlchemy
├── utils/              # Utilitaires (logger)
├── generated/          # Code généré des projets
├── alembic/            # Migrations de base de données
├── main.py             # Point d'entrée FastAPI
├── requirements.txt    # Dépendances Python
├── docker-compose.yml  # Configuration Docker
└── Dockerfile         # Image Docker
```

## 📋 Prérequis

- Docker et Docker Compose
- Python 3.11+ (pour le développement local)
- PostgreSQL 15+

## 🚀 Démarrage rapide

### Avec Docker (recommandé)

```bash
# Cloner le projet
git clone <repository-url>
cd core-engine

# Démarrer l'application
./start.sh
```

### Démarrage manuel

```bash
# Démarrer PostgreSQL
docker-compose up db -d

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## 🌐 API Endpoints

### Projets

- `POST /api/v1/create-startup` - Créer un nouveau projet
- `GET /api/v1/projects` - Lister tous les projets
- `GET /api/v1/projects/{id}` - Détails d'un projet
- `GET /api/v1/projects/{id}/download` - Télécharger le code généré

### WebSocket

- `WS /ws/logs/{project_id}` - Connexion WebSocket pour les logs

### Santé

- `GET /health` - Vérification de l'état de l'application

## 📊 Modèles de données

### Project

```python
class Project(Base):
    id: UUID (primary key)
    idea: str (idée du projet)
    roadmap: JSON (roadmap du projet)
    stack: JSON (stack technique)
    created_at: datetime (date de création)
    path: str (chemin du code généré)
```

### Log

```python
class Log(Base):
    id: UUID (primary key)
    project_id: UUID (référence au projet)
    message: str (message du log)
    timestamp: datetime (horodatage)
```

## 🔌 Configuration

### Variables d'environnement

```bash
DATABASE_URL=postgresql+asyncpg://admin:secret@db:5432/appdb
SYNC_DATABASE_URL=postgresql://admin:secret@db:5432/appdb
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Base de données

- **Host**: localhost (ou `db` en Docker)
- **Port**: 5432
- **Database**: appdb
- **Username**: admin
- **Password**: secret

## 📝 Utilisation

### 1. Créer un projet startup

```bash
curl -X POST "http://localhost:8000/api/v1/create-startup" \
  -H "Content-Type: application/json" \
  -d '{
    "idea": "SaaS marketplace pour freelances",
    "roadmap": {"phase1": "MVP", "phase2": "Beta"},
    "stack": {"frontend": "React", "backend": "Node.js"}
  }'
```

### 2. Lister les projets

```bash
curl "http://localhost:8000/api/v1/projects"
```

### 3. Télécharger un projet

```bash
curl "http://localhost:8000/api/v1/projects/{id}/download" \
  -o "project.zip"
```

### 4. Connexion WebSocket pour les logs

```javascript
const ws = new WebSocket(`ws://localhost:8000/ws/logs/${projectId}`);

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log('Nouveau log:', data);
};
```

## 🎨 Frontend React

### Composant Startups

```jsx
import Startups from './components/Startups';

// Affiche la table des projets avec actions
<Startups />
```

### Composant Logs

```jsx
import Logs from './components/Logs';

// Affiche les logs en temps réel pour un projet
<Logs projectId={projectId} />
```

## 🛠️ Développement

### Migrations de base de données

```bash
# Créer une nouvelle migration
alembic revision --autogenerate -m "Description"

# Appliquer les migrations
alembic upgrade head

# Revenir en arrière
alembic downgrade -1
```

### Tests

```bash
# Lancer les tests
pytest

# Avec couverture
pytest --cov=.
```

### Linting

```bash
# Black (formatage)
black .

# Flake8 (linting)
flake8 .
```

## 📁 Structure des fichiers générés

```
generated/
├── {project_id}/
│   ├── src/
│   ├── docs/
│   ├── tests/
│   └── README.md
```

## 🔍 Monitoring

### Logs de l'application

```bash
# Voir les logs en temps réel
docker-compose logs -f app

# Logs de la base de données
docker-compose logs -f db
```

### Métriques

- Endpoint `/health` pour la santé de l'application
- Logs structurés avec niveaux
- WebSocket pour monitoring en temps réel

## 🚨 Dépannage

### Problèmes courants

1. **Base de données non accessible**
   - Vérifier que PostgreSQL est démarré
   - Contrôler les variables d'environnement

2. **Erreurs de migration**
   - Supprimer le volume PostgreSQL et redémarrer
   - Vérifier la configuration Alembic

3. **WebSocket non connecté**
   - Vérifier l'URL WebSocket
   - Contrôler les CORS

### Logs d'erreur

```bash
# Logs détaillés
docker-compose logs app | grep ERROR

# Logs de la base de données
docker-compose logs db | grep ERROR
```

## 📚 Documentation

- **API**: http://localhost:8000/docs (Swagger UI)
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI**: http://localhost:8000/openapi.json

## 🤝 Contribution

1. Fork le projet
2. Créer une branche feature
3. Commit les changements
4. Push vers la branche
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## 🆘 Support

Pour toute question ou problème :

- Ouvrir une issue sur GitHub
- Consulter la documentation API
- Vérifier les logs de l'application