#!/usr/bin/env python3
"""
Script de migration pour fusionner les dossiers core_engine et core-engine
et résoudre les conflits de merge
"""

import os
import shutil
import sys
from pathlib import Path
import subprocess

def backup_directory(src, backup_name):
    """Crée une sauvegarde d'un dossier"""
    backup_path = Path(f"{backup_name}_backup")
    if backup_path.exists():
        shutil.rmtree(backup_path)
    shutil.copytree(src, backup_path)
    print(f"✅ Sauvegarde créée: {backup_path}")
    return backup_path

def merge_directories(src, dst):
    """Fusionne le contenu de src dans dst"""
    src_path = Path(src)
    dst_path = Path(dst)
    
    if not src_path.exists():
        print(f"⚠️  Source {src} n'existe pas")
        return False
    
    if not dst_path.exists():
        print(f"⚠️  Destination {dst} n'existe pas")
        return False
    
    print(f"🔄 Fusion de {src} dans {dst}...")
    
    # Copier tous les fichiers et dossiers
    for item in src_path.iterdir():
        dst_item = dst_path / item.name
        
        if item.is_file():
            # Si le fichier existe, le sauvegarder et le remplacer
            if dst_item.exists():
                backup_file = dst_path / f"{item.stem}_backup{item.suffix}"
                shutil.copy2(dst_item, backup_file)
                print(f"   📄 Sauvegarde: {backup_file}")
            
            shutil.copy2(item, dst_item)
            print(f"   📄 Copié: {item.name}")
            
        elif item.is_dir():
            # Si le dossier existe, fusionner récursivement
            if dst_item.exists():
                merge_directories(item, dst_item)
            else:
                shutil.copytree(item, dst_item)
                print(f"   📁 Copié: {item.name}")
    
    return True

def resolve_conflicts():
    """Résout les conflits entre les deux structures"""
    print("🔧 Résolution des conflits...")
    
    # 1. Sauvegarder les deux structures
    print("\n📦 Création des sauvegardes...")
    backup_underscore = backup_directory("core_engine", "core_engine")
    backup_dash = backup_directory("core-engine", "core-engine")
    
    # 2. Fusionner core_engine dans core-engine
    print("\n🔄 Fusion des dossiers...")
    if merge_directories("core_engine", "core-engine"):
        print("✅ Fusion réussie")
    else:
        print("❌ Échec de la fusion")
        return False
    
    # 3. Mettre à jour les fichiers __init__.py
    print("\n📝 Mise à jour des fichiers __init__.py...")
    update_init_files()
    
    # 4. Supprimer le dossier core_engine dupliqué
    print("\n🗑️  Nettoyage...")
    if Path("core_engine").exists():
        shutil.rmtree("core_engine")
        print("✅ Dossier core_engine supprimé")
    
    # 5. Renommer core-engine en core_engine (pour la compatibilité Python)
    if Path("core-engine").exists():
        if Path("core_engine").exists():
            shutil.rmtree("core_engine")
        os.rename("core-engine", "core_engine")
        print("✅ Dossier renommé: core-engine → core_engine")
    
    return True

