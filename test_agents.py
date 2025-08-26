#!/usr/bin/env python3
"""
Script de test pour les agents CEO et CTO
"""

from core_engine.agents import CEOAgent, CTOAgent

def test_agents():
    """Teste le fonctionnement des agents"""
    print("🧪 Test des agents...")
    
    # Test du CEOAgent
    print("\n1. Test du CEOAgent...")
    ceo = CEOAgent()
    roadmap = ceo.run("SaaS e-commerce")
    print("✅ Roadmap générée:", roadmap)
    
    # Test du CTOAgent
    print("\n2. Test du CTOAgent...")
    cto = CTOAgent()
    stack_info = cto.run(roadmap)
    print("✅ Stack technique générée:", stack_info)
    
    # Vérification des fichiers générés
    print("\n3. Vérification des fichiers générés...")
    import os
    if os.path.exists("generated/docker-compose.yml"):
        print("✅ docker-compose.yml généré")
    if os.path.exists("generated/backend/Dockerfile"):
        print("✅ Backend Dockerfile généré")
    if os.path.exists("generated/frontend/Dockerfile"):
        print("✅ Frontend Dockerfile généré")
    
    print("\n🎉 Test terminé avec succès!")

if __name__ == "__main__":
    test_agents()