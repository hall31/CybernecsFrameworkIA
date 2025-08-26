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