#!/usr/bin/env python3
"""
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