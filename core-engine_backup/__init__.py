"""
Core Engine - Module principal pour la génération de startups
"""

__version__ = "1.0.0"
__author__ = "AI Marketing Engineer"

from .agents.marketing_agent import MarketingAgent
from .logger import get_logger, StartupLogger

__all__ = [
    "MarketingAgent",
    "get_logger", 
    "StartupLogger"
]