#!/usr/bin/env python3
"""
Test final complet de l'Epic2 - Startup Creator
"""

import json
import os
from core_engine.agents import CEOAgent, CTOAgent

def test_complete_workflow():
    """Test complet du workflow Epic2"""
    print("🧪 TEST FINAL COMPLET - Epic2 Startup Creator")
    print("=" * 60)
    
    # Test 1: Agents
    print("\n1️⃣ Test des agents...")
    try:
        ceo = CEOAgent()
        cto = CTOAgent()
        print("✅ Agents initialisés")
    except Exception as e:
        print(f"❌ Erreur d'initialisation des agents: {e}")
        return False
    
    # Test 2: Génération de roadmap
    print("\n2️⃣ Test de génération de roadmap...")
    try:
        roadmap = ceo.run("SaaS e-commerce")
        print("✅ Roadmap générée")
        print(f"   • Idée: {roadmap['idea']}")
        print(f"   • Modèle: {roadmap['business_model']}")
        print(f"   • Marché: {roadmap['target_market']}")
    except Exception as e:
        print(f"❌ Erreur de génération de roadmap: {e}")
        return False
    
    # Test 3: Génération de stack technique
    print("\n3️⃣ Test de génération de stack technique...")
    try:
        stack_info = cto.run(roadmap)
        print("✅ Stack technique générée")
        print(f"   • Stack: {stack_info['stack']}")
        print(f"   • Services: {', '.join(stack_info['services'])}")
        print(f"   • Fichiers: {len(stack_info['files'])}")
    except Exception as e:
        print(f"❌ Erreur de génération de stack: {e}")
        return False
    
    # Test 4: Vérification des fichiers générés
    print("\n4️⃣ Test des fichiers générés...")
    required_files = [
        "generated/docker-compose.yml",
        "generated/backend/Dockerfile",
        "generated/frontend/Dockerfile",
        "generated/package.json",
        "generated/vite.config.js",
        "generated/frontend/index.html",
        "generated/frontend/src/main.jsx",
        "generated/frontend/src/App.jsx",
        "generated/frontend/src/App.css",
        "generated/frontend/src/index.css",
        "generated/start.sh",
        "generated/README.md"
    ]
    
    missing_files = []
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - MANQUANT")
            missing_files.append(file_path)
    
    if missing_files:
        print(f"\n⚠️  {len(missing_files)} fichiers manquants")
        return False
    
    # Test 5: Validation du contenu des fichiers clés
    print("\n5️⃣ Validation du contenu des fichiers...")
    
    # Docker Compose
    try:
        with open("generated/docker-compose.yml", "r") as f:
            content = f.read()
            if "version: \"3.8\"" in content and "postgres:15" in content:
                print("✅ docker-compose.yml - Contenu valide")
            else:
                print("❌ docker-compose.yml - Contenu invalide")
                return False
    except Exception as e:
        print(f"❌ Erreur lecture docker-compose.yml: {e}")
        return False
    
    # Package.json
    try:
        with open("generated/package.json", "r") as f:
            content = f.read()
            if "react" in content and "vite" in content:
                print("✅ package.json - Contenu valide")
            else:
                print("❌ package.json - Contenu invalide")
                return False
    except Exception as e:
        print(f"❌ Erreur lecture package.json: {e}")
        return False
    
    # Test 6: Structure des dossiers
    print("\n6️⃣ Test de la structure des dossiers...")
    required_dirs = [
        "generated",
        "generated/backend",
        "generated/frontend",
        "generated/frontend/src"
    ]
    
    for dir_path in required_dirs:
        if os.path.isdir(dir_path):
            print(f"✅ {dir_path}/")
        else:
            print(f"❌ {dir_path}/ - MANQUANT")
            return False
    
    # Test 7: Permissions du script de lancement
    print("\n7️⃣ Test des permissions...")
    try:
        if os.access("generated/start.sh", os.X_OK):
            print("✅ start.sh - Exécutable")
        else:
            print("❌ start.sh - Non exécutable")
            return False
    except Exception as e:
        print(f"❌ Erreur vérification permissions: {e}")
        return False
    
    return True

def main():
    """Fonction principale"""
    print("🚀 Epic2 - Startup Creator - Test Final")
    print("=" * 60)
    
    success = test_complete_workflow()
    
    print("\n" + "=" * 60)
    if success:
        print("🎉 TOUS LES TESTS SONT PASSÉS AVEC SUCCÈS!")
        print("✅ Epic2 est prêt à l'utilisation")
        
        print("\n📋 Résumé des fonctionnalités validées:")
        print("   • CEOAgent: Génération de roadmap business")
        print("   • CTOAgent: Génération de stack technique")
        print("   • Génération automatique de fichiers Docker")
        print("   • Scaffold React complet avec Vite")
        print("   • Configuration Laravel + PostgreSQL")
        print("   • Script de lancement automatisé")
        print("   • Documentation complète")
        
        print("\n🚀 Prochaines étapes:")
        print("   1. Naviguer vers le dossier /generated")
        print("   2. Lancer: ./start.sh")
        print("   3. Accéder au frontend: http://localhost:3000")
        
    else:
        print("❌ CERTAINS TESTS ONT ÉCHOUÉ")
        print("Veuillez vérifier les erreurs ci-dessus")
    
    print("=" * 60)

if __name__ == "__main__":
    main()