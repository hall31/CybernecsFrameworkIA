from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any, Optional
from .main import orchestrator

app = FastAPI(title="StartupAI Investor API", version="1.0.0")

# CORS
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

class CreateStartupRequest(BaseModel):
	idea: str
	project_id: Optional[str] = None

@app.get("/health")
async def health() -> Dict[str, str]:
	return {"status": "ok"}

@app.post("/create-startup")
async def create_startup(payload: CreateStartupRequest) -> Dict[str, Any]:
	try:
		result = orchestrator.create_startup(idea=payload.idea, project_id=payload.project_id)
		return result
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))

@app.get("/startup/{project_id}")
async def get_startup(project_id: str) -> Dict[str, Any]:
	try:
		result = orchestrator.get_startup_details(project_id)
		return result
	except Exception as e:
		raise HTTPException(status_code=404, detail=str(e))