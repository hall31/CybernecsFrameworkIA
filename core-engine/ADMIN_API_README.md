# 🚀 API Admin FastAPI - Orchestration des Agents & Épics

Cette API FastAPI permet de gérer l'orchestration des agents et des épics depuis le dashboard React.

## 📋 Fonctionnalités

### 🤖 Gestion des Agents
- **GET** `/agents` - Liste tous les agents avec leur état
- **GET** `/agents/{name}` - Récupère un agent spécifique
- **POST** `/agents/{name}/toggle` - Active/désactive un agent
- **POST** `/agents/{name}/enable` - Active un agent
- **POST** `/agents/{name}/disable` - Désactive un agent

### 📋 Gestion des Épics
- **GET** `/epics` - Liste toutes les épics avec leur état
- **GET** `/epics/{eid}` - Récupère une épic spécifique
- **POST** `/epics/{eid}/toggle` - Active/désactive tous les agents d'une épic
- **POST** `/epics/{eid}/enable` - Active tous les agents d'une épic
- **POST** `/epics/{eid}/disable` - Désactive tous les agents d'une épic
- **POST** `/epics/{eid}/run` - Exécute une épic (simulation)
- **POST** `/epics/{eid}/reset` - Remet une épic en statut 'idle'

### 🔧 Utilitaires
- **GET** `/` - Point d'entrée avec documentation
- **GET** `/health` - Vérification de l'état de l'API
- **GET** `/status` - Statut global du système
- **POST** `/reset` - Réinitialise tous les statuts d'épics

## 🚀 Installation et Lancement

### 1. Installer les dépendances
```bash
cd core-engine
pip install -r requirements.txt
```

### 2. Lancer l'API
```bash
# Option 1: Script de lancement
python run_admin_api.py

# Option 2: Directement avec uvicorn
uvicorn admin_api:app --reload --port 8000

# Option 3: Depuis le fichier principal
python admin_api.py
```

### 3. Accéder à la documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **API**: http://localhost:8000

## 🧪 Tests

### Lancer les tests
```bash
python test_admin_api.py
```

### Tests disponibles
- ✅ Vérification de la santé de l'API
- ✅ Récupération des agents et épics
- ✅ Test du toggle des agents
- ✅ Vérification du statut système

## 📊 Structure des Données

### Agent
```json
{
  "name": "CEOAgent",
  "enabled": true,
  "status": "active",
  "type": "agent"
}
```

### Épic
```json
{
  "id": "epic1",
  "name": "epic1",
  "agents": ["CEOAgent"],
  "enabled": true,
  "status": "idle",
  "type": "epic"
}
```

### Statut Système
```json
{
  "system_status": "operational",
  "agents": {
    "total": 8,
    "active": 5,
    "disabled": 3
  },
  "epics": {
    "total": 5,
    "idle": 4,
    "running": 0,
    "done": 1
  },
  "timestamp": 1703123456.789
}
```

## 🔌 Intégration Frontend

### Configuration CORS
L'API est configurée pour accepter les requêtes depuis :
- `http://localhost:3000` (React dev server)
- `http://localhost:5173` (Vite dev server)
- Toutes les origines en développement (`*`)

### Exemple d'utilisation avec fetch
```javascript
// Récupérer tous les agents
const agents = await fetch('http://localhost:8000/agents')
  .then(res => res.json());

// Toggle un agent
const result = await fetch('http://localhost:8000/agents/CEOAgent/toggle', {
  method: 'POST'
}).then(res => res.json());

// Exécuter une épic
const epicResult = await fetch('http://localhost:8000/epics/epic1/run', {
  method: 'POST'
}).then(res => res.json());
```

## 📁 Structure des Fichiers

```
core-engine/
├── admin_api.py          # API FastAPI principale
├── config.py             # Configuration des agents et épics
├── run_admin_api.py      # Script de lancement
├── test_admin_api.py     # Tests de l'API
├── requirements.txt      # Dépendances Python
├── utils/
│   └── logger.py        # Système de logging
└── agents/              # Dossier des agents
```

## 🎯 Configuration

### Agents disponibles
- `CEOAgent` - Agent CEO (activé par défaut)
- `CTOAgent` - Agent CTO (activé par défaut)
- `DevBackendAgent` - Agent Développement Backend (activé par défaut)
- `DevFrontendAgent` - Agent Développement Frontend (activé par défaut)
- `MarketingAgent` - Agent Marketing (activé par défaut)
- `FinanceAgent` - Agent Finance (désactivé par défaut)
- `LegalAgent` - Agent Légal (désactivé par défaut)
- `GrowthAgent` - Agent Croissance (désactivé par défaut)

### Épics disponibles
- `epic1` - CEO uniquement
- `epic2` - CTO uniquement
- `epic3` - Dev Backend + Frontend
- `epic4` - Marketing uniquement
- `epic7` - Finance + Légal + Croissance

## 🚨 Gestion des Erreurs

L'API inclut une gestion d'erreurs complète :
- **404** - Ressource non trouvée
- **400** - Requête invalide
- **500** - Erreur interne du serveur

Toutes les erreurs sont loggées avec des messages détaillés.

## 🔄 Logs

L'API utilise le système de logging existant avec des niveaux :
- **INFO** - Informations générales
- **SUCCESS** - Actions réussies
- **WARNING** - Avertissements
- **ERROR** - Erreurs

## 🎉 Prêt pour l'Orchestration !

Ton backend FastAPI est maintenant prêt à être connecté à ton Dashboard React ! 🚀

- **Port**: 8000
- **CORS**: Configuré pour React
- **Documentation**: Automatique avec Swagger
- **Tests**: Scripts de test inclus
- **Logs**: Système de logging coloré