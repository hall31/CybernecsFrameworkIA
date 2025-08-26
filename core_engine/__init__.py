"""
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
