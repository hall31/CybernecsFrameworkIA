from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.ceo_agent import CEOAgent
from agents.cogov_agent import CoGovAgent
from agents.codao import CoDAO
from utils.logger import log_event

app = FastAPI(title="Core Engine", description="Startup Orchestrator with CEO Agent")

class StartupRequest(BaseModel):
    idea: str

class StartupResponse(BaseModel):
    roadmap: dict
    message: str

class CoGovDecisionRequest(BaseModel):
    topic: str
    ai_vote: str = None
    human_vote: str = None

class CoGovDecisionResponse(BaseModel):
    decision: dict
    message: str

class CoDAOProposalRequest(BaseModel):
    topic: str
    description: str
    creator: str
    ai_weighting: float = 50.0
    human_weighting: float = 50.0

class CoDAOVoteRequest(BaseModel):
    proposal_id: str
    voter: str
    vote: str
    stake_amount: float = 100.0

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

# Initialize Co-Governance components
cogov_agent = CoGovAgent()
codao = CoDAO()

@app.post("/cogov/decision", response_model=CoGovDecisionResponse)
async def create_cogov_decision(request: CoGovDecisionRequest):
    """Create a co-governance decision"""
    try:
        log_event("main", f"Received co-governance decision request: {request.topic}")
        
        # Generate decision using CoGovAgent
        decision = cogov_agent.run(
            decision_topic=request.topic,
            ai_vote=request.ai_vote,
            human_vote=request.human_vote
        )
        
        log_event("main", f"Co-governance decision generated: {decision['final_decision']}")
        
        return CoGovDecisionResponse(
            decision=decision,
            message=f"Decision generated successfully for: {request.topic}"
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate decision: {str(e)}")

@app.get("/cogov/history")
async def get_decision_history():
    """Get all decision history"""
    try:
        history = cogov_agent.get_decision_history()
        return {"decisions": history}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve history: {str(e)}")

@app.get("/cogov/board-members")
async def get_board_members():
    """Get current board members"""
    try:
        members = cogov_agent.get_board_members()
        return members
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve board members: {str(e)}")

@app.post("/codao/proposal")
async def create_proposal(request: CoDAOProposalRequest):
    """Create a new DAO proposal"""
    try:
        log_event("main", f"Creating DAO proposal: {request.topic}")
        
        proposal = codao.create_proposal(
            topic=request.topic,
            description=request.description,
            creator=request.creator,
            ai_weighting=request.ai_weighting,
            human_weighting=request.human_weighting
        )
        
        return {"proposal": proposal, "message": "Proposal created successfully"}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create proposal: {str(e)}")

@app.post("/codao/vote")
async def submit_vote(request: CoDAOVoteRequest):
    """Submit a vote for a proposal"""
    try:
        log_event("main", f"Submitting vote for proposal: {request.proposal_id}")
        
        # Determine if it's an AI or human vote based on voter name
        if any(ai_agent in request.voter for ai_agent in ["Agent", "AI", "Bot"]):
            result = codao.submit_ai_vote(
                proposal_id=request.proposal_id,
                ai_agent=request.voter,
                vote=request.vote
            )
        else:
            result = codao.submit_human_vote(
                proposal_id=request.proposal_id,
                voter=request.voter,
                vote=request.vote,
                stake_amount=request.stake_amount
            )
        
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to submit vote: {str(e)}")

@app.get("/codao/proposals")
async def get_proposals():
    """Get all active proposals"""
    try:
        active_proposals = codao.get_active_proposals()
        executed_decisions = codao.get_executed_decisions()
        return {
            "active_proposals": active_proposals,
            "executed_decisions": executed_decisions
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve proposals: {str(e)}")

@app.post("/codao/execute/{proposal_id}")
async def execute_proposal(proposal_id: str):
    """Execute a proposal"""
    try:
        log_event("main", f"Executing proposal: {proposal_id}")
        
        result = codao.execute_proposal(proposal_id)
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to execute proposal: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)