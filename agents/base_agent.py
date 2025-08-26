import logging
from abc import ABC, abstractmethod
from typing import Dict, Any
import json
from datetime import datetime

class BaseAgent(ABC):
    """Classe de base pour tous les agents"""
    
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.setup_logging()
    
    def setup_logging(self):
        """Configure le logging pour l'agent"""
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            handler.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)
    
    def log_event(self, agent_name: str, action: str, details: Dict[str, Any] = None):
        """Log un événement avec timestamp et détails"""
        timestamp = datetime.now().isoformat()
        log_data = {
            "timestamp": timestamp,
            "agent": agent_name,
            "action": action,
            "details": details or {}
        }
        
        self.logger.info(f"EVENT: {json.dumps(log_data, indent=2)}")
        return log_data
    
    @abstractmethod
    def run(self, **kwargs) -> Dict[str, Any]:
        """Méthode abstraite que tous les agents doivent implémenter"""
        pass
    
    def validate_input(self, **kwargs) -> bool:
        """Validation basique des inputs"""
        return True
    
    def handle_error(self, error: Exception, context: str = "") -> Dict[str, Any]:
        """Gestion standardisée des erreurs"""
        error_data = {
            "error": str(error),
            "error_type": type(error).__name__,
            "context": context,
            "timestamp": datetime.now().isoformat()
        }
        
        self.logger.error(f"ERROR: {json.dumps(error_data, indent=2)}")
        return {
            "status": "error",
            "error": error_data
        }