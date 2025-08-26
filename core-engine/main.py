from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.ceo_agent import CEOAgent
from agents.sovereign_agent import SovereignFundAgent
from utils.logger import log_event

app = FastAPI(title="Core Engine", description="Startup Orchestrator with CEO Agent")

class StartupRequest(BaseModel):
    idea: str

class StartupResponse(BaseModel):
    roadmap: dict
    message: str

class SovereignResponse(BaseModel):
    fund_value: str
    allocations: dict
    long_term_goals: list
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

@app.get("/sovereign", response_model=SovereignResponse)
async def get_sovereign_fund():
    try:
        log_event("main", "Retrieving sovereign fund status")
        
        # Initialize Sovereign Fund Agent
        sovereign_agent = SovereignFundAgent()
        
        # Get fund status
        fund_status = sovereign_agent.get_fund_status()
        
        log_event("main", "Sovereign fund status retrieved successfully")
        
        return SovereignResponse(
            fund_value=fund_status["fund_value"],
            allocations=fund_status["allocations"],
            long_term_goals=fund_status["long_term_goals"],
            message="Sovereign fund status retrieved successfully"
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to retrieve sovereign fund status due to an internal error.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)