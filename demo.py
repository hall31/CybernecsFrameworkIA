#!/usr/bin/env python3
"""
Démonstration complète de l'Epic2 - Startup Creator avec Agents IA
"""

import json
from core_engine.agents import CEOAgent, CTOAgent

def main():
    """Démonstration principale"""
    print("🚀 Epic2 - Startup Creator avec Agents IA")
    print("=" * 50)
    
    # 1. Initialisation des agents
    print("\n1️⃣ Initialisation des agents...")
    ceo_agent = CEOAgent()
    cto_agent = CTOAgent()
    print("✅ Agents initialisés avec succès")
    
    # 2. Génération de la roadmap business
    print("\n2️⃣ Génération de la roadmap business...")
    idea = "SaaS e-commerce"
    print(f"💡 Idée: {idea}")
    
    roadmap = ceo_agent.run(idea)
    print("✅ Roadmap business générée!")
    
    # Affichage de la roadmap
    print("\n📊 Roadmap Business:")
    print(json.dumps(roadmap, indent=2, ensure_ascii=False))
    
    # 3. Génération de la stack technique
    print("\n3️⃣ Génération de la stack technique...")
    stack_info = cto_agent.run(roadmap)
    print("✅ Stack technique générée!")
    
    # Affichage de la stack technique
    print("\n🔧 Stack Technique:")
    print(json.dumps(stack_info, indent=2, ensure_ascii=False))
    
    # 4. Vérification des fichiers générés
    print("\n4️⃣ Vérification des fichiers générés...")
    import os
    
    files_to_check = [
        "generated/docker-compose.yml",
        "generated/backend/Dockerfile",
        "generated/frontend/Dockerfile"
    ]
    
    for file_path in files_to_check:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - MANQUANT")
    
    # 5. Affichage du contenu des fichiers
    print("\n5️⃣ Contenu des fichiers générés...")
    
    # Docker Compose
    if os.path.exists("generated/docker-compose.yml"):
        print("\n🐳 Docker Compose:")
        with open("generated/docker-compose.yml", "r") as f:
            print(f.read())
    
    # Backend Dockerfile
    if os.path.exists("generated/backend/Dockerfile"):
        print("\n🐳 Backend Dockerfile:")
        with open("generated/backend/Dockerfile", "r") as f:
            print(f.read())
    
    # Frontend Dockerfile
    if os.path.exists("generated/frontend/Dockerfile"):
        print("\n🐳 Frontend Dockerfile:")
        with open("generated/frontend/Dockerfile", "r") as f:
            print(f.read())
    
    # 6. Résumé final
    print("\n" + "=" * 50)
    print("🎉 DÉMONSTRATION TERMINÉE AVEC SUCCÈS!")
    print("=" * 50)
    
    print(f"\n📋 Résumé:")
    print(f"   • Idée: {idea}")
    print(f"   • Modèle économique: {roadmap['business_model']}")
    print(f"   • Marché cible: {roadmap['target_market']}")
    print(f"   • Stack technique: {stack_info['stack']}")
    print(f"   • Services: {', '.join(stack_info['services'])}")
    print(f"   • Fichiers générés: {len(stack_info['files'])}")
    
    print(f"\n🚀 Prochaines étapes:")
    print(f"   1. Naviguer vers le dossier /generated")
    print(f"   2. Lancer avec: docker-compose up")
    print(f"   3. Accéder au frontend: http://localhost:3000")
    print(f"   4. Accéder au backend: http://localhost:9000")
    print(f"   5. Base de données: localhost:5432")

if __name__ == "__main__":
    main()