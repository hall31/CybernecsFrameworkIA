import logging
import json
from typing import Dict, Any, Optional
from datetime import datetime
import uuid

# Import des agents
from agents.investor_agent import InvestorAgent
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import logging
from datetime import datetime
from agents.market_agent import MarketAgent

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Instance globale du MarketAgent
market_agent = MarketAgent()
#!/usr/bin/env python3
"""
Orchestrateur principal pour l'Epic10 - IA Autonome
Coordonne les 3 agents: ProductFeedbackAgent, AutoIterationAgent, BusinessOptimizerAgent
"""

import json
import logging
import asyncio
from typing import Dict, List, Any, Optional
from datetime import datetime
import os

# Import des agents
from agents.product_feedback_agent import ProductFeedbackAgent
from agents.auto_iteration_agent import AutoIterationAgent
from agents.business_optimizer_agent import BusinessOptimizerAgent
from flask import Flask, jsonify, request
from flask_cors import CORS
import logging
from datetime import datetime
import json

# Import des agents


# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class StartupOrchestrator:
    """
    Orchestrateur principal pour la création et l'évaluation de startups
    """
    
    def __init__(self):
        self.investor_agent = InvestorAgent()
        self.logger = logging.getLogger(__name__)
    
    def create_startup(self, idea: str, project_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Création complète d'une startup avec évaluation investisseur
        
        Args:
            idea: Idée de startup
            project_id: ID du projet (généré automatiquement si non fourni)
            
        Returns:
            Dict complet avec tous les résultats des agents
        """
        try:
            if not project_id:
                project_id = str(uuid.uuid4())
            
            self.logger.info(f"Début création startup: {idea} (ID: {project_id})")
            
            # Simulation des données des autres agents (en production, ces données viendraient des vrais agents)
            finance_data = self._simulate_finance_agent(idea)
            growth_data = self._simulate_growth_agent(idea)
            optimizer_data = self._simulate_business_optimizer(idea)
            
            # Appel de l'InvestorAgent pour évaluation et décision
            self.logger.info(f"Appel InvestorAgent pour le projet {project_id}")
            investor_result = self.investor_agent.run(
                project_id=project_id,
                finance=finance_data,
                growth=growth_data,
                optimizer=optimizer_data
            )
            
            # Construction du résultat final
            result = {
                "project_id": project_id,
                "idea": idea,
                "created_at": datetime.now().isoformat(),
                "status": "completed",
                "agents": {
                    "finance": finance_data,
                    "growth": growth_data,
                    "optimizer": optimizer_data,
                    "investor": investor_result
                },
                "summary": {
                    "valuation": investor_result.get("valuation", "N/A"),
                    "decision": investor_result.get("decision", "N/A"),
                    "confidence": investor_result.get("confidence_score", 0.0),
                    "next_funding": investor_result.get("next_funding", "N/A")
                }
            }
            
            self.logger.info(f"Startup créée avec succès: {project_id}")
            return result
            
        except Exception as e:
            self.logger.error(f"Erreur création startup: {str(e)}")
            return self._get_error_response(idea, project_id, str(e))
    
    def _simulate_finance_agent(self, idea: str) -> Dict[str, Any]:
        """Simulation des données du FinanceAgent"""
        # En production, ces données viendraient du vrai FinanceAgent
        return {
            "current_revenue": 12000,  # 12k € par mois
            "projected_revenue": 180000,  # 180k € par an
            "stripe_revenue": 15000,  # Données Stripe réelles
            "monthly_costs": 8000,
            "profit_margin": 0.33,
            "cash_flow": 4000
        }
    
    def _simulate_growth_agent(self, idea: str) -> Dict[str, Any]:
        """Simulation des données du GrowthAgent"""
        # En production, ces données viendraient du vrai GrowthAgent
        return {
            "cac": 45,  # Customer Acquisition Cost
            "ltv": 500,  # Lifetime Value
            "ctr": 0.08,  # Click Through Rate
            "conversion_rate": 0.025,  # 2.5%
            "monthly_growth": 0.15,  # 15% par mois
            "user_retention": 0.85
        }
    
    def _simulate_business_optimizer(self, idea: str) -> Dict[str, Any]:
        """Simulation des données du BusinessOptimizerAgent"""
        # En production, ces données viendraient du vrai BusinessOptimizerAgent
        return {
            "churn_rate": 0.03,  # 3% de churn
            "optimization_score": 0.78,
            "recommended_actions": [
                "Augmenter le budget marketing de 20%",
                "Optimiser la page de conversion",
                "Améliorer l'onboarding utilisateur"
            ],
            "predicted_improvement": 0.25  # 25% d'amélioration
        }
    
    def _get_error_response(self, idea: str, project_id: str, error_message: str) -> Dict[str, Any]:
        """Retourne une réponse d'erreur standardisée"""
        return {
            "project_id": project_id,
            "idea": idea,
            "created_at": datetime.now().isoformat(),
            "status": "error",
            "error": error_message,
            "agents": {
                "finance": {},
                "growth": {},
                "optimizer": {},
                "investor": {
                    "valuation": "Erreur",
                    "kpis": {"MRR": "N/A", "CAC": "N/A", "LTV": "N/A", "Churn": "N/A"},
                    "decision": "Erreur d'évaluation",
                    "next_funding": "Non disponible"
                }
            }
        }
    
    def get_startup_details(self, project_id: str) -> Dict[str, Any]:
        """
        Récupère les détails d'une startup existante
        
        Args:
            project_id: ID du projet
            
        Returns:
            Dict avec les détails de la startup
        """
        # En production, cette méthode récupérerait les données depuis une base de données
        self.logger.info(f"Récupération détails startup: {project_id}")
        
        # Simulation d'une startup existante
        return {
            "project_id": project_id,
            "idea": "SaaS marketplace innovant",
            "created_at": datetime.now().isoformat(),
            "status": "active",
            "agents": {
                "finance": self._simulate_finance_agent("SaaS marketplace"),
                "growth": self._simulate_growth_agent("SaaS marketplace"),
                "optimizer": self._simulate_business_optimizer("SaaS marketplace"),
                "investor": {
                    "valuation": "2.5M €",
                    "kpis": {
                        "MRR": "15k €",
                        "CAC": "45 €",
                        "LTV": "500 €",
                        "Churn": "3%"
                    },
                    "decision": "Investir",
                    "next_funding": "100k € en crédits cloud + pub",
                    "confidence_score": 0.85
                }
            }
        }

# Instance globale de l'orchestrateur
orchestrator = StartupOrchestrator()

def create_startup_endpoint(idea: str) -> Dict[str, Any]:
    """
    Endpoint principal pour créer une startup
    
    Args:
        idea: Idée de startup
        
    Returns:
        Résultat complet de la création
    """
    return orchestrator.create_startup(idea)

def get_startup_endpoint(project_id: str) -> Dict[str, Any]:
    """
    Endpoint pour récupérer les détails d'une startup
    
    Args:
        project_id: ID du projet
        
    Returns:
        Détails de la startup
    """
    return orchestrator.get_startup_details(project_id)

if __name__ == "__main__":
    # Test de l'orchestrateur
    test_idea = "SaaS marketplace pour freelances"
    result = create_startup_endpoint(test_idea)
    
    print("=== Résultat de création de startup ===")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    
    # Test de récupération
    if result.get("project_id"):
        details = get_startup_endpoint(result["project_id"])
        print("\n=== Détails de la startup ===")
        print(json.dumps(details, indent=2, ensure_ascii=False))

class Epic10Orchestrator:
    """
    Orchestrateur principal pour l'Epic10 - IA Autonome
    """
    
    def __init__(self, openai_api_key: str = None):
        self.openai_api_key = openai_api_key or os.getenv("OPENAI_API_KEY")
        
        # Initialisation des agents
        self.product_feedback_agent = ProductFeedbackAgent(self.openai_api_key)
        self.auto_iteration_agent = AutoIterationAgent(self.openai_api_key)
        self.business_optimizer_agent = BusinessOptimizerAgent(self.openai_api_key)
        
        logger.info("Epic10Orchestrator initialisé avec succès")
    
    def log_event(self, event_type: str, message: str, data: Dict[str, Any] = None):
        """Log un événement avec timestamp et données"""
        timestamp = datetime.now().isoformat()
        log_entry = {
            "timestamp": timestamp,
            "event_type": event_type,
            "message": message,
            "data": data or {}
        }
        
        logger.info(f"[{timestamp}] {event_type}: {message}")
        
        # TODO: Sauvegarder dans base de données ou système de monitoring
        return log_entry
    
    async def run_product_feedback_analysis(self, project_id: str) -> Dict[str, Any]:
        """
        Exécute l'analyse du feedback produit
        """
        try:
            logger.info(f"Démarrage analyse feedback pour projet {project_id}")
            
            # Exécution de l'agent
            feedback_result = self.product_feedback_agent.run(project_id)
            
            if feedback_result.get("status") == "failed":
                raise Exception(f"Échec analyse feedback: {feedback_result.get('error')}")
            
            self.log_event(
                "ProductFeedbackAgent", 
                "Analyse feedback terminée avec succès",
                {"project_id": project_id, "issues_count": len(feedback_result.get("issues", []))}
            )
            
            return feedback_result
            
        except Exception as e:
            error_msg = f"Erreur dans analyse feedback: {str(e)}"
            logger.error(error_msg)
            self.log_event("ProductFeedbackAgent", f"ERREUR: {error_msg}")
            
            return {
                "error": error_msg,
                "timestamp": datetime.now().isoformat(),
                "status": "failed"
            }
    
    async def run_auto_iteration(self, project_id: str, feedback: Dict[str, Any]) -> Dict[str, Any]:
        """
        Exécute l'itération automatique basée sur le feedback
        """
        try:
            logger.info(f"Démarrage itération automatique pour projet {project_id}")
            
            # Exécution de l'agent
            iteration_result = self.auto_iteration_agent.run(project_id, feedback)
            
            if iteration_result.get("status") == "failed":
                raise Exception(f"Échec itération automatique: {iteration_result.get('error')}")
            
            self.log_event(
                "AutoIterationAgent",
                "Itération automatique terminée avec succès",
                {
                    "project_id": project_id,
                    "user_stories_count": len(iteration_result.get("user_stories", [])),
                    "sprints_count": len(iteration_result.get("roadmap", {}).get("sprints", []))
                }
            )
            
            return iteration_result
            
        except Exception as e:
            error_msg = f"Erreur dans itération automatique: {str(e)}"
            logger.error(error_msg)
            self.log_event("AutoIterationAgent", f"ERREUR: {error_msg}")
            
            return {
                "error": error_msg,
                "timestamp": datetime.now().isoformat(),
                "status": "failed"
            }
    
    async def run_business_optimization(self, project_id: str, finance: Dict[str, Any] = None, growth: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Exécute l'optimisation business
        """
        try:
            logger.info(f"Démarrage optimisation business pour projet {project_id}")
            
            # Exécution de l'agent
            optimization_result = self.business_optimizer_agent.run(project_id, finance, growth)
            
            if optimization_result.get("status") == "failed":
                raise Exception(f"Échec optimisation business: {optimization_result.get('error')}")
            
            self.log_event(
                "BusinessOptimizerAgent",
                "Optimisation business terminée avec succès",
                {
                    "project_id": project_id,
                    "pricing_changes_count": len(optimization_result.get("pricing_changes", [])),
                    "budget_recommendations_count": len(optimization_result.get("ads_budget_shift", []))
                }
            )
            
            return optimization_result
            
        except Exception as e:
            error_msg = f"Erreur dans optimisation business: {str(e)}"
            logger.error(error_msg)
            self.log_event("BusinessOptimizerAgent", f"ERREUR: {error_msg}")
            
            return {
                "error": error_msg,
                "timestamp": datetime.now().isoformat(),
                "status": "failed"
            }
    
    async def run_complete_epic10(self, project_id: str, idea: str, finance: Dict[str, Any] = None, growth: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Exécute l'Epic10 complet avec les 3 agents
        """
        try:
            start_time = datetime.now()
            logger.info(f"Démarrage Epic10 complet pour projet {project_id}: {idea}")
            
            self.log_event("Epic10Orchestrator", f"Démarrage Epic10 pour: {idea}", {"project_id": project_id, "idea": idea})
            
            # 1. Analyse du feedback produit
            logger.info("Étape 1/3: Analyse du feedback produit")
            feedback_result = await self.run_product_feedback_analysis(project_id)
            
            if feedback_result.get("status") == "failed":
                raise Exception("Échec de l'analyse du feedback")
            
            # 2. Itération automatique
            logger.info("Étape 2/3: Itération automatique")
            iteration_result = await self.run_auto_iteration(project_id, feedback_result)
            
            if iteration_result.get("status") == "failed":
                raise Exception("Échec de l'itération automatique")
            
            # 3. Optimisation business
            logger.info("Étape 3/3: Optimisation business")
            optimization_result = await self.run_business_optimization(project_id, finance, growth)
            
            if optimization_result.get("status") == "failed":
                raise Exception("Échec de l'optimisation business")
            
            # 4. Résultat final
            end_time = datetime.now()
            execution_time = (end_time - start_time).total_seconds()
            
            epic10_result = {
                "project_id": project_id,
                "idea": idea,
                "timestamp": datetime.now().isoformat(),
                "execution_time_seconds": execution_time,
                "status": "completed",
                "epic10_version": "1.0.0",
                "agents_executed": [
                    "ProductFeedbackAgent",
                    "AutoIterationAgent", 
                    "BusinessOptimizerAgent"
                ],
                "results": {
                    "feedback": feedback_result,
                    "iteration": iteration_result,
                    "optimizer": optimization_result
                },
                "summary": {
                    "total_issues_identified": len(feedback_result.get("issues", [])),
                    "total_user_stories_generated": len(iteration_result.get("user_stories", [])),
                    "total_optimizations_proposed": len(optimization_result.get("pricing_changes", [])) + len(optimization_result.get("ads_budget_shift", [])),
                    "estimated_roi_improvement": optimization_result.get("roi_projection", "N/A")
                }
            }
            
            self.log_event(
                "Epic10Orchestrator",
                "Epic10 terminé avec succès",
                {
                    "project_id": project_id,
                    "execution_time": execution_time,
                    "total_improvements": epic10_result["summary"]["total_user_stories_generated"]
                }
            )
            
            logger.info(f"Epic10 terminé avec succès en {execution_time:.2f} secondes")
            return epic10_result
            
        except Exception as e:
            error_msg = f"Erreur dans Epic10 complet: {str(e)}"
            logger.error(error_msg)
            self.log_event("Epic10Orchestrator", f"ERREUR: {error_msg}")
            
            return {
                "error": error_msg,
                "timestamp": datetime.now().isoformat(),
                "status": "failed",
                "project_id": project_id,
                "idea": idea
            }
    
    def create_startup_with_epic10(self, idea: str, project_id: str = None) -> Dict[str, Any]:
        """
        Crée une startup complète avec l'Epic10
        """
        if not project_id:
            project_id = f"startup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        try:
            logger.info(f"Création startup avec Epic10: {idea}")
            
            # Simulation des données financières et de croissance
            mock_finance = {
                "revenue": {"mrr": 5000, "ltv": 150, "cac": 40, "churn_rate": 0.06},
                "pricing": {"starter": {"price": 25}, "pro": {"price": 69}}
            }
            
            mock_growth = {
                "advertising": {
                    "google_ads": {"budget": 2000, "roas": 2.5},
                    "linkedin_ads": {"budget": 1000, "roas": 3.0}
                }
            }
            
            # Exécution synchrone pour la compatibilité
            epic10_result = asyncio.run(
                self.run_complete_epic10(project_id, idea, mock_finance, mock_growth)
            )
            
            # Résultat final pour /create-startup
            startup_result = {
                "project_id": project_id,
                "idea": idea,
                "status": "startup_created_with_epic10",
                "timestamp": datetime.now().isoformat(),
                "epic10_results": epic10_result,
                "next_steps": [
                    "Analyser le feedback utilisateur",
                    "Implémenter les améliorations prioritaires",
                    "Appliquer les optimisations business",
                    "Monitorer les métriques de performance"
                ]
            }
            
            return startup_result
            
        except Exception as e:
            error_msg = f"Erreur création startup avec Epic10: {str(e)}"
            logger.error(error_msg)
            
            return {
                "error": error_msg,
                "timestamp": datetime.now().isoformat(),
                "status": "failed",
                "project_id": project_id,
                "idea": idea
            }

# API endpoints pour l'intégration
def create_startup_endpoint(idea: str, project_id: str = None) -> Dict[str, Any]:
    """
    Endpoint principal pour créer une startup avec Epic10
    """
    orchestrator = Epic10Orchestrator()
    return orchestrator.create_startup_with_epic10(idea, project_id)

# Test et démonstration
if __name__ == "__main__":
    print("🚀 Epic10 - IA Autonome pour Mon ShipFast")
    print("=" * 50)
    
    # Test de l'orchestrateur
    orchestrator = Epic10Orchestrator()
    
    # Création d'une startup test
    test_idea = "SaaS marketplace pour freelances"
    result = orchestrator.create_startup_with_epic10(test_idea)
    
    if result.get("status") == "startup_created_with_epic10":
        print(f"✅ Startup créée avec succès: {test_idea}")
        print(f"📊 Résultats Epic10:")
        print(f"   - Issues identifiées: {result['epic10_results']['summary']['total_issues_identified']}")
        print(f"   - User stories générées: {result['epic10_results']['summary']['total_user_stories_generated']}")
        print(f"   - Optimisations proposées: {result['epic10_results']['summary']['total_optimizations_proposed']}")
        print(f"   - ROI attendu: {result['epic10_results']['summary']['estimated_roi_improvement']}")
    else:
        print(f"❌ Erreur: {result.get('error')}")
    
    print("\n🎯 Epic10 prêt pour l'intégration dans /create-startup!")
# Initialisation de Flask
app = Flask(__name__)
CORS(app)

# Initialisation des agents
portfolio_agent = PortfolioAgent()

@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint de santé de l'API"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "Startup Tokenization Marketplace API"
    })

