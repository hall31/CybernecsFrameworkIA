"""
API Admin FastAPI pour l'orchestration des agents et épics
Cette API permet de gérer l'état des agents et des épics depuis le dashboard React
"""

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import List, Dict, Any
import asyncio
import time

from config import (
    AGENTS_CONFIG, 
    AGENT_STATUS, 
    EPICS, 
    EPIC_STATUS,
    ADMIN_API_PORT,
    ADMIN_API_HOST,
    CORS_ORIGINS
)
from utils.logger import log_event, log_success, log_warning, log_error

# Création de l'application FastAPI
app = FastAPI(
    title="Admin Orchestration API",
    description="API de gestion des agents et épics pour l'orchestration",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configuration CORS pour permettre l'accès depuis le frontend React
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================================
# ROUTES POUR LES AGENTS
# ============================================================================

@app.get("/", tags=["Root"])
async def root():
    """Point d'entrée de l'API"""
    return {
        "message": "🚀 Admin Orchestration API - Gestion des Agents & Épics",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "agents": "/agents",
            "epics": "/epics",
            "health": "/health"
        }
    }

@app.get("/health", tags=["Health"])
async def health_check():
    """Vérification de l'état de l'API"""
    return {
        "status": "healthy",
        "timestamp": time.time(),
        "agents_count": len(AGENTS_CONFIG),
        "epics_count": len(EPICS)
    }

@app.get("/agents", tags=["Agents"], response_model=List[Dict[str, Any]])
async def list_agents():
    """
    Liste tous les agents avec leur état et statut
    
    Returns:
        List[Dict]: Liste des agents avec nom, état activé/désactivé et statut
    """
    agents_list = []
    for name, enabled in AGENTS_CONFIG.items():
        agents_list.append({
            "name": name,
            "enabled": enabled,
            "status": AGENT_STATUS.get(name, "unknown"),
            "type": "agent"
        })
    
    log_event("ADMIN_API", f"Liste des agents récupérée: {len(agents_list)} agents")
    return agents_list

@app.get("/agents/{name}", tags=["Agents"])
async def get_agent(name: str):
    """
    Récupère les informations d'un agent spécifique
    
    Args:
        name (str): Nom de l'agent
        
    Returns:
        Dict: Informations de l'agent
    """
    if name not in AGENTS_CONFIG:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Agent '{name}' non trouvé"
        )
    
    return {
        "name": name,
        "enabled": AGENTS_CONFIG[name],
        "status": AGENT_STATUS.get(name, "unknown"),
        "type": "agent"
    }

@app.post("/agents/{name}/toggle", tags=["Agents"])
async def toggle_agent(name: str):
    """
    Active/désactive un agent
    
    Args:
        name (str): Nom de l'agent à basculer
        
    Returns:
        Dict: Nouvel état de l'agent
    """
    if name not in AGENTS_CONFIG:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Agent '{name}' non trouvé"
        )
    
    # Basculement de l'état
    old_state = AGENTS_CONFIG[name]
    AGENTS_CONFIG[name] = not old_state
    
    # Mise à jour du statut
    new_status = "active" if AGENTS_CONFIG[name] else "disabled"
    AGENT_STATUS[name] = new_status
    
    # Log de l'action
    action = "activé" if AGENTS_CONFIG[name] else "désactivé"
    log_success("ADMIN_API", f"Agent {name} {action} (était: {'activé' if old_state else 'désactivé'})")
    
    return {
        "name": name,
        "enabled": AGENTS_CONFIG[name],
        "status": new_status,
        "previous_state": old_state,
        "message": f"Agent {name} {action} avec succès"
    }

@app.post("/agents/{name}/enable", tags=["Agents"])
async def enable_agent(name: str):
    """
    Active un agent spécifiquement
    
    Args:
        name (str): Nom de l'agent à activer
        
    Returns:
        Dict: État de l'agent après activation
    """
    if name not in AGENTS_CONFIG:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Agent '{name}' non trouvé"
        )
    
    if AGENTS_CONFIG[name]:
        log_warning("ADMIN_API", f"Agent {name} était déjà activé")
        return {
            "name": name,
            "enabled": True,
            "status": "active",
            "message": f"Agent {name} était déjà activé"
        }
    
    AGENTS_CONFIG[name] = True
    AGENT_STATUS[name] = "active"
    
    log_success("ADMIN_API", f"Agent {name} activé avec succès")
    
    return {
        "name": name,
        "enabled": True,
        "status": "active",
        "message": f"Agent {name} activé avec succès"
    }

@app.post("/agents/{name}/disable", tags=["Agents"])
async def disable_agent(name: str):
    """
    Désactive un agent spécifiquement
    
    Args:
        name (str): Nom de l'agent à désactiver
        
    Returns:
        Dict: État de l'agent après désactivation
    """
    if name not in AGENTS_CONFIG:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Agent '{name}' non trouvé"
        )
    
    if not AGENTS_CONFIG[name]:
        log_warning("ADMIN_API", f"Agent {name} était déjà désactivé")
        return {
            "name": name,
            "enabled": False,
            "status": "disabled",
            "message": f"Agent {name} était déjà désactivé"
        }
    
    AGENTS_CONFIG[name] = False
    AGENT_STATUS[name] = "disabled"
    
    log_success("ADMIN_API", f"Agent {name} désactivé avec succès")
    
    return {
        "name": name,
        "enabled": False,
        "status": "disabled",
        "message": f"Agent {name} désactivé avec succès"
    }

