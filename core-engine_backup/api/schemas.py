from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime
from uuid import UUID

class ProjectCreate(BaseModel):
    idea: str
    roadmap: Optional[Dict[str, Any]] = None
    stack: Optional[Dict[str, Any]] = None
    path: Optional[str] = None

class ProjectResponse(BaseModel):
    id: UUID
    idea: str
    roadmap: Optional[Dict[str, Any]] = None
    stack: Optional[Dict[str, Any]] = None
    created_at: datetime
    path: Optional[str] = None

class ProjectList(BaseModel):
    id: UUID
    idea: str
    created_at: datetime

class ProjectDetail(BaseModel):
    id: UUID
    idea: str
    roadmap: Optional[Dict[str, Any]] = None
    stack: Optional[Dict[str, Any]] = None
    created_at: datetime
    path: Optional[str] = None

class LogCreate(BaseModel):
    project_id: UUID
    message: str

class LogResponse(BaseModel):
    id: UUID
    project_id: UUID
    message: str
    timestamp: datetime