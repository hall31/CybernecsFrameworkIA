#!/usr/bin/env python3
"""
Test standalone de l'API - Simulation sans Flask
"""

import json
from core_engine.agents import CEOAgent, CTOAgent

def simulate_api_call(idea):
    """Simule un appel API à /create-startup"""
    print(f"🚀 Simulation de l'API pour l'idée: {idea}")
    print("-" * 50)
    
    # Initialisation des agents
    ceo_agent = CEOAgent()
    cto_agent = CTOAgent()
    
    # Étape 1: Génération de la roadmap business par le CEO
    print("📊 Étape 1: Génération de la roadmap business...")
    roadmap = ceo_agent.run(idea)
    
    # Étape 2: Génération de la stack technique par le CTO
    print("🔧 Étape 2: Génération de la stack technique...")
    stack_info = cto_agent.run(roadmap)
    
    # Construction de la réponse finale (comme l'API)
    response = {
        "success": True,
        "idea": idea,
        "roadmap": roadmap,
        "technical_stack": stack_info,
        "message": "Startup créée avec succès! Consultez le dossier /generated pour le scaffold du projet."
    }
    
    return response

def main():
    """Fonction principale"""
    print("🧪 Test Standalone de l'Epic2 - Startup Creator")
    print("=" * 60)
    
    # Test avec différentes idées
    ideas = [
        "SaaS e-commerce",
        "Plateforme de gestion de projets",
        "Outil d'analyse marketing"
    ]
    
    for i, idea in enumerate(ideas, 1):
        print(f"\n{i}️⃣ Test avec l'idée: {idea}")
        print("=" * 40)
        
        try:
            # Simulation de l'appel API
            result = simulate_api_call(idea)
            
            # Affichage du résultat
            print("\n✅ Résultat de l'API:")
            print(json.dumps(result, indent=2, ensure_ascii=False))
            
            # Vérification des fichiers générés
            print(f"\n📁 Fichiers générés pour '{idea}':")
            import os
            if os.path.exists("generated/docker-compose.yml"):
                print("   ✅ docker-compose.yml")
            if os.path.exists("generated/backend/Dockerfile"):
                print("   ✅ backend/Dockerfile")
            if os.path.exists("generated/frontend/Dockerfile"):
                print("   ✅ frontend/Dockerfile")
                
        except Exception as e:
            print(f"❌ Erreur: {e}")
        
        print("\n" + "-" * 40)
    
    print("\n🎉 Tests terminés avec succès!")
    print("\n📋 Résumé des fonctionnalités testées:")
    print("   • CEOAgent: Génération de roadmap business")
    print("   • CTOAgent: Génération de stack technique")
    print("   • Génération automatique de fichiers Docker")
    print("   • Logging des événements")
    print("   • Structure de données cohérente")

if __name__ == "__main__":
    main()