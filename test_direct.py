#!/usr/bin/env python3
"""
Test direct du MarketingAgent
"""

import sys
from pathlib import Path

# Helper to add a directory to sys.path if not already present
def add_to_syspath(path: Path):
    path_str = str(path)
    if path_str not in sys.path:
        sys.path.insert(0, path_str)

# Ajouter le répertoire courant au path Python
current_dir = Path(__file__).parent
add_to_syspath(current_dir)

# Import direct des classes
try:
    # Import du logger
    add_to_syspath(current_dir / "core-engine")
    from logger import StartupLogger, get_logger
    
    # Import du marketing agent
    add_to_syspath(current_dir / "core-engine" / "agents")
    from marketing_agent import MarketingAgent
    
    print("✅ Imports réussis!")
    
except ImportError as e:
    print(f"❌ Erreur d'import: {e}")
    print("Vérifiez que la structure des dossiers est correcte")
    sys.exit(1)

def test_marketing_agent():
    """Test du MarketingAgent"""
    logger = get_logger("TestMarketing")
    
    print("🧪 Test du MarketingAgent")
    print("=" * 40)
    
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
        else:
            print(f"   ❌ Logo manquant: {logo_path}")
        
        if landing_path.exists():
            print(f"   ✅ Landing page créée: {landing_path}")
            # Vérifier les fichiers de la landing page
            landing_files = list(landing_path.rglob("*"))
            print(f"   📁 Fichiers créés: {len(landing_files)}")
        else:
            print(f"   ❌ Landing page manquante: {landing_path}")
            
    except Exception as e:
        print(f"❌ Erreur: {e}")
        logger.log_error(f"Test échoué pour {test_idea}", str(e))
    
    print("\n" + "=" * 40)
    print("🏁 Test terminé!")

if __name__ == "__main__":
    test_marketing_agent()