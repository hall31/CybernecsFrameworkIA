#!/usr/bin/env python3
"""
🚀 API de démonstration pour le Dashboard d'Orchestration
Lancez ce fichier pour tester le dashboard avec une API réelle
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI(title="Orchestration API", version="1.0.0")

# Configuration CORS pour le dashboard
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    Agent(name="Agent-003", enabled=True, status="error"),
    Agent(name="Agent-004", enabled=True, status="active"),
    Agent(name="Agent-005", enabled=False, status="disabled")
]

epics_db = [
    Epic(id="epic-001", name="Création de la base de données", enabled=True, status="done"),
    Epic(id="epic-002", name="Développement de l'API", enabled=True, status="running"),
    Epic(id="epic-003", name="Tests d'intégration", enabled=False, status="disabled"),
    Epic(id="epic-004", name="Déploiement en production", enabled=True, status="pending"),
    Epic(id="epic-005", name="Monitoring et alertes", enabled=True, status="failed"),
    Epic(id="epic-006", name="Documentation utilisateur", enabled=True, status="done")
]

@app.get("/")
async def root():
    return {
        "message": "🚀 API d'Orchestration pour Startup Factory",
        "endpoints": {
            "agents": "/agents",
            "epics": "/epics",
            "docs": "/docs"
        }
    }

@app.get("/agents", response_model=List[Agent])
async def get_agents():
    """Récupère la liste des agents"""
    return agents_db

@app.post("/agents/{name}/toggle")
async def toggle_agent(name: str):
    """Active ou désactive un agent"""
    for agent in agents_db:
        if agent.name == name:
            agent.enabled = not agent.enabled
            agent.status = "active" if agent.enabled else "disabled"
            return {
                "success": True, 
                "message": f"Agent {name} toggled successfully", 
                "agent": agent
            }
    raise HTTPException(status_code=404, detail="Agent not found")

@app.get("/epics", response_model=List[Epic])
async def get_epics():
    """Récupère la liste des épics"""
    return epics_db

@app.post("/epics/{epic_id}/toggle")
async def toggle_epic(epic_id: str):
    """Active ou désactive un épic"""
    for epic in epics_db:
        if epic.id == epic_id:
            epic.enabled = not epic.enabled
            epic.status = "pending" if epic.enabled else "disabled"
            return {
                "success": True, 
                "message": f"Epic {epic_id} toggled successfully", 
                "epic": epic
            }
    raise HTTPException(status_code=404, detail="Epic not found")

@app.post("/epics/{epic_id}/run")
async def run_epic(epic_id: str):
    """Exécute un épic"""
    for epic in epics_db:
        if epic.id == epic_id:
            if not epic.enabled:
                raise HTTPException(status_code=400, detail="Epic is disabled")
            epic.status = "running"
            return {
                "success": True, 
                "message": f"Epic {epic_id} started successfully", 
                "epic": epic
            }
    raise HTTPException(status_code=404, detail="Epic not found")

@app.get("/health")
async def health_check():
    """Vérification de la santé de l'API"""
    return {
        "status": "healthy",
        "agents_count": len(agents_db),
        "epics_count": len(epics_db),
        "timestamp": "2024-01-01T00:00:00Z"
    }

if __name__ == "__main__":
    print("🚀 Démarrage de l'API d'Orchestration...")
    print("📍 Dashboard: http://localhost:5173")
    print("🔌 API: http://localhost:8000")
    print("📚 Documentation: http://localhost:8000/docs")
    print("💚 Health Check: http://localhost:8000/health")
    print("\nAppuyez sur Ctrl+C pour arrêter\n")
    
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8000,
        reload=True
    )