def update_init_files():
    """Met à jour les fichiers __init__.py pour inclure tous les agents"""
    
    # Mettre à jour core-engine/__init__.py
    core_init = Path("core-engine") / "__init__.py"
    if core_init.exists():
        content = '''"""
Core Engine - Module principal pour la génération de startups
"""

__version__ = "1.0.0"
__author__ = "AI Business & Legal Engineer"

# Core Engine package
from .agents.finance_agent import FinanceAgent
from .agents.legal_agent import LegalAgent
from .agents.growth_agent import GrowthAgent
from .agents.marketing_agent import MarketingAgent
from .agents.dao_agent import DAOAgent
from .agents.investor_agent import InvestorAgent
from .agents.ceo_agent import CEOAgent
from .agents.fund_agent import FundAgent
from .agents.portfolio_agent import PortfolioAgent
from .agents.business_optimizer_agent import BusinessOptimizerAgent
from .agents.auto_iteration_agent import AutoIterationAgent
from .agents.market_agent import MarketAgent
from .agents.product_feedback_agent import ProductFeedbackAgent
from .agents.infra_agent import InfraAgent
from .agents.dev_backend_agent import DevBackendAgent
from .agents.dev_frontend_agent import DevFrontendAgent

from .logger import get_logger, StartupLogger

__all__ = [
    "FinanceAgent",
    "LegalAgent", 
    "GrowthAgent",
    "MarketingAgent",
    "DAOAgent",
    "InvestorAgent",
    "CEOAgent",
    "FundAgent",
    "PortfolioAgent",
    "BusinessOptimizerAgent",
    "AutoIterationAgent",
    "MarketAgent",
    "ProductFeedbackAgent",
    "InfraAgent",
    "DevBackendAgent",
    "DevFrontendAgent",
    "get_logger", 
    "StartupLogger"
]
'''
        core_init.write_text(content)
        print("   📝 core-engine/__init__.py mis à jour")
    
    # Mettre à jour core-engine/agents/__init__.py
    agents_init = Path("core-engine") / "agents" / "__init__.py"
    if agents_init.exists():
        content = '''"""
Agents - Package contenant tous les agents spécialisés
"""

from .finance_agent import FinanceAgent
from .legal_agent import LegalAgent
from .growth_agent import GrowthAgent
from .marketing_agent import MarketingAgent
from .dao_agent import DAOAgent
from .investor_agent import InvestorAgent
from .ceo_agent import CEOAgent
from .fund_agent import FundAgent
from .portfolio_agent import PortfolioAgent
from .business_optimizer_agent import BusinessOptimizerAgent
from .auto_iteration_agent import AutoIterationAgent
from .market_agent import MarketAgent
from .product_feedback_agent import ProductFeedbackAgent
from .infra_agent import InfraAgent
from .dev_backend_agent import DevBackendAgent
from .dev_frontend_agent import DevFrontendAgent

__all__ = [
    'FinanceAgent', 
    'LegalAgent', 
    'GrowthAgent',
    'MarketingAgent',
    'DAOAgent',
    'InvestorAgent',
    'CEOAgent',
    'FundAgent',
    'PortfolioAgent',
    'BusinessOptimizerAgent',
    'AutoIterationAgent',
    'MarketAgent',
    'ProductFeedbackAgent',
    'InfraAgent',
    'DevBackendAgent',
    'DevFrontendAgent'
]
'''
        agents_init.write_text(content)
        print("   📝 core-engine/agents/__init__.py mis à jour")

def test_imports():
    """Teste que les imports fonctionnent après la migration"""
    print("\n🧪 Test des imports...")
    
    try:
        # Test d'import depuis core_engine
        sys.path.insert(0, str(Path.cwd()))
        
        # Test d'import d'un agent
        from core_engine.agents.finance_agent import FinanceAgent
        print("✅ Import FinanceAgent réussi")
        
        # Test d'import du logger
        from core_engine.logger import get_logger
        print("✅ Import logger réussi")
        
        return True
        
    except ImportError as e:
        print(f"❌ Erreur d'import: {e}")
        return False

def main():
    """Fonction principale"""
    print("🚀 Migration des dossiers core_engine/core-engine")
    print("=" * 50)
    
    # Vérifier que nous sommes dans le bon répertoire
    if not (Path("core_engine").exists() or Path("core-engine").exists()):
        print("❌ Aucun dossier core_engine trouvé dans le répertoire actuel")
        return False
    
    # Créer une branche Git pour la migration
    try:
        subprocess.run(["git", "checkout", "-b", "fix/merge-core-engine-conflicts"], check=True)
        print("✅ Nouvelle branche Git créée: fix/merge-core-engine-conflicts")
    except subprocess.CalledProcessError:
        print("⚠️  Impossible de créer une branche Git (peut-être pas un repo Git)")
    
    # Résoudre les conflits
    if resolve_conflicts():
        print("\n✅ Migration réussie!")
        
        # Tester les imports
        if test_imports():
            print("\n🎉 Tous les tests passent!")
            
            # Commiter les changements
            try:
                subprocess.run(["git", "add", "."], check=True)
                subprocess.run(["git", "commit", "-m", "Fix: Fusion des dossiers core_engine et core-engine"], check=True)
                print("✅ Changements commités")
            except subprocess.CalledProcessError:
                print("⚠️  Impossible de commiter (peut-être pas un repo Git)")
            
            return True
        else:
            print("\n❌ Tests d'import échoués")
            return False
    else:
        print("\n❌ Migration échouée")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)