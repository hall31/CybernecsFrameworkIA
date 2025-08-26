import logging
import sys
from datetime import datetime
from pathlib import Path

class StartupLogger:
    def __init__(self, name: str = "StartupGenerator"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        
        # Créer le dossier logs s'il n'existe pas
        logs_dir = Path("logs")
        logs_dir.mkdir(exist_ok=True)
        
        # Handler pour la console
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_format = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        console_handler.setFormatter(console_format)
        
        # Handler pour le fichier
        file_handler = logging.FileHandler(
            logs_dir / f"startup_generation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        )
        file_handler.setLevel(logging.DEBUG)
        file_format = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
        )
        file_handler.setFormatter(file_format)
        
        # Ajouter les handlers
        if not self.logger.handlers:
            self.logger.addHandler(console_handler)
            self.logger.addHandler(file_handler)
    
    def info(self, message: str):
        """Log un message d'information"""
        self.logger.info(message)
    
    def debug(self, message: str):
        """Log un message de debug"""
        self.logger.debug(message)
    
    def warning(self, message: str):
        """Log un avertissement"""
        self.logger.warning(message)
    
    def error(self, message: str):
        """Log une erreur"""
        self.logger.error(message)
    
    def critical(self, message: str):
        """Log une erreur critique"""
        self.logger.critical(message)
    
    def log_step(self, step: str, description: str = ""):
        """Log une étape spécifique du processus"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        message = f"🚀 [{timestamp}] {step}"
        if description:
            message += f" - {description}"
        self.info(message)
    
    def log_success(self, action: str, result: str = ""):
        """Log une action réussie"""
        message = f"✅ {action}"
        if result:
            message += f" - {result}"
        self.info(message)
    
    def log_error(self, action: str, error: str = ""):
        """Log une erreur"""
        message = f"❌ {action}"
        if error:
            message += f" - {error}"
        self.error(message)

# Instance globale du logger
logger = StartupLogger()

def get_logger(name: str = None) -> StartupLogger:
    """Retourne une instance du logger"""
    if name:
        return StartupLogger(name)
    return logger