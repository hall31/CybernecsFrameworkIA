#!/usr/bin/env python3
"""
Test simple du système de co-gouvernance
"""

from agents.cogov_agent import CoGovAgent
from agents.codao import CoDAO
from utils.logger import log_event

def test_cogov_system():
    """Test du système de co-gouvernance"""
    print("🧪 Test du système de co-gouvernance")
    
    # Test CoGovAgent
    print("\n1. Test CoGovAgent...")
    cogov_agent = CoGovAgent()
    
    # Test d'une décision
    decision = cogov_agent.run(
        decision_topic="Budget eau 2030",
        ai_vote="Augmenter de 20%",
        human_vote="Augmenter de 30%"
    )
    
    print(f"✅ Décision générée: {decision['final_decision']}")
    print(f"   Structure de la décision: {list(decision.keys())}")
    print(f"   Pondération: {decision['weighting']}")
    
    # Test CoDAO
    print("\n2. Test CoDAO...")
    codao = CoDAO("Test DAO")
    
    # Créer une proposition
    proposal = codao.create_proposal(
        topic="Test Proposition",
        description="Proposition de test pour validation",
        creator="Test User",
        ai_weighting=60.0,
        human_weighting=40.0
    )
    
    print(f"✅ Proposition créée: {proposal['topic']}")
    
    # Soumettre des votes
    codao.submit_ai_vote(
        proposal_id=proposal['id'],
        ai_agent="Test AI Agent",
        vote="Approuver"
    )
    
    codao.submit_human_vote(
        proposal_id=proposal['id'],
        voter="Test Human",
        vote="Approuver avec modifications",
        stake_amount=100.0
    )
    
    print("✅ Votes soumis")
    
    # Vérifier le statut de la proposition
    print(f"   Statut de la proposition: {codao.get_proposal_status(proposal['id'])}")
    
    # Afficher les propositions actives
    print("\n3. Propositions actives...")
    active_proposals = codao.get_active_proposals()
    print(f"✅ {len(active_proposals)} propositions actives")
    
    # Afficher l'historique
    print("\n4. Historique des décisions...")
    history = cogov_agent.get_decision_history()
    print(f"✅ {len(history)} décisions dans l'historique")
    
    # Afficher les membres du conseil
    print("\n5. Membres du conseil...")
    members = cogov_agent.get_board_members()
    print(f"✅ {len(members['ai_members'])} membres IA, {len(members['human_members'])} membres humains")
    
    print("\n🎉 Tous les tests sont passés avec succès !")
    return True

if __name__ == "__main__":
    try:
        test_cogov_system()
    except Exception as e:
        print(f"❌ Erreur lors du test: {str(e)}")
        import traceback
        traceback.print_exc()