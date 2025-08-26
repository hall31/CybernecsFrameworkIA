#!/usr/bin/env python3
"""
Script de test local pour vérifier le fonctionnement du CEO Agent
"""

import sys
import os

# Ajouter le répertoire courant au path Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from agents.ceo_agent import CEOAgent
from utils.logger import log_event, log_success

def test_ceo_agent():
    """Test du CEO Agent avec une idée de startup"""
    
    log_event("test", "Starting CEO Agent test")
    
    # Créer une instance du CEO Agent
    ceo = CEOAgent()
    
    # Tester avec une idée de startup
    test_idea = "SaaS marketplace for freelancers"
    
    log_event("test", f"Testing with idea: {test_idea}")
    
    try:
        # Générer la roadmap
        roadmap = ceo.run(test_idea)
        
        # Afficher les résultats
        log_success("test", "Roadmap generated successfully!")
        
        print("\n" + "="*60)
        print("📋 ROADMAP GÉNÉRÉE")
        print("="*60)
        
        print(f"🚀 Idée: {roadmap['startup_idea']}")
        print(f"🎯 Vision: {roadmap['vision']}")
        
        print(f"\n📚 Epics ({len(roadmap['epics'])}):")
        for epic in roadmap['epics']:
            print(f"  • {epic['id']}: {epic['name']} ({epic['priority']})")
            print(f"    {epic['description']}")
            print(f"    User Stories: {len(epic['user_stories'])}")
        
        print(f"\n⏱️  Timeline:")
        for phase, details in roadmap['timeline'].items():
            print(f"  • {details['name']}: {details['duration']}")
        
        print(f"\n📊 Métriques de succès ({len(roadmap['success_metrics'])}):")
        for metric in roadmap['success_metrics']:
            print(f"  • {metric}")
        
        print(f"\n⚠️  Risques ({len(roadmap['risks'])}):")
        for risk in roadmap['risks']:
            print(f"  • {risk['risk']} (Prob: {risk['probability']}, Impact: {risk['impact']})")
        
        print(f"\n🎯 Prochaines étapes ({len(roadmap['next_steps'])}):")
        for i, step in enumerate(roadmap['next_steps'], 1):
            print(f"  {i}. {step}")
        
        print("\n" + "="*60)
        log_success("test", "Test completed successfully!")
        
        return True
        
    except Exception as e:
        log_event("test", f"Error during test: {str(e)}", "ERROR")
        return False

if __name__ == "__main__":
    success = test_ceo_agent()
    sys.exit(0 if success else 1)