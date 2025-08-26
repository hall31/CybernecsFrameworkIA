"""
Configuration pour gérer les deux structures de dossiers core_engine et core-engine
"""

import os
import sys
from pathlib import Path

# Configuration des chemins
CORE_ENGINE_UNDERSCORE = Path("core_engine")
CORE_ENGINE_DASH = Path("core-engine")

def get_core_engine_path():
    """
    Détermine quel dossier core_engine utiliser
    Priorité: core_engine (underscore) puis core-engine (dash)
    """
    if CORE_ENGINE_UNDERSCORE.exists():
        return CORE_ENGINE_UNDERSCORE
    elif CORE_ENGINE_DASH.exists():
        return CORE_ENGINE_DASH
    else:
        raise FileNotFoundError("Aucun dossier core_engine trouvé")

def setup_imports():
    """
    Configure les imports pour utiliser la bonne structure
    """
    core_path = get_core_engine_path()
    
    # Ajouter le chemin au sys.path
    if str(core_path) not in sys.path:
        sys.path.insert(0, str(core_path))
    
    # Ajouter le chemin parent pour les imports relatifs
    parent_path = core_path.parent
    if str(parent_path) not in sys.path:
        sys.path.insert(0, str(parent_path))
    
    return core_path

def get_agent_class(agent_name):
    """
    Récupère une classe d'agent depuis la bonne structure
    """
    try:
        # Essayer d'abord core_engine (underscore)
        if CORE_ENGINE_UNDERSCORE.exists():
            module = __import__(f"core_engine.agents.{agent_name}", fromlist=[agent_name])
            return getattr(module, agent_name)
    except ImportError:
        pass
    
    try:
        # Essayer core-engine (dash)
        if CORE_ENGINE_DASH.exists():
            # Pour core-engine, on doit gérer le tiret dans le nom
            module_path = CORE_ENGINE_DASH / "agents" / f"{agent_name}.py"
            if module_path.exists():
                # Importer manuellement
                import importlib.util
                spec = importlib.util.spec_from_file_location(agent_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                return getattr(module, agent_name)
    except Exception:
        pass
    
    raise ImportError(f"Impossible d'importer {agent_name} depuis aucune structure")

def get_logger():
    """
    Récupère le logger depuis la bonne structure
    """
    try:
        # Essayer core_engine
        if CORE_ENGINE_UNDERSCORE.exists():
            from core_engine.logger import get_logger
            return get_logger
    except ImportError:
        pass
    
    try:
        # Essayer core-engine
        if CORE_ENGINE_DASH.exists():
            logger_path = CORE_ENGINE_DASH / "logger.py"
            if logger_path.exists():
                import importlib.util
                spec = importlib.util.spec_from_file_location("logger", logger_path)
                logger_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(logger_module)
                return logger_module.get_logger
    except Exception:
        pass
    
    # Fallback vers un logger simple
    import logging
    def simple_logger(name):
        return logging.getLogger(name)
    return simple_logger

# Configuration automatique au chargement du module
CORE_PATH = setup_imports()

# Exports
__all__ = [
    "get_core_engine_path",
    "setup_imports", 
    "get_agent_class",
    "get_logger",
    "CORE_PATH"
]