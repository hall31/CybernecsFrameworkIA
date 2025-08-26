#!/usr/bin/env python3
"""
Script de test pour l'orchestrateur de startup
"""

import sys
import os

# Ajouter le répertoire courant au path Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import StartupOrchestrator

def test_startup_generation():
    """Test de génération d'une startup complète"""
    print("🚀 Test de l'orchestrateur de startup")
    print("=" * 50)
    
    try:
        # Créer l'orchestrateur
        orchestrator = StartupOrchestrator()
        print("✅ Orchestrateur créé avec succès")
        
        # Tester avec une idée
        idea = "SaaS marketplace pour freelances"
        print(f"📝 Idée testée: {idea}")
        
        # Générer la startup
        result = orchestrator.create_startup(idea)
        
        if result.get("status") == "success":
            print("✅ Startup générée avec succès!")
            print(f"📊 Finance: {len(result.get('finance', {}).get('pricing_models', []))} modèles de pricing")
            print(f"⚖️ Legal: {len(result.get('legal', []))} documents générés")
            print(f"📈 Growth: {len(result.get('growth', {}).get('channels', []))} canaux d'acquisition")
            
            # Vérifier les fichiers légaux
            legal_dir = "generated/legal"
            if os.path.exists(legal_dir):
                legal_files = os.listdir(legal_dir)
                print(f"📁 Fichiers légaux créés: {legal_files}")
            else:
                print("❌ Répertoire légal non trouvé")
                
        else:
            print(f"❌ Erreur lors de la génération: {result.get('error')}")
            return False
            
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors du test: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def test_individual_agents():
    """Test des agents individuels"""
    print("\n🔧 Test des agents individuels")
    print("=" * 50)
    
    try:
        from core_engine.agents.finance_agent import FinanceAgent
        from core_engine.agents.legal_agent import LegalAgent
        from core_engine.agents.growth_agent import GrowthAgent
        
        # Test FinanceAgent
        finance = FinanceAgent()
        finance_result = finance.run("Test idea")
        print(f"✅ FinanceAgent: {len(finance_result.get('pricing_models', []))} modèles de pricing")
        
        # Test LegalAgent
        legal = LegalAgent()
        legal_result = legal.run("Test idea")
        print(f"✅ LegalAgent: {len(legal_result.get('generated_files', []))} documents générés")
        
        # Test GrowthAgent
        growth = GrowthAgent()
        growth_result = growth.run("Test idea")
        print(f"✅ GrowthAgent: {len(growth_result.get('channels', []))} canaux d'acquisition")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors du test des agents: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🧪 Démarrage des tests...")
    
    # Test des agents individuels
    agents_ok = test_individual_agents()
    
    # Test de l'orchestrateur complet
    orchestrator_ok = test_startup_generation()
    
    print("\n" + "=" * 50)
    if agents_ok and orchestrator_ok:
        print("🎉 Tous les tests sont passés avec succès!")
        print("✅ L'épique est complètement implémentée")
    else:
        print("❌ Certains tests ont échoué")
        print("🔧 Vérifiez les erreurs ci-dessus")
    
    print("=" * 50)