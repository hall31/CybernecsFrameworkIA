import json
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
import openai
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

class BusinessOptimizerAgent:
    """
    Agent d'optimisation business
    Analyse les métriques financières et de croissance pour proposer des optimisations
    """
    
    def __init__(self, openai_api_key: str = None):
        self.openai_api_key = openai_api_key
        if openai_api_key:
            openai.api_key = openai_api_key
            self.llm = OpenAI(temperature=0.1, openai_api_key=openai_api_key)
        else:
            self.llm = None
        
        # Configuration du logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        # Seuils d'optimisation
        self.optimization_thresholds = {
            "cac_threshold": 50,  # € par acquisition client
            "ltv_threshold": 200,  # € valeur vie client
            "churn_threshold": 0.05,  # 5% de churn max
            "roi_min_threshold": 3.0  # ROI minimum 3:1
        }
    
    def log_event(self, agent_name: str, message: str):
        """Log un événement avec timestamp"""
        timestamp = datetime.now().isoformat()
        self.logger.info(f"[{timestamp}] {agent_name}: {message}")
    
    def collect_financial_metrics(self, project_id: str) -> Dict[str, Any]:
        """
        Collecte les métriques financières depuis Stripe et autres sources
        """
        # TODO: Intégrer avec vraies APIs (Stripe, Google Analytics, etc.)
        mock_finance = {
            "revenue": {
                "mrr": 12500,  # Monthly Recurring Revenue
                "arr": 150000,  # Annual Recurring Revenue
                "growth_rate": 0.15,  # 15% croissance mensuelle
                "churn_rate": 0.08,  # 8% de churn
                "ltv": 180,  # Lifetime Value par client
                "cac": 45  # Customer Acquisition Cost
            },
            "pricing": {
                "starter": {"price": 29, "subscribers": 150},
                "pro": {"price": 79, "subscribers": 80},
                "enterprise": {"price": 199, "subscribers": 25}
            },
            "subscriptions": {
                "total": 255,
                "active": 235,
                "cancelled": 20
            }
        }
        
        return mock_finance
    
    def collect_growth_metrics(self, project_id: str) -> Dict[str, Any]:
        """
        Collecte les métriques de croissance et marketing
        """
        # TODO: Intégrer avec vraies APIs (Google Ads, Facebook Ads, etc.)
        mock_growth = {
            "advertising": {
                "google_ads": {
                    "budget": 3000,
                    "clicks": 15000,
                    "conversions": 45,
                    "ctr": 0.025,
                    "cpc": 0.20,
                    "roas": 2.8
                },
                "linkedin_ads": {
                    "budget": 1500,
                    "clicks": 8000,
                    "conversions": 35,
                    "ctr": 0.035,
                    "cpc": 0.18,
                    "roas": 3.2
                },
                "facebook_ads": {
                    "budget": 1000,
                    "clicks": 12000,
                    "conversions": 25,
                    "ctr": 0.020,
                    "cpc": 0.15,
                    "roas": 2.5
                }
            },
            "organic": {
                "seo_traffic": 25000,
                "conversion_rate": 0.08,
                "cost_per_lead": 0
            },
            "referrals": {
                "referral_rate": 0.12,
                "referral_value": 1800
            }
        }
        
        return mock_growth
    
    def analyze_financial_performance(self, finance: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyse les performances financières et identifie les opportunités d'optimisation
        """
        analysis = {
            "revenue_health": "good",
            "pricing_optimization": [],
            "churn_analysis": {},
            "ltv_cac_ratio": 0,
            "recommendations": []
        }
        
        # Analyse LTV/CAC
        ltv = finance.get("revenue", {}).get("ltv", 0)
        cac = finance.get("revenue", {}).get("cac", 0)
        if ltv > 0 and cac > 0:
            ltv_cac_ratio = ltv / cac
            analysis["ltv_cac_ratio"] = round(ltv_cac_ratio, 2)
            
            if ltv_cac_ratio < 3:
                analysis["recommendations"].append("LTV/CAC trop bas - optimiser l'acquisition ou augmenter la rétention")
            elif ltv_cac_ratio > 5:
                analysis["recommendations"].append("LTV/CAC excellent - possible d'augmenter le budget marketing")
        
        # Analyse du churn
        churn_rate = finance.get("revenue", {}).get("churn_rate", 0)
        if churn_rate > self.optimization_thresholds["churn_threshold"]:
            analysis["churn_analysis"] = {
                "status": "critical",
                "message": f"Churn élevé ({churn_rate*100:.1f}%) - action immédiate requise"
            }
            analysis["recommendations"].append("Réduire le churn via programme de rétention")
        else:
            analysis["churn_analysis"] = {
                "status": "healthy",
                "message": f"Churn acceptable ({churn_rate*100:.1f}%)"
            }
        
        # Analyse du pricing
        pricing = finance.get("pricing", {})
        starter_price = pricing.get("starter", {}).get("price", 0)
        pro_price = pricing.get("pro", {}).get("price", 0)
        
        if pro_price / starter_price < 2.5:
            analysis["pricing_optimization"].append("Écart starter/pro insuffisant - augmenter pro")
        
        if starter_price < 25:
            analysis["pricing_optimization"].append("Prix starter trop bas - risque de dévalorisation")
        
        return analysis
    
    def analyze_advertising_performance(self, growth: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyse les performances publicitaires et propose des optimisations
        """
        analysis = {
            "top_performing_channel": None,
            "budget_reallocation": [],
            "roi_improvements": [],
            "ctr_optimizations": []
        }
        
        channels = growth.get("advertising", {})
        channel_performance = {}
        
        for channel_name, metrics in channels.items():
            roas = metrics.get("roas", 0)
            ctr = metrics.get("ctr", 0)
            cpc = metrics.get("cpc", 0)
            
            channel_performance[channel_name] = {
                "roas": roas,
                "ctr": ctr,
                "cpc": cpc,
                "efficiency_score": roas * ctr / cpc if cpc > 0 else 0
            }
        
        # Identifier le meilleur canal
        if channel_performance:
            top_channel = max(channel_performance.items(), key=lambda x: x[1]["efficiency_score"])
            analysis["top_performing_channel"] = top_channel[0]
        
        # Recommandations de réallocation
        for channel_name, performance in channel_performance.items():
            roas = performance["roas"]
            
            if roas < 2.5:
                analysis["budget_reallocation"].append(f"Réduire budget {channel_name} (ROAS: {roas})")
            elif roas > 3.5:
                analysis["budget_reallocation"].append(f"Augmenter budget {channel_name} (ROAS: {roas})")
        
        return analysis
    
    def generate_pricing_optimizations(self, finance: Dict[str, Any], analysis: Dict[str, Any]) -> List[str]:
        """
        Génère des recommandations d'optimisation du pricing
        """
        optimizations = []
        pricing = finance.get("pricing", {})
        
        # Analyse des plans existants
        starter = pricing.get("starter", {})
        pro = pricing.get("pro", {})
        enterprise = pricing.get("enterprise", {})
        
        # Optimisations basées sur l'analyse
        if analysis.get("pricing_optimization"):
            for opt in analysis["pricing_optimization"]:
                if "augmenter pro" in opt.lower():
                    new_pro_price = int(pro.get("price", 79) * 1.15)  # +15%
                    optimizations.append(f"Pro passe à {new_pro_price}€/mois (+15%)")
                
                if "starter trop bas" in opt.lower():
                    new_starter_price = int(starter.get("price", 29) * 1.20)  # +20%
                    optimizations.append(f"Starter passe à {new_starter_price}€/mois (+20%)")
        
        # Optimisations basées sur la performance
        if analysis.get("ltv_cac_ratio", 0) > 4:
            optimizations.append("LTV/CAC excellent - possible d'augmenter tous les plans de 10-15%")
        
        if not optimizations:
            optimizations.append("Pricing actuel optimal - maintenir")
        
        return optimizations
    
    def generate_budget_recommendations(self, growth: Dict[str, Any], analysis: Dict[str, Any]) -> List[str]:
        """
        Génère des recommandations de réallocation budgétaire
        """
        recommendations = []
        channels = growth.get("advertising", {})
        
        # Calculer les budgets optimaux
        total_budget = sum(ch.get("budget", 0) for ch in channels.values())
        
        if analysis.get("budget_reallocation"):
            for rec in analysis["budget_reallocation"]:
                if "augmenter" in rec.lower():
                    channel_name = rec.split()[1]
                    current_budget = channels.get(channel_name, {}).get("budget", 0)
                    new_budget = int(current_budget * 1.20)  # +20%
                    recommendations.append(f"+20% {channel_name.title()}, budget: {current_budget}€ → {new_budget}€")
                
                elif "réduire" in rec.lower():
                    channel_name = rec.split()[1]
                    current_budget = channels.get(channel_name, {}).get("budget", 0)
                    new_budget = int(current_budget * 0.90)  # -10%
                    recommendations.append(f"-10% {channel_name.title()}, budget: {current_budget}€ → {new_budget}€")
        
        # Recommandations basées sur le ROI
        if analysis.get("top_performing_channel"):
            top_channel = analysis["top_performing_channel"]
            top_roas = channels.get(top_channel, {}).get("roas", 0)
            if top_roas > 3.5:
                recommendations.append(f"Priorité {top_channel.title()} - ROI exceptionnel ({top_roas})")
        
        if not recommendations:
            recommendations.append("Répartition budgétaire actuelle optimale")
        
        return recommendations
    
    def calculate_roi_projection(self, finance: Dict[str, Any], optimizations: List[str]) -> str:
        """
        Calcule la projection de ROI basée sur les optimisations proposées
        """
        base_mrr = finance.get("revenue", {}).get("mrr", 0)
        base_ltv = finance.get("revenue", {}).get("ltv", 0)
        
        # Estimation des améliorations
        mrr_improvement = 0
        ltv_improvement = 0
        
        for opt in optimizations:
            if "augmenter" in opt.lower() and "€/mois" in opt:
                mrr_improvement += 0.10  # +10% par optimisation pricing
            elif "budget" in opt.lower() and "+20%" in opt:
                mrr_improvement += 0.05  # +5% par augmentation budget efficace
        
        # Projection
        projected_mrr = base_mrr * (1 + mrr_improvement)
        projected_ltv = base_ltv * (1 + ltv_improvement)
        
        roi_improvement = ((projected_mrr - base_mrr) / base_mrr) * 100 if base_mrr > 0 else 0
        
        if roi_improvement > 0:
            return f"ROI +{roi_improvement:.1f}% attendu"
        else:
            return "ROI stable attendu"
    
    def run(self, project_id: str, finance: Dict[str, Any] = None, growth: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Méthode principale qui exécute l'optimisation business
        """
        try:
            self.log_event("BusinessOptimizerAgent", f"Démarrage optimisation pour projet {project_id}")
            
            # 1. Collecte des métriques si non fournies
            if finance is None:
                finance = self.collect_financial_metrics(project_id)
                self.logger.info("Métriques financières collectées")
            
            if growth is None:
                growth = self.collect_growth_metrics(project_id)
                self.logger.info("Métriques de croissance collectées")
            
            # 2. Analyse des performances
            financial_analysis = self.analyze_financial_performance(finance)
            advertising_analysis = self.analyze_advertising_performance(growth)
            
            self.logger.info("Analyses financières et publicitaires terminées")
            
            # 3. Génération des optimisations
            pricing_optimizations = self.generate_pricing_optimizations(finance, financial_analysis)
            budget_recommendations = self.generate_budget_recommendations(growth, advertising_analysis)
            
            # 4. Calcul des projections
            roi_projection = self.calculate_roi_projection(finance, pricing_optimizations)
            
            # 5. Résultat final
            result = {
                "project_id": project_id,
                "timestamp": datetime.now().isoformat(),
                "status": "optimization_completed",
                "financial_analysis": financial_analysis,
                "advertising_analysis": advertising_analysis,
                "pricing_changes": pricing_optimizations,
                "ads_budget_shift": budget_recommendations,
                "roi_projection": roi_projection,
                "summary": {
                    "total_optimizations": len(pricing_optimizations) + len(budget_recommendations),
                    "ltv_cac_ratio": financial_analysis.get("ltv_cac_ratio", 0),
                    "churn_status": financial_analysis.get("churn_analysis", {}).get("status", "unknown"),
                    "top_channel": advertising_analysis.get("top_performing_channel", "none")
                }
            }
            
            self.log_event("BusinessOptimizerAgent", "Optimisation business proposée")
            self.logger.info(f"Optimisation terminée avec succès pour projet {project_id}")
            
            return result
            
        except Exception as e:
            error_msg = f"Erreur dans BusinessOptimizerAgent: {str(e)}"
            self.logger.error(error_msg)
            self.log_event("BusinessOptimizerAgent", f"ERREUR: {error_msg}")
            
            return {
                "error": error_msg,
                "timestamp": datetime.now().isoformat(),
                "status": "failed"
            }

# Test du agent
if __name__ == "__main__":
    # Données simulées
    mock_finance = {
        "revenue": {
            "mrr": 12500,
            "ltv": 180,
            "cac": 45,
            "churn_rate": 0.08
        },
        "pricing": {
            "starter": {"price": 29},
            "pro": {"price": 79}
        }
    }
    
    mock_growth = {
        "advertising": {
            "google_ads": {"budget": 3000, "roas": 2.8},
            "linkedin_ads": {"budget": 1500, "roas": 3.2}
        }
    }
    
    agent = BusinessOptimizerAgent()
    result = agent.run("test-project-123", mock_finance, mock_growth)
    print(json.dumps(result, indent=2, ensure_ascii=False))