# ============================================================================
# ROUTES POUR LES ÉPICS
# ============================================================================

@app.get("/epics", tags=["Epics"], response_model=List[Dict[str, Any]])
async def list_epics():
    """
    Liste toutes les épics avec leur état et statut
    
    Returns:
        List[Dict]: Liste des épics avec id, nom, état et statut
    """
    epics_list = []
    for eid, agents in EPICS.items():
        # Une épic est activée si tous ses agents sont activés
        enabled = all(AGENTS_CONFIG.get(a, False) for a in agents)
        epics_list.append({
            "id": eid,
            "name": eid,
            "agents": agents,
            "enabled": enabled,
            "status": EPIC_STATUS.get(eid, "idle"),
            "type": "epic"
        })
    
    log_event("ADMIN_API", f"Liste des épics récupérée: {len(epics_list)} épics")
    return epics_list

@app.get("/epics/{eid}", tags=["Epics"])
async def get_epic(eid: str):
    """
    Récupère les informations d'une épic spécifique
    
    Args:
        eid (str): ID de l'épic
        
    Returns:
        Dict: Informations de l'épic
    """
    if eid not in EPICS:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Épic '{eid}' non trouvée"
        )
    
    agents = EPICS[eid]
    enabled = all(AGENTS_CONFIG.get(a, False) for a in agents)
    
    return {
        "id": eid,
        "name": eid,
        "agents": agents,
        "enabled": enabled,
        "status": EPIC_STATUS.get(eid, "idle"),
        "type": "epic"
    }

@app.post("/epics/{eid}/toggle", tags=["Epics"])
async def toggle_epic(eid: str):
    """
    Active/désactive tous les agents d'une épic
    
    Args:
        eid (str): ID de l'épic à basculer
        
    Returns:
        Dict: Nouvel état de l'épic
    """
    if eid not in EPICS:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Épic '{eid}' non trouvée"
        )
    
    agents = EPICS[eid]
    currently_enabled = all(AGENTS_CONFIG.get(a, False) for a in agents)
    
    # Basculement de l'état (si activée, on désactive, sinon on active)
    new_state = not currently_enabled
    
    # Mise à jour de tous les agents de l'épic
    for agent_name in agents:
        if agent_name in AGENTS_CONFIG:
            AGENTS_CONFIG[agent_name] = new_state
            AGENT_STATUS[agent_name] = "active" if new_state else "disabled"
    
    # Log de l'action
    action = "activée" if new_state else "désactivée"
    log_success("ADMIN_API", f"Épic {eid} {action} - Agents: {', '.join(agents)}")
    
    return {
        "id": eid,
        "enabled": new_state,
        "agents": agents,
        "message": f"Épic {eid} {action} avec succès"
    }

@app.post("/epics/{eid}/enable", tags=["Epics"])
async def enable_epic(eid: str):
    """
    Active tous les agents d'une épic
    
    Args:
        eid (str): ID de l'épic à activer
        
    Returns:
        Dict: État de l'épic après activation
    """
    if eid not in EPICS:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Épic '{eid}' non trouvée"
        )
    
    agents = EPICS[eid]
    currently_enabled = all(AGENTS_CONFIG.get(a, False) for a in agents)
    
    if currently_enabled:
        log_warning("ADMIN_API", f"Épic {eid} était déjà activée")
        return {
            "id": eid,
            "enabled": True,
            "agents": agents,
            "message": f"Épic {eid} était déjà activée"
        }
    
    # Activation de tous les agents de l'épic
    for agent_name in agents:
        if agent_name in AGENTS_CONFIG:
            AGENTS_CONFIG[agent_name] = True
            AGENT_STATUS[agent_name] = "active"
    
    log_success("ADMIN_API", f"Épic {eid} activée - Agents: {', '.join(agents)}")
    
    return {
        "id": eid,
        "enabled": True,
        "agents": agents,
        "message": f"Épic {eid} activée avec succès"
    }

@app.post("/epics/{eid}/disable", tags=["Epics"])
async def disable_epic(eid: str):
    """
    Désactive tous les agents d'une épic
    
    Args:
        eid (str): ID de l'épic à désactiver
        
    Returns:
        Dict: État de l'épic après désactivation
    """
    if eid not in EPICS:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Épic '{eid}' non trouvée"
        )
    
    agents = EPICS[eid]
    currently_enabled = all(AGENTS_CONFIG.get(a, False) for a in agents)
    
    if not currently_enabled:
        log_warning("ADMIN_API", f"Épic {eid} était déjà désactivée")
        return {
            "id": eid,
            "enabled": False,
            "agents": agents,
            "message": f"Épic {eid} était déjà désactivée"
        }
    
    # Désactivation de tous les agents de l'épic
    for agent_name in agents:
        if agent_name in AGENTS_CONFIG:
            AGENTS_CONFIG[agent_name] = False
            AGENT_STATUS[agent_name] = "disabled"
    
    log_success("ADMIN_API", f"Épic {eid} désactivée - Agents: {', '.join(agents)}")
    
    return {
        "id": eid,
        "enabled": False,
        "agents": agents,
        "message": f"Épic {eid} désactivée avec succès"
    }

