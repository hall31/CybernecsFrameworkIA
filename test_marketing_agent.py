#!/usr/bin/env python3
"""
Script de test pour le MarketingAgent
"""

import sys
import os
from pathlib import Path

# Ajouter le répertoire courant au path Python
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

try:
    from core_engine.agents.marketing_agent import MarketingAgent
    from core_engine.logger import get_logger
except ImportError as e:
    print(f"❌ Erreur d'import: {e}")
    print("Vérifiez que la structure des dossiers est correcte")
    sys.exit(1)

def test_marketing_agent():
    """Test du MarketingAgent"""
    logger = get_logger("TestMarketing")
    
    print("🧪 Test du MarketingAgent")
    print("=" * 40)
    
    # Test avec différentes idées
    test_ideas = [
        "SaaS marketplace pour freelances",
        "Application mobile de fitness",
        "Plateforme de gestion de projets",
        "Outil de création de contenu"
    ]
    
    for idea in test_ideas:
        print(f"\n🎯 Test avec l'idée: {idea}")
        print("-" * 30)
        
        try:
            # Créer l'agent
            agent = MarketingAgent()
            
            # Exécuter l'agent
            result = agent.run(idea)
            
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
            logger.log_error(f"Test échoué pour {idea}", str(e))
    
    print("\n" + "=" * 40)
    print("🏁 Tests terminés!")

if __name__ == "__main__":
    test_marketing_agent()