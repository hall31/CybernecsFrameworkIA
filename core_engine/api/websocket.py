from fastapi import WebSocket, WebSocketDisconnect, HTTPException
from typing import Dict, List
import json
from uuid import UUID
from .api.crud import LogCRUD
from .core.database import AsyncSessionLocal

class ConnectionManager:
    def __init__(self):
        # Store connections by project_id
        self.active_connections: Dict[UUID, List[WebSocket]] = {}
    
    async def connect(self, websocket: WebSocket, project_id: UUID):
        await websocket.accept()
        
        if project_id not in self.active_connections:
            self.active_connections[project_id] = []
        
        self.active_connections[project_id].append(websocket)
    
    def disconnect(self, websocket: WebSocket, project_id: UUID):
        if project_id in self.active_connections:
            if websocket in self.active_connections[project_id]:
                self.active_connections[project_id].remove(websocket)
            
            # Clean up empty project connections
            if not self.active_connections[project_id]:
                del self.active_connections[project_id]
    
    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)
    
    async def broadcast_to_project(self, message: str, project_id: UUID):
        if project_id in self.active_connections:
            for connection in self.active_connections[project_id]:
                try:
                    await connection.send_text(message)
                except:
                    # Remove dead connections
                    self.active_connections[project_id].remove(connection)
                    if not self.active_connections[project_id]:
                        del self.active_connections[project_id]

manager = ConnectionManager()

async def websocket_endpoint(websocket: WebSocket, project_id: UUID):
    await manager.connect(websocket, project_id)
    
    try:
        # Send initial logs
        async with AsyncSessionLocal() as db:
            logs = await LogCRUD.get_by_project(db, project_id)
            initial_logs = [
                {
                    "id": str(log.id),
                    "message": log.message,
                    "timestamp": log.timestamp.isoformat()
                }
                for log in logs[-50:]  # Last 50 logs
            ]
            
            await websocket.send_text(json.dumps({
                "type": "initial_logs",
                "logs": initial_logs
            }))
        
        # Keep connection alive and handle incoming messages
        while True:
            data = await websocket.receive_text()
            # Echo back for ping/pong
            await websocket.send_text(json.dumps({
                "type": "pong",
                "data": data
            }))
            
    except WebSocketDisconnect:
        manager.disconnect(websocket, project_id)
    except Exception as e:
        manager.disconnect(websocket, project_id)
        print(f"WebSocket error: {e}")

# Function to broadcast new logs to connected clients
async def broadcast_log(project_id: UUID, log_data: dict):
    await manager.broadcast_to_project(
        json.dumps({
            "type": "new_log",
            "log": log_data
        }),
        project_id
    )