@app.post("/epics/{eid}/run", tags=["Epics"])
async def run_epic(eid: str):
    """
    Exécute une épic (simulation d'exécution)
    
    Args:
        eid (str): ID de l'épic à exécuter
        
    Returns:
        Dict: Statut de l'épic après exécution
    """
    if eid not in EPICS:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Épic '{eid}' non trouvée"
        )
    
    agents = EPICS[eid]
    enabled = all(AGENTS_CONFIG.get(a, False) for a in agents)
    
    if not enabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Impossible d'exécuter l'épic {eid}: certains agents sont désactivés"
        )
    
    # Simulation de l'exécution
    EPIC_STATUS[eid] = "running"
    log_event("ADMIN_API", f"Épic {eid} en cours d'exécution...")
    
    # Simulation d'un délai d'exécution
    await asyncio.sleep(2)
    
    # Fin de l'exécution
    EPIC_STATUS[eid] = "done"
    log_success("ADMIN_API", f"Épic {eid} exécutée avec succès")
    
    return {
        "id": eid,
        "status": "done",
        "agents": agents,
        "message": f"Épic {eid} exécutée avec succès"
    }

@app.post("/epics/{eid}/reset", tags=["Epics"])
async def reset_epic(eid: str):
    """
    Remet une épic en statut 'idle'
    
    Args:
        eid (str): ID de l'épic à réinitialiser
        
    Returns:
        Dict: Nouveau statut de l'épic
    """
    if eid not in EPICS:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Épic '{eid}' non trouvée"
        )
    
    old_status = EPIC_STATUS.get(eid, "idle")
    EPIC_STATUS[eid] = "idle"
    
    log_event("ADMIN_API", f"Épic {eid} réinitialisée: {old_status} -> idle")
    
    return {
        "id": eid,
        "status": "idle",
        "previous_status": old_status,
        "message": f"Épic {eid} réinitialisée avec succès"
    }

# ============================================================================
# ROUTES UTILITAIRES
# ============================================================================

@app.get("/status", tags=["Status"])
async def get_system_status():
    """
    Récupère le statut global du système
    
    Returns:
        Dict: Statut global avec agents et épics
    """
    active_agents = sum(1 for enabled in AGENTS_CONFIG.values() if enabled)
    total_agents = len(AGENTS_CONFIG)
    
    running_epics = sum(1 for status in EPIC_STATUS.values() if status == "running")
    done_epics = sum(1 for status in EPIC_STATUS.values() if status == "done")
    total_epics = len(EPICS)
    
    return {
        "system_status": "operational",
        "agents": {
            "total": total_agents,
            "active": active_agents,
            "disabled": total_agents - active_agents
        },
        "epics": {
            "total": total_epics,
            "idle": total_epics - running_epics - done_epics,
            "running": running_epics,
            "done": done_epics
        },
        "timestamp": time.time()
    }

@app.post("/reset", tags=["System"])
async def reset_system():
    """
    Remet tous les statuts d'épics en 'idle'
    
    Returns:
        Dict: Confirmation de la réinitialisation
    """
    for eid in EPIC_STATUS:
        EPIC_STATUS[eid] = "idle"
    
    log_event("ADMIN_API", "Système réinitialisé - tous les statuts d'épics remis à 'idle'")
    
    return {
        "message": "Système réinitialisé avec succès",
        "epics_reset": len(EPIC_STATUS),
        "timestamp": time.time()
    }

# ============================================================================
# GESTIONNAIRE D'ERREURS
# ============================================================================

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Gestionnaire d'erreurs HTTP personnalisé"""
    log_error("ADMIN_API", f"Erreur HTTP {exc.status_code}: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "status_code": exc.status_code,
            "timestamp": time.time()
        }
    )

@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """Gestionnaire d'erreurs générales"""
    log_error("ADMIN_API", f"Erreur inattendue: {str(exc)}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "Erreur interne du serveur",
            "detail": str(exc),
            "timestamp": time.time()
        }
    )

# ============================================================================
# POINT D'ENTRÉE PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    
    log_success("ADMIN_API", f"🚀 Démarrage de l'API Admin sur {ADMIN_API_HOST}:{ADMIN_API_PORT}")
    log_event("ADMIN_API", f"Documentation disponible sur: http://{ADMIN_API_HOST}:{ADMIN_API_PORT}/docs")
    
    uvicorn.run(
        "admin_api:app",
        host=ADMIN_API_HOST,
        port=ADMIN_API_PORT,
        reload=True,
        log_level="info"
    )