from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router
from api.websocket import websocket_endpoint
from core.database import engine, Base
import asyncio

app = FastAPI(
    title="Epic6 Core Engine",
    description="Backend FastAPI pour la gestion des projets startup",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En production, spécifier les domaines autorisés
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(router, prefix="/api/v1")

# WebSocket endpoint for project logs
@app.websocket("/ws/logs/{project_id}")
async def websocket_logs(websocket: WebSocket, project_id: str):
    from uuid import UUID
    try:
        project_uuid = UUID(project_id)
        await websocket_endpoint(websocket, project_uuid)
    except ValueError:
        await websocket.close(code=4000, reason="Invalid project ID")

# Health check
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "epic6-core-engine"}

# Startup event - create tables
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Shutdown event
@app.on_event("shutdown")
async def shutdown():
    await engine.dispose()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)