#!/usr/bin/env python3
"""
Script pour corriger automatiquement les imports problématiques
"""

import os
import re
from pathlib import Path

def fix_imports_in_file(file_path: Path):
    """Corrige les imports dans un fichier Python"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Corriger les imports de utils
        content = re.sub(
            r'from utils\.logger import',
            'from .utils.logger import',
            content
        )
        
        # Corriger les imports de core
        content = re.sub(
            r'from core\.',
            'from .core.',
            content
        )
        
        # Corriger les imports d'api
        content = re.sub(
            r'from api\.',
            'from .api.',
            content
        )
        
        # Corriger les imports de models
        content = re.sub(
            r'from models\.',
            'from .models.',
            content
        )
        
        # Corriger les imports d'orchestrator
        content = re.sub(
            r'from orchestrator\.',
            'from .orchestrator.',
            content
        )
        
        # Si le fichier a été modifié, le sauvegarder
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Corrigé: {file_path}")
            return True
        else:
            print(f"   Aucun changement: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ Erreur lors du traitement de {file_path}: {e}")
        return False

def fix_imports_in_directory(directory: Path):
    """Corrige les imports dans tous les fichiers Python d'un répertoire"""
    print(f"🔧 Correction des imports dans {directory}")
    
    fixed_count = 0
    total_count = 0
    
    for file_path in directory.rglob("*.py"):
        if file_path.is_file():
            total_count += 1
            if fix_imports_in_file(file_path):
                fixed_count += 1
    
    print(f"📊 Résumé: {fixed_count}/{total_count} fichiers corrigés")
    return fixed_count, total_count

def main():
    """Fonction principale"""
    print("🚀 Correction automatique des imports")
    print("=" * 50)
    
    core_engine_dir = Path("core_engine")
    
    if not core_engine_dir.exists():
        print("❌ Dossier core_engine non trouvé")
        return False
    
    # Corriger les imports dans le dossier core_engine
    fixed, total = fix_imports_in_directory(core_engine_dir)
    
    print(f"\n✅ Correction terminée: {fixed}/{total} fichiers modifiés")
    return True

if __name__ == "__main__":
    main()