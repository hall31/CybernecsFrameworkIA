from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.ceo_agent import CEOAgent
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
        log_event("main", f"Error generating roadmap: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to generate roadmap: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)