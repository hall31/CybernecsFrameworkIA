"""
Exemple de backend Python avec FastAPI pour le dashboard ShipFast
Implémente les endpoints WebSocket et API requis
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
import json
import asyncio
from datetime import datetime
import uuid

# Configuration de l'application
app = FastAPI(
    title="ShipFast Core Engine",
    description="Backend pour le dashboard ShipFast avec WebSocket et API",
    version="1.0.0"
)

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Dashboard URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modèles de données
class StartupIdea(BaseModel):
    idea: str

class Startup(BaseModel):
    id: int
    idea: str
    created_at: str
    status: str
    estimated_hours: int

class LogEvent(BaseModel):
    timestamp: str
    message: str
    level: str = "info"

# Stockage en mémoire (remplacer par une vraie base de données)
startups_db = []
websocket_connections: List[WebSocket] = []

# Fonction pour envoyer des logs à tous les clients WebSocket connectés
async def broadcast_log(message: str, level: str = "info"):
    """Envoie un log à tous les clients WebSocket connectés"""
    log_event = LogEvent(
        timestamp=datetime.now().isoformat(),
        message=message,
        level=level
    )
    
    # Envoyer à tous les clients connectés
    for connection in websocket_connections:
        try:
            await connection.send_text(log_event.json())
        except:
            # Supprimer les connexions défaillantes
            websocket_connections.remove(connection)

# Endpoint WebSocket pour les logs
@app.websocket("/ws/logs")
async def websocket_logs(websocket: WebSocket):
    await websocket.accept()
    websocket_connections.append(websocket)
    
    try:
        # Envoyer un message de bienvenue
        await broadcast_log("Nouveau client connecté au stream de logs", "info")
        
        # Garder la connexion active
        while True:
            # Attendre des messages du client (optionnel)
            data = await websocket.receive_text()
            # Traiter les messages si nécessaire
            
    except WebSocketDisconnect:
        websocket_connections.remove(websocket)
        await broadcast_log("Client déconnecté du stream de logs", "info")

# Endpoint pour créer une startup
@app.post("/create-startup")
async def create_startup(startup_idea: StartupIdea):
    """Crée une nouvelle startup avec génération de roadmap"""
    try:
        # Simuler la génération de roadmap par l'IA CEO Agent
        startup_id = len(startups_db) + 1
        
        # Log de l'événement
        await broadcast_log(f"Génération de startup: {startup_idea.idea[:50]}...", "info")
        
        # Simuler le processus de génération
        await asyncio.sleep(2)  # Simulation du traitement IA
        
        # Créer la startup
        new_startup = Startup(
            id=startup_id,
            idea=startup_idea.idea,
            created_at=datetime.now().isoformat(),
            status="completed",
            estimated_hours=120  # Estimation simulée
        )
        
        startups_db.append(new_startup)
        
        # Log de succès
        await broadcast_log(f"Startup #{startup_id} générée avec succès!", "success")
        
        return {
            "success": True,
            "startup_id": startup_id,
            "message": "Startup générée avec succès"
        }
        
    except Exception as e:
        await broadcast_log(f"Erreur lors de la génération: {str(e)}", "error")
        raise HTTPException(status_code=500, detail="Erreur lors de la génération")

# Endpoint pour récupérer la liste des projets
@app.get("/projects", response_model=List[Startup])
async def get_projects():
    """Récupère la liste de toutes les startups"""
    return startups_db

# Endpoint pour télécharger une startup
@app.get("/download-startup/{startup_id}")
async def download_startup(startup_id: int):
    """Télécharge une startup au format ZIP"""
    # Trouver la startup
    startup = next((s for s in startups_db if s.id == startup_id), None)
    
    if not startup:
        raise HTTPException(status_code=404, detail="Startup non trouvée")
    
    # Log du téléchargement
    await broadcast_log(f"Téléchargement de la startup #{startup_id}", "info")
    
    # Ici vous généreriez et retourneriez un vrai fichier ZIP
    # Pour l'exemple, on retourne juste une confirmation
    return {
        "success": True,
        "startup_id": startup_id,
        "message": "Fichier ZIP généré avec succès"
    }

# Endpoint de santé
@app.get("/health")
async def health_check():
    """Vérification de la santé de l'API"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "websocket_connections": len(websocket_connections),
        "total_startups": len(startups_db)
    }

# Fonction pour simuler des logs d'agents IA
async def simulate_agent_logs():
    """Simule des logs d'agents IA pour la démo"""
    import random
    
    log_messages = [
        "Agent CEO: Analyse de l'idée de startup...",
        "Agent CEO: Génération de la roadmap...",
        "Agent CEO: Création des épics...",
        "Agent CEO: Génération des user stories...",
        "Agent CEO: Calcul des estimations...",
        "Agent CEO: Roadmap générée avec succès!",
        "Agent Marketing: Analyse du marché cible...",
        "Agent Marketing: Étude de la concurrence...",
        "Agent Marketing: Stratégie de go-to-market définie...",
        "Agent Tech: Architecture technique validée...",
        "Agent Tech: Stack technologique recommandée...",
        "Agent Tech: Estimations de développement calculées..."
    ]
    
    while True:
        if websocket_connections:  # Seulement si des clients sont connectés
            message = random.choice(log_messages)
            await broadcast_log(message, "info")
        
        # Attendre entre 5 et 15 secondes
        await asyncio.sleep(random.randint(5, 15))

# Démarrer la simulation des logs au démarrage
@app.on_event("startup")
async def startup_event():
    """Événement de démarrage de l'application"""
    asyncio.create_task(simulate_agent_logs())

if __name__ == "__main__":
    import uvicorn
    
    print("🚀 Démarrage du Core Engine ShipFast...")
    print("📊 Dashboard disponible sur: http://localhost:3000")
    print("🔌 API disponible sur: http://localhost:8000")
    print("📡 WebSocket disponible sur: ws://localhost:8000/ws/logs")
    
    uvicorn.run(
        "backend-example:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )