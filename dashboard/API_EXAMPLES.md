# 🔌 Exemples d'API pour le Dashboard d'Orchestration

## 📋 Endpoints Requis

### 1. Agents

#### GET /agents
Récupère la liste des agents

**Response:**
```json
[
  {
    "name": "Agent-001",
    "enabled": true,
    "status": "active"
  },
  {
    "name": "Agent-002",
    "enabled": false,
    "status": "disabled"
  },
  {
    "name": "Agent-003",
    "enabled": true,
    "status": "error"
  }
]
```

#### POST /agents/{name}/toggle
Active ou désactive un agent

**Request:**
```bash
POST /agents/Agent-001/toggle
```

**Response:**
```json
{
  "success": true,
  "message": "Agent Agent-001 toggled successfully",
  "agent": {
    "name": "Agent-001",
    "enabled": false,
    "status": "disabled"
  }
}
```

### 2. Épics

#### GET /epics
Récupère la liste des épics

**Response:**
```json
[
  {
    "id": "epic-001",
    "name": "Création de la base de données",
    "enabled": true,
    "status": "done"
  },
  {
    "id": "epic-002",
    "name": "Développement de l'API",
    "enabled": true,
    "status": "running"
  },
  {
    "id": "epic-003",
    "name": "Tests d'intégration",
    "enabled": false,
    "status": "disabled"
  }
]
```

#### POST /epics/{id}/toggle
Active ou désactive un épic

**Request:**
```bash
POST /epics/epic-001/toggle
```

**Response:**
```json
{
  "success": true,
  "message": "Epic epic-001 toggled successfully",
  "epic": {
    "id": "epic-001",
    "name": "Création de la base de données",
    "enabled": false,
    "status": "disabled"
  }
}
```

#### POST /epics/{id}/run
Exécute un épic

**Request:**
```bash
POST /epics/epic-001/run
```

**Response:**
```json
{
  "success": true,
  "message": "Epic epic-001 started successfully",
  "epic": {
    "id": "epic-001",
    "name": "Création de la base de données",
    "enabled": true,
    "status": "running"
  }
}
```

## 🚀 Exemples d'Implémentation

### Python (FastAPI)

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid

app = FastAPI()

# Modèles de données
class Agent(BaseModel):
    name: str
    enabled: bool
    status: str

class Epic(BaseModel):
    id: str
    name: str
    enabled: bool
    status: str

# Base de données simulée
agents_db = [
    Agent(name="Agent-001", enabled=True, status="active"),
    Agent(name="Agent-002", enabled=False, status="disabled"),
    Agent(name="Agent-003", enabled=True, status="error")
]

epics_db = [
    Epic(id="epic-001", name="Création de la base de données", enabled=True, status="done"),
    Epic(id="epic-002", name="Développement de l'API", enabled=True, status="running"),
    Epic(id="epic-003", name="Tests d'intégration", enabled=False, status="disabled")
]

@app.get("/agents", response_model=List[Agent])
async def get_agents():
    return agents_db

@app.post("/agents/{name}/toggle")
async def toggle_agent(name: str):
    for agent in agents_db:
        if agent.name == name:
            agent.enabled = not agent.enabled
            agent.status = "active" if agent.enabled else "disabled"
            return {"success": True, "message": f"Agent {name} toggled successfully", "agent": agent}
    raise HTTPException(status_code=404, detail="Agent not found")

@app.get("/epics", response_model=List[Epic])
async def get_epics():
    return epics_db

@app.post("/epics/{epic_id}/toggle")
async def toggle_epic(epic_id: str):
    for epic in epics_db:
        if epic.id == epic_id:
            epic.enabled = not epic.enabled
            epic.status = "pending" if epic.enabled else "disabled"
            return {"success": True, "message": f"Epic {epic_id} toggled successfully", "epic": epic}
    raise HTTPException(status_code=404, detail="Epic not found")