@app.route('/market', methods=['GET'])
def get_market():
    """
    Endpoint principal pour récupérer toutes les startups tokenisées listées
    GET /market
    """
    try:
        logger.info("GET /market - Récupération des données du marketplace")
        
        # Appel du MarketAgent
        market_data = market_agent.run()
        
        return jsonify({
            "success": True,
            "data": market_data,
        "service": "AI Portfolio Manager API"
    })

@app.route('/portfolio', methods=['GET'])
def get_portfolio():
    """Endpoint principal pour récupérer le tableau de bord du portefeuille"""
    try:
        logger.info("Demande d'analyse du portefeuille reçue")
        
        # Appel du PortfolioAgent
        portfolio_data = portfolio_agent.run()
        
        if "error" in portfolio_data:
            logger.error(f"Erreur lors de l'analyse: {portfolio_data['error']}")
            return jsonify({
                "success": False,
                "error": portfolio_data["error"],
                "timestamp": datetime.now().isoformat()
            }), 500
        
        logger.info("Analyse du portefeuille terminée avec succès")
        
        return jsonify({
            "success": True,
            "data": portfolio_data,
            "timestamp": datetime.now().isoformat()
        })
        
    except Exception as e:
        logger.error(f"Erreur lors de la récupération du marché: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }), 500

@app.route('/market/token/<symbol>', methods=['GET'])
def get_token_details(symbol):
    """
    Récupère les détails d'un token spécifique
    GET /market/token/<symbol>
    """
    try:
        logger.info(f"GET /market/token/{symbol} - Récupération des détails du token")
        
        token_details = market_agent.get_token_details(symbol)
        
        if not token_details:
            return jsonify({
                "success": False,
                "error": f"Token {symbol} non trouvé",
                "timestamp": datetime.now().isoformat()
            }), 404
        
        return jsonify({
            "success": True,
            "data": token_details,
        error_msg = f"Erreur inattendue: {str(e)}"
        logger.error(error_msg)
        return jsonify({
            "success": False,
            "error": error_msg,
            "timestamp": datetime.now().isoformat()
        }), 500

@app.route('/portfolio/summary', methods=['GET'])
def get_portfolio_summary():
    """Endpoint pour récupérer un résumé du portefeuille (sans nouvelle analyse)"""
    try:
        summary = portfolio_agent.get_portfolio_summary()
        return jsonify({
            "success": True,
            "data": summary,
            "timestamp": datetime.now().isoformat()
        })
        
    except Exception as e:
        logger.error(f"Erreur lors de la récupération du token {symbol}: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }), 500

@app.route('/market/stats', methods=['GET'])
def get_market_stats():
    """
    Récupère les statistiques globales du marché
    GET /market/stats
    """
    try:
        logger.info("GET /market/stats - Récupération des statistiques du marché")
        
        stats = market_agent.get_market_stats()
        
        return jsonify({
            "success": True,
            "data": stats,
            "timestamp": datetime.now().isoformat()
        })
        
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des statistiques: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }), 500

@app.route('/market/orderbook/<symbol>', methods=['GET'])
def get_order_book(symbol):
    """
    Récupère l'order book d'un token spécifique
    GET /market/orderbook/<symbol>
    """
    try:
        logger.info(f"GET /market/orderbook/{symbol} - Récupération de l'order book")
        
        token = market_agent.get_token_details(symbol)
        if not token:
            return jsonify({
                "success": False,
                "error": f"Token {symbol} non trouvé",
                "timestamp": datetime.now().isoformat()
            }), 404
        
        order_book = token.get("order_book", {})
        
        return jsonify({
            "success": True,
            "data": {
                "symbol": symbol,
                "order_book": order_book,
                "timestamp": datetime.now().isoformat()
            }
        })
        
    except Exception as e:
        logger.error(f"Erreur lors de la récupération de l'order book: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }), 500

@app.route('/market/price-history/<symbol>', methods=['GET'])
def get_price_history(symbol):
    """
    Récupère l'historique des prix d'un token
    GET /market/price-history/<symbol>?days=30
    """
    try:
        days = request.args.get('days', 30, type=int)
        logger.info(f"GET /market/price-history/{symbol} - Récupération de l'historique sur {days} jours")
        
        token = market_agent.get_token_details(symbol)
        if not token:
            return jsonify({
                "success": False,
                "error": f"Token {symbol} non trouvé",
                "timestamp": datetime.now().isoformat()
            }), 404
        
        price_history = market_agent.generate_price_history(symbol, days)
        
        return jsonify({
            "success": True,
            "data": {
                "symbol": symbol,
                "price_history": price_history,
                "period_days": days,
                "timestamp": datetime.now().isoformat()
            }
        })
        
    except Exception as e:
        logger.error(f"Erreur lors de la récupération de l'historique des prix: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e),
        error_msg = f"Erreur lors de la récupération du résumé: {str(e)}"
        logger.error(error_msg)
        return jsonify({
            "success": False,
            "error": error_msg,
            "timestamp": datetime.now().isoformat()
        }), 500

@app.route('/portfolio/startups', methods=['GET'])
def get_startups():
    """Endpoint pour récupérer la liste des startups"""
    try:
        startups = portfolio_agent.get_all_startups()
        return jsonify({
            "success": True,
            "data": {
                "startups": startups,
                "total": len(startups),
                "timestamp": datetime.now().isoformat()
            }
        })
        
    except Exception as e:
        error_msg = f"Erreur lors de la récupération des startups: {str(e)}"
        logger.error(error_msg)
        return jsonify({
            "success": False,
            "error": error_msg,
            "timestamp": datetime.now().isoformat()
        }), 500

@app.route('/portfolio/startup/<startup_id>', methods=['GET'])
def get_startup(startup_id):
    """Endpoint pour récupérer une startup spécifique"""
    try:
        startups = portfolio_agent.get_all_startups()
        startup = next((s for s in startups if s["id"] == startup_id), None)
        
        if not startup:
            return jsonify({
                "success": False,
                "error": f"Startup {startup_id} non trouvée",
                "timestamp": datetime.now().isoformat()
            }), 404
        
        # Évaluation de la startup
        evaluated_startup = portfolio_agent.evaluate_startup(startup)
        
        return jsonify({
            "success": True,
            "data": evaluated_startup,
            "timestamp": datetime.now().isoformat()
        })
        
    except Exception as e:
        error_msg = f"Erreur lors de la récupération de la startup: {str(e)}"
        logger.error(error_msg)
        return jsonify({
            "success": False,
            "error": error_msg,
            "timestamp": datetime.now().isoformat()
        }), 500

@app.route('/portfolio/analysis', methods=['POST'])
def analyze_portfolio():
    """Endpoint pour forcer une nouvelle analyse du portefeuille"""
    try:
        logger.info("Demande de nouvelle analyse du portefeuille")
        
        # Force une nouvelle analyse
        portfolio_data = portfolio_agent.run()
        
        if "error" in portfolio_data:
            logger.error(f"Erreur lors de l'analyse: {portfolio_data['error']}")
            return jsonify({
                "success": False,
                "error": portfolio_data["error"],
                "timestamp": datetime.now().isoformat()
            }), 500
        
        logger.info("Nouvelle analyse du portefeuille terminée avec succès")
        
        return jsonify({
            "success": True,
            "data": portfolio_data,
            "message": "Analyse du portefeuille mise à jour",
            "timestamp": datetime.now().isoformat()
        })
        
    except Exception as e:
        error_msg = f"Erreur lors de l'analyse: {str(e)}"
        logger.error(error_msg)
        return jsonify({
            "success": False,
            "error": error_msg,
            "timestamp": datetime.now().isoformat()
        }), 500

@app.errorhandler(404)
def not_found(error):
    """Gestionnaire d'erreur 404"""
    return jsonify({
        "success": False,
        "error": "Endpoint non trouvé",
        "timestamp": datetime.now().isoformat()
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Gestionnaire d'erreur 500"""
    return jsonify({
        "success": False,
        "error": "Erreur interne du serveur",
        "timestamp": datetime.now().isoformat()
    }), 500

if __name__ == '__main__':
    logger.info("🚀 Démarrage de l'API Startup Tokenization Marketplace")
    logger.info("📊 MarketAgent initialisé et prêt")
    logger.info("🌐 Serveur démarré sur http://localhost:5000")
    
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=False
    )
    logger.info("Démarrage de l'AI Portfolio Manager API")
    logger.info("Endpoints disponibles:")
    logger.info("  GET  /health - Vérification de santé")
    logger.info("  GET  /portfolio - Tableau de bord complet")
    logger.info("  GET  /portfolio/summary - Résumé du portefeuille")
    logger.info("  GET  /portfolio/startups - Liste des startups")
    logger.info("  GET  /portfolio/startup/<id> - Détails d'une startup")
    logger.info("  POST /portfolio/analysis - Force une nouvelle analyse")
    
    debug_mode = os.environ.get("FLASK_DEBUG", "False").lower() in ("1", "true", "yes")
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=debug_mode
    )
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router
from api.websocket import websocket_endpoint
from core.database import engine, Base
import asyncio

app = FastAPI(
    title="Epic6 Core Engine",
    description="Backend FastAPI pour la gestion des projets startup",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En production, spécifier les domaines autorisés
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(router, prefix="/api/v1")

# WebSocket endpoint for project logs
@app.websocket("/ws/logs/{project_id}")
async def websocket_logs(websocket: WebSocket, project_id: str):
    from uuid import UUID
    try:
        project_uuid = UUID(project_id)
        await websocket_endpoint(websocket, project_uuid)
    except ValueError:
        await websocket.close(code=4000, reason="Invalid project ID")

# Health check
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "epic6-core-engine"}

# Startup event - create tables
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Shutdown event
@app.on_event("shutdown")
async def shutdown():
    await engine.dispose()
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.ceo_agent import CEOAgent
from agents.fund_agent import FundAgent
from utils.logger import log_event
from typing import List

app = FastAPI(title="Core Engine", description="Startup Orchestrator with CEO Agent & Fund Management")

class StartupRequest(BaseModel):
    idea: str

class StartupResponse(BaseModel):
    roadmap: dict
    message: str

class FundRequest(BaseModel):
    startups: List[str]

class FundResponse(BaseModel):
    fund_address: str
    fund_symbol: str
    composition: List[dict]
    nav: str
    message: str

# Initialize agents
ceo_agent = CEOAgent()
fund_agent = FundAgent()

@app.get("/")
async def root():
    return {"message": "Core Engine - Startup Orchestrator with Fund Management"}

@app.post("/create-startup", response_model=StartupResponse)
async def create_startup(request: StartupRequest):
    try:
        log_event("main", f"Received startup idea: {request.idea}")
        
        # Generate roadmap
        roadmap = ceo_agent.run(request.idea)
        
        log_event("main", f"Generated roadmap for: {request.idea}")
        
        return StartupResponse(
            roadmap=roadmap,
            message=f"Roadmap generated successfully for: {request.idea}"
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to generate roadmap due to an internal error.")

@app.post("/funds", response_model=FundResponse)
async def create_fund(request: FundRequest):
    """
    Create a new AI Startup Fund (ETF)
    
    Args:
        request: FundRequest containing list of startup tokens
        
    Returns:
        FundResponse with fund details
    """
    try:
        log_event("main", f"Creating fund with startups: {request.startups}")
        
        # Validate input
        if len(request.startups) < 2:
            raise HTTPException(
                status_code=400, 
                detail="Minimum 2 startups required to create a fund"
            )
        
        # Create fund using FundAgent
        fund = fund_agent.run(request.startups)
        
        log_event("main", f"Fund created successfully: {fund['fund_symbol']}")
        
        return FundResponse(
            fund_address=fund["fund_address"],
            fund_symbol=fund["fund_symbol"],
            composition=fund["composition"],
            nav=fund["nav"],
            message=f"AI Startup Fund {fund['fund_symbol']} created successfully"
        )
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        log_event("main", f"Error creating fund: {str(e)}", "ERROR")
        raise HTTPException(status_code=500, detail="Failed to create fund due to an internal error.")

@app.get("/funds")
async def get_all_funds():
    """
    Get all active funds
    
    Returns:
        List of all created funds
    """
    try:
        funds = fund_agent.get_all_funds()
        log_event("main", f"Retrieved {len(funds)} funds")
        
        return {
            "funds": funds,
            "total_count": len(funds),
            "active_count": len([f for f in funds if f["status"] == "active"])
        }
        
    except Exception as e:
        log_event("main", f"Error retrieving funds: {str(e)}", "ERROR")
        raise HTTPException(status_code=500, detail="Failed to retrieve funds due to an internal error.")

@app.get("/funds/{fund_symbol}")
async def get_fund_by_symbol(fund_symbol: str):
    """
    Get fund details by symbol
    
    Args:
        fund_symbol: Fund symbol (e.g., ETF001)
        
    Returns:
        Fund details
    """
    try:
        fund = fund_agent.get_fund_by_symbol(fund_symbol)
        
        if not fund:
            raise HTTPException(status_code=404, detail=f"Fund {fund_symbol} not found")
        
        log_event("main", f"Retrieved fund: {fund_symbol}")
        return fund
        
    except HTTPException:
        raise
    except Exception as e:
        log_event("main", f"Error retrieving fund {fund_symbol}: {str(e)}", "ERROR")
        raise HTTPException(status_code=500, detail="Failed to retrieve fund due to an internal error.")

@app.put("/funds/{fund_symbol}/nav")
async def update_fund_nav(fund_symbol: str, nav: str):
    """
    Update fund NAV
    
    Args:
        fund_symbol: Fund symbol
        nav: New NAV value
        
    Returns:
        Success message
    """
    try:
        success = fund_agent.update_fund_nav(fund_symbol, nav)
        
        if not success:
            raise HTTPException(status_code=404, detail=f"Fund {fund_symbol} not found")
        
        log_event("main", f"Updated NAV for fund {fund_symbol}: {nav}")
        return {"message": f"NAV updated successfully for {fund_symbol}"}
        
    except HTTPException:
        raise
    except Exception as e:
        log_event("main", f"Error updating NAV for fund {fund_symbol}: {str(e)}", "ERROR")
        raise HTTPException(status_code=500, detail="Failed to update NAV due to an internal error.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)