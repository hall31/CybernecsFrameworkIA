from utils.logger import log_event
from typing import Dict, List, Optional
import random
import time

class CoGovAgent:
    def __init__(self, ai_weighting: float = 50.0, human_weighting: float = 50.0):
        """
        Initialize the Co-Governance Agent
        
        Args:
            ai_weighting (float): Weight percentage for AI decisions (default: 50%)
            human_weighting (float): Weight percentage for human decisions (default: 50%)
        """
        self.name = "CoGovAgent"
        self.ai_weighting = ai_weighting
        self.human_weighting = human_weighting
        
        # AI Board Members (agents)
        self.ai_board_members = [
            "PlanetaryAgent",
            "MacroFundAgent", 
            "SovereignFundAgent",
            "ClimateAgent",
            "EconomicAgent"
        ]
        
        # Human Board Members (stakeholders)
        self.human_board_members = [
            "Citizens",
            "Governments", 
            "NGOs",
            "Experts",
            "Indigenous Communities",
            "Business Leaders"
        ]
        
        # Decision history
        self.decision_history = []
        
        log_event(self.name, f"Initialized with AI: {ai_weighting}%, Human: {human_weighting}%")
    
    def run(self, decision_topic: str, ai_vote: Optional[str] = None, human_vote: Optional[str] = None) -> dict:
        """
        Execute co-governance decision process
        
        Args:
            decision_topic (str): The topic requiring a decision
            ai_vote (str, optional): Pre-determined AI vote
            human_vote (str, optional): Pre-determined human vote
            
        Returns:
            dict: Complete decision report with weighted outcome
        """
        log_event(self.name, f"Processing decision: {decision_topic}")
        
        # Step 1: Get AI decision (if not provided)
        if ai_vote is None:
            ai_vote = self._get_ai_decision(decision_topic)
        
        # Step 2: Get human decision (if not provided)
        if human_vote is None:
            human_vote = self._get_human_decision(decision_topic)
        
        # Step 3: Calculate weighted final decision
        final_decision = self._calculate_weighted_decision(ai_vote, human_vote)
        
        # Step 4: Generate decision report
        decision_report = {
            "decision_topic": decision_topic,
            "ai_vote": ai_vote,
            "human_vote": human_vote,
            "final_decision": final_decision,
            "weighting": {
                "AI": self.ai_weighting,
                "Human": self.human_weighting
            },
            "timestamp": self._get_timestamp(),
            "ai_board_members": self.ai_board_members,
            "human_board_members": self.human_board_members
        }
        
        # Store in history
        self.decision_history.append(decision_report)
        
        log_event(self.name, f"Décision hybride IA+Humains prise: {final_decision}")
        
        return decision_report
    
    def _get_ai_decision(self, topic: str) -> str:
        """Generate AI decision based on topic"""
        # Simulate AI decision making based on topic
        ai_decisions = {
            "budget": ["Augmenter de 15%", "Augmenter de 20%", "Augmenter de 25%"],
            "eau": ["Augmenter de 20%", "Augmenter de 30%", "Augmenter de 40%"],
            "climat": ["Réduire émissions de 30%", "Réduire émissions de 40%", "Réduire émissions de 50%"],
            "économie": ["Investir 2% du PIB", "Investir 3% du PIB", "Investir 4% du PIB"],
            "santé": ["Augmenter budget de 15%", "Augmenter budget de 25%", "Augmenter budget de 35%"]
        }
        
        # Find matching category
        for category, decisions in ai_decisions.items():
            if category.lower() in topic.lower():
                return random.choice(decisions)
        
        # Default AI decision
        return "Maintenir statu quo"
    
    def _get_human_decision(self, topic: str) -> str:
        """Generate human decision based on topic"""
        # Simulate human decision making based on topic
        human_decisions = {
            "budget": ["Augmenter de 20%", "Augmenter de 30%", "Augmenter de 35%"],
            "eau": ["Augmenter de 25%", "Augmenter de 35%", "Augmenter de 45%"],
            "climat": ["Réduire émissions de 35%", "Réduire émissions de 45%", "Réduire émissions de 55%"],
            "économie": ["Investir 2.5% du PIB", "Investir 3.5% du PIB", "Investir 4.5% du PIB"],
            "santé": ["Augmenter budget de 20%", "Augmenter budget de 30%", "Augmenter budget de 40%"]
        }
        
        # Find matching category
        for category, decisions in human_decisions.items():
            if category.lower() in topic.lower():
                return random.choice(decisions)
        
        # Default human decision
        return "Évaluer plus en détail"
    
    def _calculate_weighted_decision(self, ai_vote: str, human_vote: str) -> str:
        """Calculate weighted final decision"""
        # Extract numerical values from votes
        ai_value = self._extract_numerical_value(ai_vote)
        human_value = self._extract_numerical_value(human_vote)
        
        if ai_value is not None and human_value is not None:
            # Calculate weighted average
            weighted_value = (ai_value * self.ai_weighting + human_value * self.human_weighting) / 100
            
            # Format the decision
            if "augmenter" in ai_vote.lower() or "augmenter" in human_vote.lower():
                return f"Augmenter de {weighted_value:.1f}%"
            elif "réduire" in ai_vote.lower() or "réduire" in human_vote.lower():
                return f"Réduire de {weighted_value:.1f}%"
            elif "investir" in ai_vote.lower() or "investir" in human_vote.lower():
                return f"Investir {weighted_value:.1f}% du PIB"
            else:
                return f"Recommandation pondérée: {weighted_value:.1f}"
        
        # If no numerical values, return compromise decision
        return f"Compromis: {ai_vote} + {human_vote}"
    
    def _extract_numerical_value(self, vote: str) -> Optional[float]:
        """Extract numerical percentage from vote string"""
        import re
        
        # Look for percentage patterns
        percentage_match = re.search(r'(\d+(?:\.\d+)?)\s*%', vote)
        if percentage_match:
            return float(percentage_match.group(1))
        
        # Look for other numerical patterns
        number_match = re.search(r'(\d+(?:\.\d+)?)', vote)
        if number_match:
            return float(number_match.group(1))
        
        return None
    
    def _get_timestamp(self) -> str:
        """Get current timestamp"""
        return time.strftime("%Y-%m-%dT%H:%M:%S")
    
    def get_decision_history(self) -> List[Dict]:
        """Get all decision history"""
        return self.decision_history
    
    def update_weighting(self, ai_weighting: float, human_weighting: float):
        """Update AI vs Human weighting"""
        if ai_weighting + human_weighting != 100:
            raise ValueError("Total weighting must equal 100%")
        
        self.ai_weighting = ai_weighting
        self.human_weighting = human_weighting
        
        log_event(self.name, f"Weighting updated: AI {ai_weighting}%, Human {human_weighting}%")
    
    def get_board_members(self) -> Dict[str, List[str]]:
        """Get current board members"""
        return {
            "ai_members": self.ai_board_members,
            "human_members": self.human_board_members
        }
    
    def add_board_member(self, member_type: str, member_name: str):
        """Add new board member"""
        if member_type.lower() == "ai":
            self.ai_board_members.append(member_name)
            log_event(self.name, f"Added AI board member: {member_name}")
        elif member_type.lower() == "human":
            self.human_board_members.append(member_name)
            log_event(self.name, f"Added human board member: {member_name}")
        else:
            raise ValueError("Member type must be 'ai' or 'human'")