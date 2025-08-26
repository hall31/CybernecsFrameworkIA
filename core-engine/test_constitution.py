#!/usr/bin/env python3

from agents.constitution_agent import ConstitutionAgent

def test_constitution_agent():
    """Test simple de l'agent Constitution"""
    try:
        print("🧪 Test de l'agent Constitution...")
        
        # Créer l'agent
        agent = ConstitutionAgent()
        print("✅ Agent créé avec succès")
        
        # Exécuter l'agent
        result = agent.run()
        print("✅ Agent exécuté avec succès")
        
        # Vérifier la structure du résultat
        print(f"📊 Résumé: {result['summary']}")
        print(f"📝 Articles: {len(result['constitution']['articles'])}")
        print(f"✏️ Amendements: {len(result['constitution']['amendments'])}")
        
        print("\n🎉 Test réussi !")
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors du test: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_constitution_agent()