# 🚀 Epic 15: Startup Tokenization Marketplace

## 📋 Vue d'ensemble

L'Epic 15 implémente un système complet de marketplace pour l'échange de tokens de startups. Cette fonctionnalité permet aux investisseurs d'acheter et de vendre des parts tokenisées de startups sur un exchange interne sécurisé.

## 🏗️ Architecture

### Core Engine (`/core-engine`)

```
core-engine/
├── agents/
│   ├── __init__.py
│   └── market_agent.py          # Agent principal du marketplace
├── contracts/                   # Smart contracts (futur)
├── utils/                       # Utilitaires
├── main.py                      # API Flask principale
└── requirements.txt             # Dépendances Python
```

### Dashboard React (`/dashboard`)

- **Page Global Market**: Interface complète du marketplace
- **Graphiques interactifs**: Prix, volumes, répartition portefeuille
- **Tableau des tokens**: Liste des startups avec actions Acheter/Vendre

## 🔧 Composants Techniques

### 1. MarketAgent (`market_agent.py`)

**Responsabilités :**
- Gestion du marketplace des startups tokenisées
- Listing automatique des tokens sur l'exchange
- Création de smart contracts marketplace
- Génération de données de marché simulées

**Méthodes principales :**
- `run()`: Point d'entrée principal
- `get_tokenised_startups()`: Récupération des startups
- `list_startup_on_exchange()`: Listing sur l'exchange
- `create_marketplace_contract()`: Création du smart contract
- `generate_price_history()`: Historique des prix
- `get_market_stats()`: Statistiques globales

**Données simulées :**
- 5 startups tokenisées (TechFlow, GreenEnergy, HealthTech, FinTech, AI Dynamics)
- Prix basés sur valuation + volatilité
- Volumes d'échange aléatoires
- Variations de prix 24h

### 2. API Flask (`main.py`)

**Endpoints :**
- `GET /market` - Données complètes du marketplace
- `GET /market/token/<symbol>` - Détails d'un token
- `GET /market/stats` - Statistiques globales
- `GET /market/orderbook/<symbol>` - Order book d'un token
- `GET /market/price-history/<symbol>` - Historique des prix

**Fonctionnalités :**
- Gestion d'erreurs robuste
- Logging détaillé
- CORS activé pour le dashboard
- Réponses JSON standardisées

### 3. Dashboard Global Market

**Interface inspirée Nasdaq/Binance :**
- Header premium avec gradient bleu/violet
- Tableau des tokens avec actions Acheter/Vendre
- Panneau de détails du token sélectionné
- Graphiques interactifs (Recharts)
- Statistiques en temps réel

**Composants visuels :**
- 📊 Tableau des startups tokenisées
- 📈 Graphique d'évolution des prix (7j/30j)
- 📊 Graphique des volumes par startup
- 🥧 Répartition du portefeuille (Pie chart)
- 🎨 Icônes sectorielles et badges de stage

## 🚀 Démarrage Rapide

### 1. Backend Python

```bash
cd core-engine
pip install -r requirements.txt
python main.py
```

**API accessible sur :** `http://localhost:5000`

### 2. Dashboard React

```bash
cd dashboard
npm install
npm run dev
```

**Dashboard accessible sur :** `http://localhost:5173`

## 📊 Données du Marketplace

### Startups Simulées

| Symbol | Nom | Secteur | Stage | Valuation | Prix Token |
|--------|-----|---------|-------|-----------|------------|
| STK001 | TechFlow Solutions | SaaS | Series A | 2.5M € | 2.50 € |
| STK002 | GreenEnergy Corp | CleanTech | Seed | 1.8M € | 0.90 € |
| STK003 | HealthTech Innovations | HealthTech | Series B | 3.2M € | 2.13 € |
| STK004 | FinTech Revolution | FinTech | Series A | 4.5M € | 1.50 € |
| STK005 | AI Dynamics | AI | Seed | 2.8M € | 3.50 € |

### Statistiques Globales

- **Total Tokens Listés :** 5
- **Market Cap Total :** 14.8M €
- **Volume 24h :** Variable (simulé)
- **Sentiment :** Bullish/Neutral

## 🔮 Fonctionnalités Futures

### Smart Contracts
- Intégration Ethereum/Polygon
- Achat/Vente automatisés
- Gestion de la liquidité
- Settlement automatique

### Trading Avancé
- Order book en temps réel
- Stop-loss et take-profit
- Trading algorithmique
- Notifications de prix

### Analytics
- Indicateurs techniques
- Analyse fondamentale
- Comparaison sectorielle
- Prédictions IA

## 🧪 Tests

### Test du MarketAgent

```bash
cd core-engine
python -c "
from agents.market_agent import MarketAgent
agent = MarketAgent()
result = agent.run()
print('Marketplace initialisé avec succès!')
print(f'Tokens listés: {len(result[\"listed_tokens\"])}')
"
```

### Test de l'API

