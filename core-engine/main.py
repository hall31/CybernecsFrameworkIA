from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.ceo_agent import CEOAgent
from agents.macrofund_agent import MacroFundAgent
from agents.global_trader_contract import GlobalTraderContract
from utils.logger import log_event

app = FastAPI(title="Core Engine", description="Startup Orchestrator with CEO Agent")

class StartupRequest(BaseModel):
    idea: str

class StartupResponse(BaseModel):
    roadmap: dict
    message: str

class MacroFundResponse(BaseModel):
    portfolio_value: str
    allocations: dict
    hedges: dict
    recent_arbitrages: list
    performance_ytd: float
    sharpe_ratio: float
    max_drawdown: float

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

@app.get("/macrofund", response_model=MacroFundResponse)
async def get_macrofund():
    """
    Get macro fund portfolio overview with allocations, hedges, and performance
    """
    try:
        log_event("main", "Received macrofund request")
        
        # Initialize MacroFundAgent
        macro_agent = MacroFundAgent()
        
        # Get portfolio summary
        portfolio_summary = macro_agent.get_portfolio_summary()
        
        log_event("main", f"Macrofund data retrieved - NAV: {portfolio_summary['portfolio_value']}")
        
        return MacroFundResponse(
            portfolio_value=portfolio_summary['portfolio_value'],
            allocations=portfolio_summary['allocations'],
            hedges=portfolio_summary['hedges'],
            recent_arbitrages=portfolio_summary['recent_arbitrages'],
            performance_ytd=portfolio_summary['performance_ytd'],
            sharpe_ratio=portfolio_summary['sharpe_ratio'],
            max_drawdown=portfolio_summary['max_drawdown']
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve macrofund data: {str(e)}")

@app.post("/macrofund/execute")
async def execute_macrofund():
    """
    Execute macro fund analysis and rebalancing
    """
    try:
        log_event("main", "Received macrofund execution request")
        
        # Initialize MacroFundAgent
        macro_agent = MacroFundAgent()
        
        # Execute macro fund analysis
        result = await macro_agent.run()
        
        log_event("main", f"Macrofund execution completed - {len(result.get('recent_arbitrages', []))} arbitrages")
        
        return {
            "success": True,
            "message": "Macro fund analysis and rebalancing completed",
            "result": result
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to execute macrofund: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)