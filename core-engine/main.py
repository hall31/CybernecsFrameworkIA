from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.ceo_agent import CEOAgent
from agents.hedgefund_agent import HedgeFundAgent
from contracts.trader_contract import TraderContract
from utils.logger import log_event
from datetime import datetime

app = FastAPI(title="Core Engine", description="Startup Orchestrator with CEO Agent and Hedge Fund AI")

# Initialize Hedge Fund components
hedgefund_agent = HedgeFundAgent()
trader_contract = TraderContract()

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

@app.get("/hedgefund")
async def get_hedgefund_status():
    """Retourne le statut actuel du hedge fund avec positions et performance"""
    try:
        log_event("main", "Hedge fund status requested")
        
        # Récupérer le portefeuille actuel
        portfolio_data = hedgefund_agent.get_current_portfolio()
        
        # Récupérer les positions du smart contract
        contract_positions = trader_contract.get_portfolio_summary()
        
        # Combiner les données
        hedgefund_status = {
            "portfolio": portfolio_data["portfolio"],
            "performance": portfolio_data["performance"],
            "strategy_commentary": portfolio_data["strategy_commentary"],
            "contract_summary": contract_positions,
            "last_update": portfolio_data["last_update"]
        }
        
        log_event("main", "Hedge fund status retrieved successfully")
        return hedgefund_status
        
    except Exception as e:
        log_event("main", f"Error retrieving hedge fund status: {str(e)}", "ERROR")
        raise HTTPException(status_code=500, detail="Failed to retrieve hedge fund status")

@app.post("/hedgefund/rebalance")
async def rebalance_hedgefund():
    """Force le rebalancement du portefeuille du hedge fund"""
    try:
        log_event("main", "Manual hedge fund rebalancing requested")
        
        # Exécuter le rebalancement via l'agent
        result = hedgefund_agent.rebalance_portfolio()
        
        # Exécuter le rebalancement via le smart contract
        contract_result = trader_contract.rebalance("HedgeFundAgent")
        
        rebalance_result = {
            "agent_rebalance": result,
            "contract_rebalance": contract_result,
            "timestamp": datetime.now().isoformat()
        }
        
        log_event("main", "Hedge fund rebalancing completed")
        return rebalance_result
        
    except Exception as e:
        log_event("main", f"Error in hedge fund rebalancing: {str(e)}", "ERROR")
        raise HTTPException(status_code=500, detail="Failed to rebalance hedge fund")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)