@app.post("/epics/{epic_id}/run")
async def run_epic(epic_id: str):
    for epic in epics_db:
        if epic.id == epic_id:
            if not epic.enabled:
                raise HTTPException(status_code=400, detail="Epic is disabled")
            epic.status = "running"
            return {"success": True, "message": f"Epic {epic_id} started successfully", "epic": epic}
    raise HTTPException(status_code=404, detail="Epic not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Node.js (Express)

```javascript
const express = require('express');
const app = express();
const port = 8000;

app.use(express.json());

// Base de données simulée
let agents = [
  { name: "Agent-001", enabled: true, status: "active" },
  { name: "Agent-002", enabled: false, status: "disabled" },
  { name: "Agent-003", enabled: true, status: "error" }
];

let epics = [
  { id: "epic-001", name: "Création de la base de données", enabled: true, status: "done" },
  { id: "epic-002", name: "Développement de l'API", enabled: true, status: "running" },
  { id: "epic-003", name: "Tests d'intégration", enabled: false, status: "disabled" }
];

// GET /agents
app.get('/agents', (req, res) => {
  res.json(agents);
});

// POST /agents/:name/toggle
app.post('/agents/:name/toggle', (req, res) => {
  const { name } = req.params;
  const agent = agents.find(a => a.name === name);
  
  if (!agent) {
    return res.status(404).json({ error: "Agent not found" });
  }
  
  agent.enabled = !agent.enabled;
  agent.status = agent.enabled ? "active" : "disabled";
  
  res.json({
    success: true,
    message: `Agent ${name} toggled successfully`,
    agent
  });
});

// GET /epics
app.get('/epics', (req, res) => {
  res.json(epics);
});

// POST /epics/:id/toggle
app.post('/epics/:id/toggle', (req, res) => {
  const { id } = req.params;
  const epic = epics.find(e => e.id === id);
  
  if (!epic) {
    return res.status(404).json({ error: "Epic not found" });
  }
  
  epic.enabled = !epic.enabled;
  epic.status = epic.enabled ? "pending" : "disabled";
  
  res.json({
    success: true,
    message: `Epic ${id} toggled successfully`,
    epic
  });
});

// POST /epics/:id/run
app.post('/epics/:id/run', (req, res) => {
  const { id } = req.params;
  const epic = epics.find(e => e.id === id);
  
  if (!epic) {
    return res.status(404).json({ error: "Epic not found" });
  }
  
  if (!epic.enabled) {
    return res.status(400).json({ error: "Epic is disabled" });
  }
  
  epic.status = "running";
  
  res.json({
    success: true,
    message: `Epic ${id} started successfully`,
    epic
  });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
```

## 🔧 Configuration CORS

Pour permettre au dashboard de communiquer avec votre API :

```python
# FastAPI
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # URL du dashboard
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

```javascript
// Express
const cors = require('cors');

app.use(cors({
  origin: 'http://localhost:5173',  // URL du dashboard
  credentials: true
}));
```

## 📊 Statuts Supportés

### Agents
- `active` : Agent actif et fonctionnel
- `disabled` : Agent désactivé
- `error` : Agent en erreur

### Épics
- `running` : Épic en cours d'exécution
- `done` : Épic terminé avec succès
- `pending` : Épic en attente
- `failed` : Épic en échec
- `disabled` : Épic désactivé

## 🚀 Démarrage Rapide

1. **Installez les dépendances :**
   ```bash
   # Python
   pip install fastapi uvicorn
   
   # Node.js
   npm install express cors
   ```

2. **Lancez l'API :**
   ```bash
   # Python
   python api.py
   
   # Node.js
   node api.js
   ```

3. **Testez les endpoints :**
   ```bash
   curl http://localhost:8000/agents
   curl http://localhost:8000/epics
   ```

4. **Le dashboard se connectera automatiquement !**

---

**Prêt pour la production ! 🚀**