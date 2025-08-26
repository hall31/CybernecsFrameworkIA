#!/usr/bin/env python3
"""
Script de démarrage rapide pour tester tous les composants du Core Engine
"""

import sys
import os

# Ajouter le répertoire courant au path Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Teste que tous les modules peuvent être importés"""
    print("🔍 Test des imports...")
    
    try:
        from .utils.logger import log_event, log_success, log_warning, log_error
        print("   ✅ utils.logger - OK")
    except ImportError as e:
        print(f"   ❌ utils.logger - Erreur: {e}")
        return False
    
    try:
        from agents.ceo_agent import CEOAgent
        print("   ✅ agents.ceo_agent - OK")
    except ImportError as e:
        print(f"   ❌ agents.ceo_agent - Erreur: {e}")
        return False
    
    try:
        from main import app
        print("   ✅ main - OK")
    except ImportError as e:
        print(f"   ❌ main - Erreur: {e}")
        return False
    
    return True

def test_logger():
    """Teste le système de logging"""
    print("\n📝 Test du système de logging...")
    
    try:
        from .utils.logger import log_event, log_success, log_warning, log_error
        
        log_event("test", "Test de log INFO")
        log_success("test", "Test de log SUCCESS")
        log_warning("test", "Test de log WARNING")
        log_error("test", "Test de log ERROR")
        
        print("   ✅ Logger - OK")
        return True
    except Exception as e:
        print(f"   ❌ Logger - Erreur: {e}")
        return False

def test_ceo_agent():
    """Teste le CEO Agent"""
    print("\n🧠 Test du CEO Agent...")
    
    try:
        from agents.ceo_agent import CEOAgent
        
        ceo = CEOAgent()
        roadmap = ceo.run("Test startup idea")
        
        # Vérifier la structure de la roadmap
        required_keys = ['startup_idea', 'vision', 'epics', 'timeline', 'success_metrics', 'risks', 'next_steps']
        for key in required_keys:
            if key not in roadmap:
                print(f"   ❌ Clé manquante dans la roadmap: {key}")
                return False
        
        print(f"   ✅ CEO Agent - OK (Roadmap avec {len(roadmap['epics'])} epics)")
        return True
    except Exception as e:
        print(f"   ❌ CEO Agent - Erreur: {e}")
        return False

def test_fastapi_app():
    """Teste l'application FastAPI"""
    print("\n🚀 Test de l'application FastAPI...")
    
    try:
        from main import app
        
        # Vérifier que l'app FastAPI est créée
        if hasattr(app, 'routes'):
            print(f"   ✅ FastAPI App - OK ({len(app.routes)} routes)")
            return True
        else:
            print("   ❌ FastAPI App - Pas de routes trouvées")
            return False
    except Exception as e:
        print(f"   ❌ FastAPI App - Erreur: {e}")
        return False

def main():
    """Fonction principale de test"""
    print("🧩 Core Engine - Test de démarrage rapide")
    print("=" * 50)
    
    tests = [
        ("Imports", test_imports),
        ("Logger", test_logger),
        ("CEO Agent", test_ceo_agent),
        ("FastAPI App", test_fastapi_app)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        if test_func():
            passed += 1
        else:
            print(f"\n❌ Test '{test_name}' a échoué")
    
    print("\n" + "=" * 50)
    print(f"📊 Résultats: {passed}/{total} tests passés")
    
    if passed == total:
        print("🎉 Tous les tests sont passés ! Le Core Engine est prêt.")
        print("\n🚀 Pour lancer l'application:")
        print("   python main.py")
        print("\n🐳 Ou avec Docker:")
        print("   docker-compose up --build")
        print("\n🧪 Pour tester l'API:")
        print("   python test_api.py")
        return True
    else:
        print("❌ Certains tests ont échoué. Vérifiez les erreurs ci-dessus.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)