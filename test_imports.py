#!/usr/bin/env python3
"""
Script de test pour vérifier que les imports fonctionnent après la migration
"""

import sys
import os
from pathlib import Path

def test_imports():
    """Teste les imports depuis core_engine"""
    print("🧪 Test des imports depuis core_engine...")
    
    # Ajouter le répertoire courant au path
    current_dir = Path(__file__).parent
    sys.path.insert(0, str(current_dir))
    
    try:
        # Test 1: Import du module principal
        print("📦 Test import du module principal...")
        import core_engine
        print("   ✅ Import core_engine réussi")
        
        # Test 2: Import d'un agent spécifique
        print("🤖 Test import d'un agent...")
        from core_engine.agents.finance_agent import FinanceAgent
        print("   ✅ Import FinanceAgent réussi")
        
        # Test 3: Import du logger
        print("📝 Test import du logger...")
        from core_engine.logger import get_logger
        print("   ✅ Import logger réussi")
        
        # Test 4: Création d'instances
        print("🔧 Test création d'instances...")
        finance_agent = FinanceAgent()
        logger = get_logger("test")
        print("   ✅ Instances créées avec succès")
        
        # Test 5: Test de fonctionnement
        print("🚀 Test de fonctionnement...")
        result = finance_agent.run("Test startup")
        print(f"   ✅ FinanceAgent.run() exécuté: {len(result)} éléments retournés")
        
        print("\n🎉 Tous les tests passent!")
        return True
        
    except ImportError as e:
        print(f"❌ Erreur d'import: {e}")
        return False
    except Exception as e:
        print(f"❌ Erreur générale: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_file_structure():
    """Vérifie la structure des fichiers"""
    print("\n📁 Vérification de la structure des fichiers...")
    
    core_engine_path = Path("core_engine")
    if not core_engine_path.exists():
        print("❌ Dossier core_engine n'existe pas")
        return False
    
    # Vérifier les fichiers clés
    key_files = [
        "core_engine/__init__.py",
        "core_engine/agents/__init__.py",
        "core_engine/agents/finance_agent.py",
        "core_engine/logger.py"
    ]
    
    for file_path in key_files:
        if Path(file_path).exists():
            print(f"   ✅ {file_path}")
        else:
            print(f"   ❌ {file_path}")
            return False
    
    print("   ✅ Structure des fichiers correcte")
    return True

def main():
    """Fonction principale"""
    print("🚀 Test des imports après migration")
    print("=" * 50)
    
    # Vérifier la structure
    if not test_file_structure():
        print("\n❌ Structure des fichiers incorrecte")
        return False
    
    # Tester les imports
    if test_imports():
        print("\n✅ Migration réussie! Tous les imports fonctionnent.")
        return True
    else:
        print("\n❌ Problèmes d'import détectés")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)