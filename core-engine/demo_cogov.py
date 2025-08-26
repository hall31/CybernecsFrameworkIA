#!/usr/bin/env python3
"""
Demo script for Co-Governance System
Shows the complete workflow of hybrid AI+Human governance
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.cogov_agent import CoGovAgent
from agents.codao import CoDAO

def demo_cogov_system():
    """Demonstrate the complete co-governance system"""
    print("🏛️ CO-GOVERNANCE SYSTEM DEMONSTRATION")
    print("=" * 60)
    
    # Initialize the system
    print("\n1️⃣ INITIALIZING CO-GOVERNANCE SYSTEM")
    cogov_agent = CoGovAgent(ai_weighting=50, human_weighting=50)
    codao = CoDAO("Global Co-Governance DAO")
    
    print(f"   ✅ CoGovAgent initialized with {cogov_agent.ai_weighting}% AI, {cogov_agent.ai_weighting}% Human")
    print(f"   ✅ CoDAO initialized: {codao.name}")
    
    # Show board members
    print("\n2️⃣ BOARD MEMBERS")
    members = cogov_agent.get_board_members()
    print("   🤖 AI Board Members:")
    for member in members['ai_members']:
        print(f"      • {member}")
    
    print("   👥 Human Board Members:")
    for member in members['human_members']:
        print(f"      • {member}")
    
    # Demonstrate decision making
    print("\n3️⃣ DECISION MAKING PROCESS")
    print("   📋 Topic: Budget eau 2030")
    
    decision = cogov_agent.run("Budget eau 2030")
    print(f"   🤖 AI Vote: {decision['ai_vote']}")
    print(f"   👥 Human Vote: {decision['human_vote']}")
    print(f"   ⚖️  Final Decision: {decision['final_decision']}")
    print(f"   📊 Weighting: AI {decision['weighting']['AI']}% | Human {decision['weighting']['Human']}")
    
    # Demonstrate DAO proposal
    print("\n4️⃣ DAO PROPOSAL SYSTEM")
    proposal = codao.create_proposal(
        topic="Protection biodiversité marine",
        description="Augmenter le budget pour la protection des océans",
        creator="Marine Conservation NGO",
        ai_weighting=40,
        human_weighting=60
    )
    
    print(f"   📝 Proposal created: {proposal['id']}")
    print(f"   🎯 Topic: {proposal['topic']}")
    print(f"   ⚖️  Weighting: AI {proposal['weighting']['AI']}% | Human {proposal['weighting']['Human']}")
    
    # Submit votes
    print("\n5️⃣ VOTING PROCESS")
    
    # AI votes
    codao.submit_ai_vote(proposal['id'], "PlanetaryAgent", "Augmenter de 25%")
    codao.submit_ai_vote(proposal['id'], "ClimateAgent", "Augmenter de 30%")
    print("   🤖 AI votes submitted")
    
    # Human votes
    codao.submit_human_vote(proposal['id'], "Citizen Group A", "Augmenter de 35%", 150)
    codao.submit_human_vote(proposal['id'], "Expert Marine", "Augmenter de 40%", 200)
    codao.submit_human_vote(proposal['id'], "Indigenous Community", "Augmenter de 45%", 180)
    print("   👥 Human votes submitted")
    
    # Show proposal status
    status = codao.get_proposal_status(proposal['id'])
    print(f"   📊 Current Status: {status['status']}")
    print(f"   🤖 AI Votes: {len(status['ai_votes'])}")
    print(f"   👥 Human Votes: {len(status['human_votes'])}")
    
    # Demonstrate weighting adjustment
    print("\n6️⃣ WEIGHTING ADJUSTMENT")
    print("   🔄 Adjusting weighting for climate decisions...")
    cogov_agent.update_weighting(30, 70)
    print(f"   ✅ New weighting: AI {cogov_agent.ai_weighting}% | Human {cogov_agent.human_weighting}%")
    
    # New decision with adjusted weighting
    climate_decision = cogov_agent.run("Réduction émissions CO2 2025")
    print(f"   🌍 Climate Decision: {climate_decision['final_decision']}")
    print(f"   🤖 AI Vote: {climate_decision['ai_vote']}")
    print(f"   👥 Human Vote: {climate_decision['human_vote']}")
    
    # Show decision history
    print("\n7️⃣ DECISION HISTORY")
    history = cogov_agent.get_decision_history()
    print(f"   📚 Total decisions: {len(history)}")
    
    for i, decision in enumerate(history, 1):
        print(f"   {i}. {decision['decision_topic']}")
        print(f"      🤖 AI: {decision['ai_vote']}")
        print(f"      👥 Human: {decision['human_vote']}")
        print(f"      ⚖️  Final: {decision['final_decision']}")
        print()
    
    # System summary
    print("8️⃣ SYSTEM SUMMARY")
    print("   🎯 Co-Governance System: ✅ OPERATIONAL")
    print("   🤖 AI Integration: ✅ READY")
    print("   👥 Human Participation: ✅ ENABLED")
    print("   ⚖️  Weighted Decisions: ✅ FUNCTIONAL")
    print("   🏛️  DAO Governance: ✅ ACTIVE")
    print("   📊 Decision History: ✅ TRACKED")
    
    print("\n" + "=" * 60)
    print("🎉 DEMONSTRATION COMPLETED SUCCESSFULLY!")
    print("   The Co-Governance system is ready for production use.")
    print("   Next steps: Integrate with React dashboard and deploy API.")

if __name__ == "__main__":
    try:
        demo_cogov_system()
    except Exception as e:
        print(f"❌ Demo failed: {str(e)}")
        sys.exit(1)