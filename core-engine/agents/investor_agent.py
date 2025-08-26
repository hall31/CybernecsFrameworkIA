import json
import logging
from typing import Dict, Any, Optional
from datetime import datetime, timedelta
import math

class InvestorAgent:
    """
    Agent d'investissement IA pour évaluer et décider des investissements dans les startups
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.vc_multiples = {
            "saas": 8.0,      # Multiple ARR pour SaaS
            "marketplace": 6.0, # Multiple ARR pour marketplace
            "fintech": 10.0,   # Multiple ARR pour fintech
            "ai": 12.0,        # Multiple ARR pour IA
            "default": 7.0     # Multiple par défaut
        }
        
        self.investment_thresholds = {
            "mrr_min": 5000,    # MRR minimum pour investir
            "cac_max": 100,     # CAC maximum acceptable
            "ltv_min": 300,     # LTV minimum
            "churn_max": 0.05   # Churn maximum (5%)
        }
    
    def run(self, project_id: str, finance: Dict[str, Any], 
            growth: Dict[str, Any], optimizer: Dict[str, Any]) -> Dict[str, Any]:
        """
        Méthode principale d'évaluation et de décision d'investissement
        
        Args:
            project_id: Identifiant du projet
            finance: Données financières (CA réel, projections)
            growth: Données de croissance (CAC, LTV, CTR)
            optimizer: Données d'optimisation business
            
        Returns:
            Dict avec valuation, KPIs, décision et prochain financement
        """
        try:
            self.logger.info(f"InvestorAgent: Début d'évaluation pour le projet {project_id}")
            
            # 1. Analyse des données financières
            financial_analysis = self._analyze_financials(finance)
            
            # 2. Analyse de la croissance
            growth_analysis = self._analyze_growth(growth, optimizer)
            
            # 3. Calcul de la valorisation
            valuation = self._calculate_valuation(financial_analysis, growth_analysis)
            
            # 4. Décision d'investissement
            investment_decision = self._make_investment_decision(
                financial_analysis, growth_analysis, valuation
            )
            
            # 5. Plan de financement
            funding_plan = self._generate_funding_plan(
                investment_decision, financial_analysis, growth_analysis
            )
            
            result = {
                "valuation": valuation,
                "kpis": self._extract_kpis(financial_analysis, growth_analysis),
                "decision": investment_decision["decision"],
                "next_funding": funding_plan,
                "confidence_score": investment_decision["confidence"],
                "analysis_date": datetime.now().isoformat(),
                "project_id": project_id
            }
            
            self.logger.info(f"InvestorAgent: Évaluation et décision effectuées pour {project_id}")
            self._log_event("InvestorAgent", "Évaluation et décision effectuées")
            
            return result
            
        except Exception as e:
            self.logger.error(f"InvestorAgent: Erreur lors de l'évaluation: {str(e)}")
            return self._get_error_response(project_id, str(e))
    
    def _analyze_financials(self, finance: Dict[str, Any]) -> Dict[str, Any]:
        """Analyse des données financières"""
        try:
            # Extraction des données financières
            current_revenue = finance.get("current_revenue", 0)
            projected_revenue = finance.get("projected_revenue", 0)
            stripe_revenue = finance.get("stripe_revenue", 0)
            
            # Calcul du MRR (Monthly Recurring Revenue)
            mrr = max(stripe_revenue, current_revenue, projected_revenue / 12)
            
            # Calcul de l'ARR (Annual Recurring Revenue)
            arr = mrr * 12
            
            # Analyse de la croissance des revenus
            revenue_growth = 0
            if current_revenue > 0:
                revenue_growth = ((projected_revenue - current_revenue) / current_revenue) * 100
            
            return {
                "mrr": mrr,
                "arr": arr,
                "current_revenue": current_revenue,
                "projected_revenue": projected_revenue,
                "stripe_revenue": stripe_revenue,
                "revenue_growth_percent": revenue_growth,
                "has_stripe_data": stripe_revenue > 0
            }
            
        except Exception as e:
            self.logger.error(f"Erreur analyse financière: {str(e)}")
            return {"mrr": 0, "arr": 0, "error": str(e)}
    
    def _analyze_growth(self, growth: Dict[str, Any], optimizer: Dict[str, Any]) -> Dict[str, Any]:
        """Analyse des métriques de croissance"""
        try:
            # Métriques de croissance
            cac = growth.get("cac", 0)  # Customer Acquisition Cost
            ltv = growth.get("ltv", 0)  # Lifetime Value
            ctr = growth.get("ctr", 0)  # Click Through Rate
            conversion_rate = growth.get("conversion_rate", 0)
            
            # Métriques d'optimisation
            churn_rate = optimizer.get("churn_rate", 0.05)
            retention_rate = 1 - churn_rate
            
            # Calcul du ratio LTV/CAC
            ltv_cac_ratio = ltv / cac if cac > 0 else 0
            
            # Score de santé de la croissance
            growth_health_score = self._calculate_growth_health_score(
                cac, ltv, ctr, conversion_rate, churn_rate
            )
            
            return {
                "cac": cac,
                "ltv": ltv,
                "ctr": ctr,
                "conversion_rate": conversion_rate,
                "churn_rate": churn_rate,
                "retention_rate": retention_rate,
                "ltv_cac_ratio": ltv_cac_ratio,
                "growth_health_score": growth_health_score
            }
            
        except Exception as e:
            self.logger.error(f"Erreur analyse croissance: {str(e)}")
            return {"cac": 0, "ltv": 0, "error": str(e)}
    
    def _calculate_valuation(self, financial_analysis: Dict[str, Any], 
                           growth_analysis: Dict[str, Any]) -> str:
        """Calcul de la valorisation estimée"""
        try:
            arr = financial_analysis.get("arr", 0)
            growth_health = growth_analysis.get("growth_health_score", 0.5)
            
            # Détermination du multiple selon le type de business
            business_type = self._determine_business_type(financial_analysis, growth_analysis)
            base_multiple = self.vc_multiples.get(business_type, self.vc_multiples["default"])
            
            # Ajustement du multiple selon la santé de la croissance
            adjusted_multiple = base_multiple * (0.8 + growth_health * 0.4)
            
            # Calcul de la valorisation
            valuation = arr * adjusted_multiple
            
            # Formatage en millions d'euros
            if valuation >= 1000000:
                return f"{valuation / 1000000:.1f}M €"
            elif valuation >= 1000:
                return f"{valuation / 1000:.0f}k €"
            else:
                return f"{valuation:.0f} €"
                
        except Exception as e:
            self.logger.error(f"Erreur calcul valorisation: {str(e)}")
            return "N/A"
    
    def _determine_business_type(self, financial_analysis: Dict[str, Any], 
                                growth_analysis: Dict[str, Any]) -> str:
        """Détermine le type de business pour le calcul du multiple"""
        # Logique simplifiée pour déterminer le type
        if growth_analysis.get("ltv_cac_ratio", 0) > 5:
            return "ai"  # Business avec forte rétention
        elif financial_analysis.get("has_stripe_data", False):
            return "saas"  # Business SaaS avec paiements
        else:
            return "marketplace"  # Par défaut
    
    def _calculate_growth_health_score(self, cac: float, ltv: float, ctr: float, 
                                     conversion_rate: float, churn_rate: float) -> float:
        """Calcule un score de santé de la croissance (0-1)"""
        try:
            score = 0.0
            
            # Score LTV/CAC (40% du score total)
            if cac > 0:
                ltv_cac_score = min(ltv / cac / 3, 1.0)  # Normalisé sur 3
                score += ltv_cac_score * 0.4
            
            # Score CTR (20% du score total)
            ctr_score = min(ctr / 0.05, 1.0)  # Normalisé sur 5%
            score += ctr_score * 0.2
            
            # Score conversion (20% du score total)
            conversion_score = min(conversion_rate / 0.03, 1.0)  # Normalisé sur 3%
            score += conversion_score * 0.2
            
            # Score churn (20% du score total)
            churn_score = max(0, 1 - (churn_rate / 0.1))  # Normalisé sur 10%
            score += churn_score * 0.2
            
            return min(max(score, 0.0), 1.0)
            
        except Exception as e:
            self.logger.error(f"Erreur calcul score croissance: {str(e)}")
            return 0.5
    
    def _make_investment_decision(self, financial_analysis: Dict[str, Any], 
                                 growth_analysis: Dict[str, Any], 
                                 valuation: str) -> Dict[str, Any]:
        """Prend la décision d'investissement"""
        try:
            mrr = financial_analysis.get("mrr", 0)
            cac = growth_analysis.get("cac", 0)
            ltv = growth_analysis.get("ltv", 0)
            churn_rate = growth_analysis.get("churn_rate", 0.05)
            growth_health = growth_analysis.get("growth_health_score", 0.5)
            
            # Critères d'investissement
            mrr_ok = mrr >= self.investment_thresholds["mrr_min"]
            cac_ok = cac <= self.investment_thresholds["cac_max"]
            ltv_ok = ltv >= self.investment_thresholds["ltv_min"]
            churn_ok = churn_rate <= self.investment_thresholds["churn_max"]
            growth_ok = growth_health >= 0.6
            
            # Calcul du score global
            criteria_met = sum([mrr_ok, cac_ok, ltv_ok, churn_ok, growth_ok])
            total_criteria = 5
            
            # Décision basée sur le score
            if criteria_met >= 4:
                decision = "Investir"
                confidence = min(0.9, 0.5 + (criteria_met / total_criteria) * 0.4)
            elif criteria_met >= 3:
                decision = "Investir avec conditions"
                confidence = 0.6
            else:
                decision = "Ne pas investir"
                confidence = 0.3
            
            return {
                "decision": decision,
                "confidence": confidence,
                "criteria_met": criteria_met,
                "total_criteria": total_criteria,
                "details": {
                    "mrr_ok": mrr_ok,
                    "cac_ok": cac_ok,
                    "ltv_ok": ltv_ok,
                    "churn_ok": churn_ok,
                    "growth_ok": growth_ok
                }
            }
            
        except Exception as e:
            self.logger.error(f"Erreur décision investissement: {str(e)}")
            return {"decision": "Erreur", "confidence": 0.0}
    
    def _generate_funding_plan(self, investment_decision: Dict[str, Any], 
                              financial_analysis: Dict[str, Any], 
                              growth_analysis: Dict[str, Any]) -> str:
        """Génère le plan de financement"""
        try:
            if investment_decision["decision"] == "Ne pas investir":
                return "Aucun financement recommandé"
            
            mrr = financial_analysis.get("mrr", 0)
            growth_health = growth_analysis.get("growth_health_score", 0.5)
            
            # Calcul du montant d'investissement basé sur le MRR et la santé
            base_investment = mrr * 6  # 6 mois de MRR
            growth_multiplier = 1 + growth_health
            
            total_investment = base_investment * growth_multiplier
            
            # Répartition des investissements
            if total_investment > 100000:
                cloud_credits = "50k € en crédits cloud"
                marketing_budget = "30k € en budget marketing"
                ai_resources = "20k € en ressources IA"
            elif total_investment > 50000:
                cloud_credits = "25k € en crédits cloud"
                marketing_budget = "15k € en budget marketing"
                ai_resources = "10k € en ressources IA"
            else:
                cloud_credits = "10k € en crédits cloud"
                marketing_budget = "5k € en budget marketing"
                ai_resources = "5k € en ressources IA"
            
            return f"{int(total_investment/1000)}k €: {cloud_credits}, {marketing_budget}, {ai_resources}"
            
        except Exception as e:
            self.logger.error(f"Erreur génération plan financement: {str(e)}")
            return "Plan de financement non disponible"
    
    def _extract_kpis(self, financial_analysis: Dict[str, Any], 
                      growth_analysis: Dict[str, Any]) -> Dict[str, str]:
        """Extrait les KPIs principaux pour l'affichage"""
        try:
            return {
                "MRR": f"{financial_analysis.get('mrr', 0):.0f} €",
                "CAC": f"{growth_analysis.get('cac', 0):.0f} €",
                "LTV": f"{growth_analysis.get('ltv', 0):.0f} €",
                "Churn": f"{growth_analysis.get('churn_rate', 0.05) * 100:.1f}%"
            }
        except Exception as e:
            self.logger.error(f"Erreur extraction KPIs: {str(e)}")
            return {"MRR": "N/A", "CAC": "N/A", "LTV": "N/A", "Churn": "N/A"}
    
    def _log_event(self, agent_name: str, message: str):
        """Log un événement"""
        try:
            log_entry = {
                "timestamp": datetime.now().isoformat(),
                "agent": agent_name,
                "message": message,
                "level": "INFO"
            }
            self.logger.info(json.dumps(log_entry))
        except Exception as e:
            self.logger.error(f"Erreur logging: {str(e)}")
    
    def _get_error_response(self, project_id: str, error_message: str) -> Dict[str, Any]:
        """Retourne une réponse d'erreur standardisée"""
        return {
            "valuation": "Erreur",
            "kpis": {"MRR": "N/A", "CAC": "N/A", "LTV": "N/A", "Churn": "N/A"},
            "decision": "Erreur d'évaluation",
            "next_funding": "Non disponible",
            "error": error_message,
            "project_id": project_id,
            "analysis_date": datetime.now().isoformat()
        }