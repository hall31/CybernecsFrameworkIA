"""
Logger utilitaire pour le core_engine
"""

import logging
import datetime
from typing import Optional

# Configuration du logging de base
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def log_event(agent: str, message: str, level: str = "INFO") -> None:
    """
    Log un événement avec timestamp, nom de l'agent et message
    
    Args:
        agent (str): Nom de l'agent ou composant
        message (str): Message de log
        level (str): Niveau de log (INFO, WARNING, ERROR, DEBUG)
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Codes couleur pour différents niveaux de log
    colors = {
        "INFO": "\033[94m",      # Bleu
        "WARNING": "\033[93m",   # Jaune
        "ERROR": "\033[91m",     # Rouge
        "DEBUG": "\033[90m",     # Gris
        "SUCCESS": "\033[92m"    # Vert
    }
    
    # Code de réinitialisation de couleur
    reset_color = "\033[0m"
    
    # Obtenir la couleur pour le niveau de log
    color = colors.get(level.upper(), colors["INFO"])
    
    # Formater le message
    formatted_message = f"{color}[{level.upper()}]{reset_color} {timestamp} | {agent} | {message}"
    
    # Logger selon le niveau
    logger = logging.getLogger(agent)
    if level.upper() == "INFO":
        logger.info(message)
    elif level.upper() == "WARNING":
        logger.warning(message)
    elif level.upper() == "ERROR":
        logger.error(message)
    elif level.upper() == "DEBUG":
        logger.debug(message)
    else:
        logger.info(message)
    
    # Afficher dans la console avec couleur
    print(formatted_message)

def log_success(agent: str, message: str) -> None:
    """Log un succès"""
    log_event(agent, message, "SUCCESS")

def log_warning(agent: str, message: str) -> None:
    """Log un avertissement"""
    log_event(agent, message, "WARNING")

def log_error(agent: str, message: str) -> None:
    """Log une erreur"""
    log_event(agent, message, "ERROR")

def log_debug(agent: str, message: str) -> None:
    """Log un message de debug"""
    log_event(agent, message, "DEBUG")

class SimpleLogger:
    """Logger simple pour les agents"""
    
    def __init__(self, name: str):
        self.name = name
        self.logger = logging.getLogger(name)
    
    def info(self, message: str):
        """Log un message info"""
        log_event(self.name, message, "INFO")
    
    def success(self, message: str):
        """Log un succès"""
        log_event(self.name, message, "SUCCESS")
    
    def warning(self, message: str):
        """Log un avertissement"""
        log_event(self.name, message, "WARNING")
    
    def error(self, message: str):
        """Log une erreur"""
        log_event(self.name, message, "ERROR")
    
    def debug(self, message: str):
        """Log un message de debug"""
        log_event(self.name, message, "DEBUG")

# Instance globale du logger
db_logger = SimpleLogger("Database")

# Fonctions utilitaires pour la compatibilité
def get_logger(name: str) -> SimpleLogger:
    """Retourne un logger pour le nom donné"""
    return SimpleLogger(name)

def log_step(step: str, message: str) -> None:
    """Log une étape du processus"""
    log_event("Process", f"Étape: {step} - {message}", "INFO")

def log_success_step(step: str, message: str) -> None:
    """Log le succès d'une étape"""
    log_event("Process", f"✅ {step} - {message}", "SUCCESS")

def log_error_step(step: str, message: str) -> None:
    """Log l'échec d'une étape"""
    log_event("Process", f"❌ {step} - {message}", "ERROR")