```bash
# Test de santé
curl http://localhost:5000/health

# Récupération du marché
curl http://localhost:5000/market

# Détails d'un token
curl http://localhost:5000/market/token/STK001
=======
Backend FastAPI pour la gestion des projets startup avec persistance PostgreSQL et WebSockets.

## 🚀 Fonctionnalités

- **Gestion des projets startup** avec persistance en base de données
- **API REST** complète pour les opérations CRUD
- **WebSockets** pour les logs en temps réel
- **Téléchargement ZIP** des projets générés
- **Logs persistants** avec niveaux (INFO, WARNING, ERROR, DEBUG)
- **Base de données PostgreSQL** avec migrations Alembic
# 🧩 Core Engine - Startup Orchestrator

Un moteur d'orchestration intelligent pour startups avec un agent CEO qui génère des roadmaps complètes.

## 🚀 Fonctionnalités

- **API FastAPI** avec endpoint POST `/create-startup`
- **Agent CEO** qui analyse les idées et génère des roadmaps
- **Roadmaps structurées** avec epics, user stories, timeline et métriques
- **Logging coloré** pour le suivi des événements
- **Dockerisation** complète avec docker-compose

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


├── main.py              # Application FastAPI principale
├── agents/
│   └── ceo_agent.py    # Agent CEO intelligent
├── utils/
│   └── logger.py       # Système de logging
├── requirements.txt     # Dépendances Python
├── Dockerfile          # Configuration Docker
├── docker-compose.yml  # Orchestration des services
└── README.md           # Documentation
```

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

# Cloner et naviguer vers le projet
cd core-engine

# Lancer avec Docker Compose
docker-compose up --build

# L'API sera disponible sur http://localhost:8000
```

### Sans Docker

```bash
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

python main.py
```

## 📡 API Endpoints

### POST /create-startup

Génère une roadmap complète pour une idée de startup.

**Request:**
```json
{
  "idea": "SaaS marketplace"
}
```

**Response:**
```json
{
  "roadmap": {
    "startup_idea": "SaaS marketplace",
    "vision": "To revolutionize the SaaS marketplace market...",
    "epics": [...],
    "timeline": {...},
    "success_metrics": [...],
    "risks": [...],
    "next_steps": [...]
  },
  "message": "Roadmap generated successfully for: SaaS marketplace"
}
```

## 🧠 Agent CEO

L'agent CEO analyse l'idée de startup et génère :

- **Vision** : Énoncé de vision stratégique
- **Epics** : Grandes fonctionnalités avec user stories
- **Timeline** : Phases de développement (4-6 mois)
- **Métriques** : KPIs de succès
- **Risques** : Évaluation et mitigation des risques
- **Prochaines étapes** : Actions immédiates

## 🔧 Configuration

### Variables d'environnement

- `PYTHONPATH=/app` : Chemin Python dans le container
- `PYTHONUNBUFFERED=1` : Sortie Python non bufferisée

### Ports

- **8000** : API FastAPI

## 📊 Exemple d'utilisation

```bash
# Test de l'API
curl -X POST "http://localhost:8000/create-startup" \
     -H "Content-Type: application/json" \
     -d '{"idea": "SaaS marketplace"}'
```

## 🐳 Docker

### Build de l'image

```bash
docker build -t core-engine .
```

### Lancer le container

```bash
docker run -p 8000:8000 core-engine
```

### Docker Compose

```bash
# Lancer tous les services
docker-compose up

# Lancer en arrière-plan
docker-compose up -d

# Arrêter les services
docker-compose down
```

## 📝 Logs

Le système génère des logs détaillés pour :
- Initialisation du marketplace
- Listing des startups
- Création des smart contracts
- Erreurs et exceptions
- Activité des utilisateurs

## 🔒 Sécurité

- Validation des données d'entrée
- Gestion d'erreurs robuste
- Logs de sécurité
- CORS configuré
- Rate limiting (futur)

## 📈 Métriques

- Performance de l'API
- Temps de réponse
- Taux d'erreur
- Utilisation des ressources
- Activité des utilisateurs

---

**🎯 Epic 15 - Marketplace des Startups Tokenisées**  
*Développé avec ❤️ pour la révolution de la finance décentralisée*

Les logs sont affichés dans la console avec un format coloré :

```
[2024-01-15 10:30:00] INFO     | main             | Received startup idea: SaaS marketplace
[2024-01-15 10:30:00] INFO     | CEO Agent        | Initialized
[2024-01-15 10:30:00] INFO     | CEO Agent        | Analyzing idea: SaaS marketplace
[2024-01-15 10:30:00] INFO     | CEO Agent        | Roadmap generated with 4 epics
[2024-01-15 10:30:00] INFO     | main             | Generated roadmap for: SaaS marketplace
```

## 🧪 Tests

```bash
# Test de santé
curl http://localhost:8000/

# Test de création de startup
curl -X POST "http://localhost:8000/create-startup" \
     -H "Content-Type: application/json" \
     -d '{"idea": "Test startup"}'
```

## 🔮 Roadmap future

- [ ] Intégration avec des modèles d'IA avancés
- [ ] Base de données pour persistance des roadmaps
- [ ] Interface web pour visualisation
- [ ] API pour mise à jour des roadmaps
- [ ] Intégration avec des outils de gestion de projet

## 📄 Licence

MIT License - Voir le fichier LICENSE pour plus de détails.
