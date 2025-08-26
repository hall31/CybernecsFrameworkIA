#!/usr/bin/env python3
"""
Test de la version simplifiée du MarketingAgent
"""

import sys
from pathlib import Path

# Ajouter le répertoire courant au path Python
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

# Import direct des classes
try:
    # Import du logger
    sys.path.insert(0, str(current_dir / "core-engine"))
    from logger import StartupLogger, get_logger
    
    # Import du marketing agent simplifié
    sys.path.insert(0, str(current_dir / "core-engine" / "agents"))
    from marketing_agent_simple import MarketingAgent
    
    print("✅ Imports réussis!")
    
except ImportError as e:
    print(f"❌ Erreur d'import: {e}")
    print("Vérifiez que la structure des dossiers est correcte")
    sys.exit(1)

def test_marketing_agent():
    """Test du MarketingAgent simplifié"""
    logger = get_logger("TestMarketing")
    
    print("🧪 Test du MarketingAgent (version simplifiée)")
    print("=" * 50)
    
    # Test avec une idée
    test_idea = "SaaS marketplace pour freelances"
    print(f"\n🎯 Test avec l'idée: {test_idea}")
    print("-" * 30)
    
    try:
        # Créer l'agent
        agent = MarketingAgent()
        
        # Exécuter l'agent
        result = agent.run(test_idea)
        
        # Afficher les résultats
        print(f"✅ Succès!")
        print(f"   Headline: {result['headline']}")
        print(f"   Tagline: {result['tagline']}")
        print(f"   Features: {len(result['features'])} fonctionnalités")
        print(f"   Pricing: {len(result['pricing'])} plans")
        print(f"   Logo: {result['logo']}")
        print(f"   Landing: {result['landing']}")
        
        # Vérifier que les fichiers ont été créés
        logo_path = Path(result['logo'])
        landing_path = Path(result['landing'])
        
        if logo_path.exists():
            print(f"   ✅ Logo créé: {logo_path}")
            # Vérifier le contenu du logo
            with open(logo_path, 'r') as f:
                logo_content = f.read()
                if 'svg' in logo_content.lower():
                    print(f"   ✅ Logo SVG valide")
                else:
                    print(f"   ⚠️ Logo créé mais contenu suspect")
        else:
            print(f"   ❌ Logo manquant: {logo_path}")
        
        if landing_path.exists():
            print(f"   ✅ Landing page créée: {landing_path}")
            # Vérifier les fichiers de la landing page
            landing_files = list(landing_path.rglob("*"))
            print(f"   📁 Fichiers créés: {len(landing_files)}")
            
            # Vérifier les fichiers clés
            key_files = ['LandingPage.jsx', 'package.json', 'tailwind.config.js', 'README.md']
            for key_file in key_files:
                if (landing_path / key_file).exists():
                    print(f"   ✅ {key_file} créé")
                else:
                    print(f"   ❌ {key_file} manquant")
        else:
            print(f"   ❌ Landing page manquante: {landing_path}")
            
    except Exception as e:
        print(f"❌ Erreur: {e}")
        logger.log_error(f"Test échoué pour {test_idea}", str(e))
        import traceback
        traceback.print_exc()
    
    print("\n" + "=" * 50)
    print("🏁 Test terminé!")

if __name__ == "__main__":
    test_marketing_agent()
Test simple du système d'agents IA
"""

from main import StartupOrchestrator

def test_simple():
    """Test simple du système"""
    print("🧪 TEST SIMPLE DU SYSTÈME D'AGENTS")
    print("=" * 50)
    
    try:
        # Créer une startup
        orchestrator = StartupOrchestrator()
        result = orchestrator.create_startup("Test SaaS simple")
        
        print(f"✅ Statut: {result['status']}")
        
        if result['status'] == 'success':
            print(f"🔧 Backend: {result['backend']['backend_type']}")
            print(f"🎨 Frontend: {result['frontend']['frontend_type']}")
            print(f"📁 Dossier: {result['generated_path']}")
            
            # Vérifier que les fichiers sont créés
            from pathlib import Path
            generated_path = Path(result['generated_path'])
            
            backend_exists = (generated_path / "backend").exists()
            frontend_exists = (generated_path / "frontend").exists()
            docker_exists = (generated_path / "docker-compose.yml").exists()
            
            print(f"📁 Backend créé: {backend_exists}")
            print(f"📁 Frontend créé: {frontend_exists}")
            print(f"🐳 Docker configuré: {docker_exists}")
            
            if backend_exists and frontend_exists and docker_exists:
                print("\n🎉 TOUS LES TESTS ONT RÉUSSI!")
                return True
            else:
                print("\n❌ CERTAINS FICHIERS MANQUENT")
                return False
        else:
            print(f"❌ Erreur: {result.get('error', 'Erreur inconnue')}")
            return False
            
    except Exception as e:
        print(f"❌ Exception: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_simple()
    exit(0 if success else 1)
