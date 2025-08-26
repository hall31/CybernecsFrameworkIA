import logging
from typing import Dict, Any


class BaseAgent:
    """
    Classe de base pour tous les agents du système
    """
    
    def __init__(self, name: str):
        self.name = name
        self.logger = logging.getLogger(name)
        
        # Configuration du logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    
    def log_event(self, agent_name: str, message: str):
        """
        Log un événement avec le nom de l'agent
        
        Args:
            agent_name: Nom de l'agent qui génère l'événement
            message: Message à logger
        """
        self.logger.info(f"[{agent_name}] {message}")
    
    def run(self, *args, **kwargs) -> Dict[str, Any]:
        """
        Méthode abstraite à implémenter par les agents enfants
        
        Returns:
            Dict contenant le résultat de l'exécution
        """
        raise NotImplementedError("La méthode run doit être implémentée par les classes enfants")