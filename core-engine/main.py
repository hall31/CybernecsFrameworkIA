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
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.ceo_agent import CEOAgent
from agents.fund_agent import FundAgent
from utils.logger import log_event
from typing import List

app = FastAPI(title="Core Engine", description="Startup Orchestrator with CEO Agent & Fund Management")

class StartupRequest(BaseModel):
    idea: str

class StartupResponse(BaseModel):
    roadmap: dict
    message: str

class FundRequest(BaseModel):
    startups: List[str]

class FundResponse(BaseModel):
    fund_address: str
    fund_symbol: str
    composition: List[dict]
    nav: str
    message: str

# Initialize agents
ceo_agent = CEOAgent()
fund_agent = FundAgent()

@app.get("/")
async def root():
    return {"message": "Core Engine - Startup Orchestrator with Fund Management"}

@app.post("/create-startup", response_model=StartupResponse)
async def create_startup(request: StartupRequest):
    try:
        log_event("main", f"Received startup idea: {request.idea}")
        
        # Generate roadmap
        roadmap = ceo_agent.run(request.idea)
        
        log_event("main", f"Generated roadmap for: {request.idea}")
        
        return StartupResponse(
            roadmap=roadmap,
            message=f"Roadmap generated successfully for: {request.idea}"
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to generate roadmap due to an internal error.")

@app.post("/funds", response_model=FundResponse)
async def create_fund(request: FundRequest):
    """
    Create a new AI Startup Fund (ETF)
    
    Args:
        request: FundRequest containing list of startup tokens
        
    Returns:
        FundResponse with fund details
    """
    try:
        log_event("main", f"Creating fund with startups: {request.startups}")
        
        # Validate input
        if len(request.startups) < 2:
            raise HTTPException(
                status_code=400, 
                detail="Minimum 2 startups required to create a fund"
            )
        
        # Create fund using FundAgent
        fund = fund_agent.run(request.startups)
        
        log_event("main", f"Fund created successfully: {fund['fund_symbol']}")
        
        return FundResponse(
            fund_address=fund["fund_address"],
            fund_symbol=fund["fund_symbol"],
            composition=fund["composition"],
            nav=fund["nav"],
            message=f"AI Startup Fund {fund['fund_symbol']} created successfully"
        )
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        log_event("main", f"Error creating fund: {str(e)}", "ERROR")
        raise HTTPException(status_code=500, detail="Failed to create fund due to an internal error.")

@app.get("/funds")
async def get_all_funds():
    """
    Get all active funds
    
    Returns:
        List of all created funds
    """
    try:
        funds = fund_agent.get_all_funds()
        log_event("main", f"Retrieved {len(funds)} funds")
        
        return {
            "funds": funds,
            "total_count": len(funds),
            "active_count": len([f for f in funds if f["status"] == "active"])
        }
        
    except Exception as e:
        log_event("main", f"Error retrieving funds: {str(e)}", "ERROR")
        raise HTTPException(status_code=500, detail="Failed to retrieve funds due to an internal error.")

@app.get("/funds/{fund_symbol}")
async def get_fund_by_symbol(fund_symbol: str):
    """
    Get fund details by symbol
    
    Args:
        fund_symbol: Fund symbol (e.g., ETF001)
        
    Returns:
        Fund details
    """
    try:
        fund = fund_agent.get_fund_by_symbol(fund_symbol)
        
        if not fund:
            raise HTTPException(status_code=404, detail=f"Fund {fund_symbol} not found")
        
        log_event("main", f"Retrieved fund: {fund_symbol}")
        return fund
        
    except HTTPException:
        raise
    except Exception as e:
        log_event("main", f"Error retrieving fund {fund_symbol}: {str(e)}", "ERROR")
        raise HTTPException(status_code=500, detail="Failed to retrieve fund due to an internal error.")

@app.put("/funds/{fund_symbol}/nav")
async def update_fund_nav(fund_symbol: str, nav: str):
    """
    Update fund NAV
    
    Args:
        fund_symbol: Fund symbol
        nav: New NAV value
        
    Returns:
        Success message
    """
    try:
        success = fund_agent.update_fund_nav(fund_symbol, nav)
        
        if not success:
            raise HTTPException(status_code=404, detail=f"Fund {fund_symbol} not found")
        
        log_event("main", f"Updated NAV for fund {fund_symbol}: {nav}")
        return {"message": f"NAV updated successfully for {fund_symbol}"}
        
    except HTTPException:
        raise
    except Exception as e:
        log_event("main", f"Error updating NAV for fund {fund_symbol}: {str(e)}", "ERROR")
        raise HTTPException(status_code=500, detail="Failed to update NAV due to an internal error.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)