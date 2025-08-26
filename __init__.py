"""
Package principal pour la génération automatique de startups
"""

__version__ = "1.0.0"
__author__ = "AI Business & Legal Engineer"

# Import depuis core_engine (structure principale)
try:
    from core_engine.agents.finance_agent import FinanceAgent
    from core_engine.agents.legal_agent import LegalAgent
    from core_engine.agents.growth_agent import GrowthAgent
    from core_engine.agents.marketing_agent import MarketingAgent
    from core_engine.agents.dao_agent import DAOAgent
    from core_engine.agents.investor_agent import InvestorAgent
    from core_engine.agents.ceo_agent import CEOAgent
    from core_engine.agents.fund_agent import FundAgent
    from core_engine.agents.portfolio_agent import PortfolioAgent
    from core_engine.agents.business_optimizer_agent import BusinessOptimizerAgent
    from core_engine.agents.auto_iteration_agent import AutoIterationAgent
    from core_engine.agents.market_agent import MarketAgent
    from core_engine.agents.product_feedback_agent import ProductFeedbackAgent
    from core_engine.agents.infra_agent import InfraAgent
    from core_engine.agents.dev_backend_agent import DevBackendAgent
    from core_engine.agents.dev_frontend_agent import DevFrontendAgent
    
    from core_engine.logger import get_logger, StartupLogger
    
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
    
except ImportError:
    # Fallback vers core-engine si core_engine n'est pas disponible
    try:
        from core-engine.agents.finance_agent import FinanceAgent
        from core-engine.agents.legal_agent import LegalAgent
        from core-engine.agents.growth_agent import GrowthAgent
        from core-engine.agents.marketing_agent import MarketingAgent
        from core-engine.agents.dao_agent import DAOAgent
        from core-engine.agents.investor_agent import InvestorAgent
        from core-engine.agents.ceo_agent import CEOAgent
        from core-engine.agents.fund_agent import FundAgent
        from core-engine.agents.portfolio_agent import PortfolioAgent
        from core-engine.agents.business_optimizer_agent import BusinessOptimizerAgent
        from core-engine.agents.auto_iteration_agent import AutoIterationAgent
        from core-engine.agents.market_agent import MarketAgent
        from core-engine.agents.product_feedback_agent import ProductFeedbackAgent
        from core-engine.agents.infra_agent import InfraAgent
        from core-engine.agents.dev_backend_agent import DevBackendAgent
        from core-engine.agents.dev_frontend_agent import DevFrontendAgent
        
        from core-engine.logger import get_logger, StartupLogger
        
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
        
    except ImportError as e:
        print(f"Warning: Impossible d'importer depuis core_engine ou core-engine: {e}")
        __all__ = []