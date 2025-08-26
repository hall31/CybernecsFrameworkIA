from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.ceo_agent import CEOAgent
from agents.constitution_agent import ConstitutionAgent
from utils.logger import log_event

app = FastAPI(title="Core Engine", description="Startup Orchestrator with CEO Agent")

class StartupRequest(BaseModel):
    idea: str

class StartupResponse(BaseModel):
    roadmap: dict
    message: str

@app.get("/")
async def root():
    return {"message": "Core Engine - Startup Orchestrator"}

@app.post("/create-startup", response_model=StartupResponse)
async def create_startup(request: StartupRequest):
    try:
        log_event("main", f"Received startup idea: {request.idea}")
        
        # Initialize CEO Agent
        ceo_agent = CEOAgent()
        
        # Generate roadmap
        roadmap = ceo_agent.run(request.idea)
        
        log_event("main", f"Generated roadmap for: {request.idea}")
        
        return StartupResponse(
            roadmap=roadmap,
            message=f"Roadmap generated successfully for: {request.idea}"
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to generate roadmap due to an internal error.")

@app.get("/constitution")
async def get_constitution():
    """Récupère la Constitution IA Globale"""
    try:
        log_event("main", "Constitution request received")
        
        # Initialize Constitution Agent
        constitution_agent = ConstitutionAgent()
        
        # Generate constitution
        result = constitution_agent.run()
        
        log_event("main", "Constitution generated successfully")
        
        return {
            "constitution": result["constitution"],
            "markdown": result["markdown"],
            "summary": result["summary"]
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to generate constitution due to an internal error.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)