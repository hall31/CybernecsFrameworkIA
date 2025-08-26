from utils.logger import log_event
from typing import Dict, List, Optional
from .cogov_agent import CoGovAgent
import hashlib
import json
import time

class CoDAO:
    def __init__(self, name: str = "Co-Governance DAO"):
        """
        Initialize the Co-Governance DAO
        
        Args:
            name (str): Name of the DAO
        """
        self.name = name
        self.cogov_agent = CoGovAgent()
        
        # DAO governance parameters
        self.minimum_quorum = 51  # Minimum participation percentage
        self.voting_period = 7  # Days for voting
        self.execution_delay = 1  # Days delay before execution
        
        # Active proposals
        self.active_proposals = {}
        
        # Executed decisions
        self.executed_decisions = []
        
        # Smart contract rules (simulated)
        self.smart_contract_rules = {
            "ai_weighting": 50.0,
            "human_weighting": 50.0,
            "max_proposal_duration": 30,
            "min_stake_required": 100
        }
        
        log_event(self.name, f"Initialized with governance rules")
    
    def create_proposal(self, topic: str, description: str, creator: str, 
                       ai_weighting: Optional[float] = None, 
                       human_weighting: Optional[float] = None) -> Dict:
        """
        Create a new governance proposal
        
        Args:
            topic (str): Decision topic
            description (str): Detailed description
            creator (str): Creator of the proposal
            ai_weighting (float, optional): Custom AI weighting
            human_weighting (float, optional): Custom human weighting
            
        Returns:
            dict: Proposal details with unique ID
        """
        # Generate unique proposal ID
        proposal_id = self._generate_proposal_id(topic, creator)
        
        # Set custom weighting if provided
        if ai_weighting is not None and human_weighting is not None:
            self.cogov_agent.update_weighting(ai_weighting, human_weighting)
        
        # Create proposal
        proposal = {
            "id": proposal_id,
            "topic": topic,
            "description": description,
            "creator": creator,
            "status": "active",
            "created_at": self._get_timestamp(),
            "voting_ends": self._calculate_voting_end(),
            "execution_date": self._calculate_execution_date(),
            "ai_votes": [],
            "human_votes": [],
            "weighting": {
                "AI": self.cogov_agent.ai_weighting,
                "Human": self.cogov_agent.human_weighting
            }
        }
        
        self.active_proposals[proposal_id] = proposal
        
        log_event(self.name, f"New proposal created: {topic} (ID: {proposal_id})")
        
        return proposal
    
    def submit_ai_vote(self, proposal_id: str, ai_agent: str, vote: str) -> Dict:
        """
        Submit AI vote for a proposal
        
        Args:
            proposal_id (str): Proposal ID
            ai_agent (str): Name of the AI agent
            vote (str): AI decision
            
        Returns:
            dict: Vote confirmation
        """
        if proposal_id not in self.active_proposals:
            raise ValueError("Proposal not found")
        
        proposal = self.active_proposals[proposal_id]
        
        # Check if voting is still open
        if not self._is_voting_open(proposal):
            raise ValueError("Voting period has ended")
        
        # Add AI vote
        ai_vote = {
            "agent": ai_agent,
            "vote": vote,
            "timestamp": self._get_timestamp(),
            "type": "ai"
        }
        
        proposal["ai_votes"].append(ai_vote)
        
        log_event(self.name, f"AI vote submitted by {ai_agent}: {vote}")
        
        return {
            "status": "success",
            "message": f"AI vote recorded for {ai_agent}",
            "proposal_id": proposal_id
        }
    
    def submit_human_vote(self, proposal_id: str, voter: str, vote: str, 
                          stake_amount: float = 100) -> Dict:
        """
        Submit human vote for a proposal
        
        Args:
            proposal_id (str): Proposal ID
            voter (str): Voter identifier
            vote (str): Human decision
            stake_amount (float): Stake amount (influence on decision)
            
        Returns:
            dict: Vote confirmation
        """
        if proposal_id not in self.active_proposals:
            raise ValueError("Proposal not found")
        
        proposal = self.active_proposals[proposal_id]
        
        # Check if voting is still open
        if not self._is_voting_open(proposal):
            raise ValueError("Voting period has ended")
        
        # Check minimum stake requirement
        if stake_amount < self.smart_contract_rules["min_stake_required"]:
            raise ValueError(f"Minimum stake required: {self.smart_contract_rules['min_stake_required']}")
        
        # Add human vote
        human_vote = {
            "voter": voter,
            "vote": vote,
            "stake_amount": stake_amount,
            "timestamp": self._get_timestamp(),
            "type": "human"
        }
        
        proposal["human_votes"].append(human_vote)
        
        log_event(self.name, f"Human vote submitted by {voter} with stake {stake_amount}")
        
        return {
            "status": "success",
            "message": f"Human vote recorded for {voter}",
            "proposal_id": proposal_id,
            "stake_amount": stake_amount
        }
    
    def execute_proposal(self, proposal_id: str) -> Dict:
        """
        Execute a proposal and generate final decision
        
        Args:
            proposal_id (str): Proposal ID to execute
            
        Returns:
            dict: Final decision and execution details
        """
        if proposal_id not in self.active_proposals:
            raise ValueError("Proposal not found")
        
        proposal = self.active_proposals[proposal_id]
        
        # Check if execution date has arrived
        if not self._can_execute(proposal):
            raise ValueError("Execution date has not arrived yet")
        
        # Check quorum
        if not self._meets_quorum(proposal):
            raise ValueError("Minimum quorum not met")
        
        # Generate final decision using CoGovAgent
        ai_vote = self._aggregate_ai_votes(proposal["ai_votes"])
        human_vote = self._aggregate_human_votes(proposal["human_votes"])
        
        decision_result = self.cogov_agent.run(
            decision_topic=proposal["topic"],
            ai_vote=ai_vote,
            human_vote=human_vote
        )
        
        # Add execution details
        execution_details = {
            "proposal_id": proposal_id,
            "executed_at": self._get_timestamp(),
            "total_ai_votes": len(proposal["ai_votes"]),
            "total_human_votes": len(proposal["human_votes"]),
            "participation_rate": self._calculate_participation_rate(proposal),
            "final_decision": decision_result["final_decision"]
        }
        
        # Move to executed decisions
        self.executed_decisions.append({
            **proposal,
            **execution_details,
            "status": "executed"
        })
        
        # Remove from active proposals
        del self.active_proposals[proposal_id]
        
        log_event(self.name, f"Proposal executed: {proposal['topic']} -> {decision_result['final_decision']}")
        
        return {
            "status": "executed",
            "proposal": proposal,
            "decision": decision_result,
            "execution": execution_details
        }
    
    def get_active_proposals(self) -> List[Dict]:
        """Get all active proposals"""
        return list(self.active_proposals.values())
    
    def get_executed_decisions(self) -> List[Dict]:
        """Get all executed decisions"""
        return self.executed_decisions
    
    def get_proposal_status(self, proposal_id: str) -> Optional[Dict]:
        """Get status of a specific proposal"""
        if proposal_id in self.active_proposals:
            return self.active_proposals[proposal_id]
        
        # Check executed decisions
        for decision in self.executed_decisions:
            if decision["id"] == proposal_id:
                return decision
        
        return None
    
    def get_proposals(self) -> Dict[str, List[Dict]]:
        """Get all active proposals and executed decisions"""
        return {
            "active_proposals": list(self.active_proposals.values()),
            "executed_decisions": self.executed_decisions
        }
    
    def _generate_proposal_id(self, topic: str, creator: str) -> str:
        """Generate unique proposal ID"""
        content = f"{topic}_{creator}_{self._get_timestamp()}"
        return hashlib.md5(content.encode()).hexdigest()[:8]
    
    def _get_timestamp(self) -> str:
        """Get current timestamp"""
        return time.strftime("%Y-%m-%dT%H:%M:%S")
    
    def _calculate_voting_end(self) -> str:
        """Calculate voting end date"""
        end_timestamp = time.time() + (self.voting_period * 24 * 3600)
        return time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(end_timestamp))
    
    def _calculate_execution_date(self) -> str:
        """Calculate execution date"""
        execution_timestamp = time.time() + ((self.voting_period + self.execution_delay) * 24 * 3600)
        return time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(execution_timestamp))
    
    def _is_voting_open(self, proposal: Dict) -> bool:
        """Check if voting is still open"""
        voting_end = time.strptime(proposal["voting_ends"], "%Y-%m-%dT%H:%M:%S")
        voting_end_timestamp = time.mktime(voting_end)
        return time.time() < voting_end_timestamp
    
    def _can_execute(self, proposal: Dict) -> bool:
        """Check if proposal can be executed"""
        execution_date = time.strptime(proposal["execution_date"], "%Y-%m-%dT%H:%M:%S")
        execution_timestamp = time.mktime(execution_date)
        return time.time() >= execution_timestamp
    
    def _meets_quorum(self, proposal: Dict) -> bool:
        """Check if minimum quorum is met"""
        total_votes = len(proposal["ai_votes"]) + len(proposal["human_votes"])
        return total_votes >= self.minimum_quorum
    
    def _calculate_participation_rate(self, proposal: Dict) -> float:
        """Calculate participation rate"""
        total_votes = len(proposal["ai_votes"]) + len(proposal["human_votes"])
        # Assuming total possible participants
        total_participants = len(self.cogov_agent.ai_board_members) + len(self.cogov_agent.human_board_members)
        return (total_votes / total_participants) * 100 if total_participants > 0 else 0
    
    def _aggregate_ai_votes(self, ai_votes: List[Dict]) -> str:
        """Aggregate AI votes into single decision"""
        if not ai_votes:
            return "Aucun vote IA"
        
        # Simple aggregation - take the most common vote
        vote_counts = {}
        for vote in ai_votes:
            vote_text = vote["vote"]
            vote_counts[vote_text] = vote_counts.get(vote_text, 0) + 1
        
        # Return most common vote
        return max(vote_counts.items(), key=lambda x: x[1])[0]
    
    def _aggregate_human_votes(self, human_votes: List[Dict]) -> str:
        """Aggregate human votes into single decision"""
        if not human_votes:
            return "Aucun vote humain"
        
        # Weighted aggregation based on stake amount
        vote_weights = {}
        total_stake = 0
        
        for vote in human_votes:
            vote_text = vote["vote"]
            stake = vote["stake_amount"]
            
            if vote_text not in vote_weights:
                vote_weights[vote_text] = 0
            
            vote_weights[vote_text] += stake
            total_stake += stake
        
        if total_stake == 0:
            return "Aucun vote humain"
        
        # Return vote with highest weighted stake
        return max(vote_weights.items(), key=lambda x: x[1])[0]