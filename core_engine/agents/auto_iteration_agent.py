"""
Auto Iteration Agent - Agent d'itération automatique des produits
"""

import json
import random
from typing import Dict, List, Optional
from ..utils.logger import log_event

class AutoIterationAgent:
    """Agent d'itération automatique des produits basé sur les données"""
    
    def __init__(self):
        self.logger = log_event
        self.iteration_strategies = [
            "A/B Testing", "Feature Flags", "Rolling Deployments", "Canary Releases"
        ]
        
    def run(self, product_data: Dict) -> Dict:
        """
        Analyse le produit et génère un plan d'itération
        
        Args:
            product_data: Données du produit (métriques, feedback, etc.)
            
        Returns:
            Dict contenant le plan d'itération
        """
        try:
            self.logger("AutoIterationAgent", "Démarrage de l'analyse d'itération")
            
            # Analyse des métriques
            metrics_analysis = self._analyze_metrics(product_data)
            
            # Identification des opportunités d'amélioration
            improvement_opportunities = self._identify_opportunities(metrics_analysis)
            
            # Plan d'itération
            iteration_plan = self._create_iteration_plan(improvement_opportunities)
            
            # Stratégie de déploiement
            deployment_strategy = self._define_deployment_strategy(iteration_plan)
            
            result = {
                "metrics_analysis": metrics_analysis,
                "improvement_opportunities": improvement_opportunities,
                "iteration_plan": iteration_plan,
                "deployment_strategy": deployment_strategy,
                "success_probability": self._calculate_success_probability(metrics_analysis),
                "estimated_roi": "Élevé - Amélioration continue du produit"
            }
            
            self.logger("AutoIterationAgent", "Plan d'itération généré avec succès")
            return result
            
        except Exception as e:
            self.logger("AutoIterationAgent", f"Erreur lors de l'analyse: {str(e)}")
            raise
    
    def _analyze_metrics(self, product_data: Dict) -> Dict:
        """Analyse les métriques du produit"""
        metrics = product_data.get("metrics", {})
        
        analysis = {
            "performance": {
                "response_time": metrics.get("response_time", "N/A"),
                "uptime": metrics.get("uptime", "N/A"),
                "error_rate": metrics.get("error_rate", "N/A")
            },
            "user_engagement": {
                "daily_active_users": metrics.get("dau", 0),
                "session_duration": metrics.get("session_duration", "N/A"),
                "retention_rate": metrics.get("retention_rate", 0)
            },
            "business_metrics": {
                "conversion_rate": metrics.get("conversion_rate", 0),
                "revenue_per_user": metrics.get("arpu", 0),
                "churn_rate": metrics.get("churn_rate", 0)
            }
        }
        
        # Évaluation de la santé du produit
        health_score = self._calculate_health_score(analysis)
        analysis["health_score"] = health_score
        analysis["overall_status"] = "Bon" if health_score > 7 else "À améliorer"
        
        return analysis
    
    def _calculate_health_score(self, analysis: Dict) -> float:
        """Calcule un score de santé du produit (0-10)"""
        score = 0
        total_metrics = 0
        
        # Métriques de performance
        if analysis["performance"]["uptime"] != "N/A":
            uptime = float(analysis["performance"]["uptime"].replace("%", ""))
            score += min(uptime / 10, 2)  # Max 2 points
            total_metrics += 1
        
        if analysis["performance"]["error_rate"] != "N/A":
            error_rate = float(analysis["performance"]["error_rate"].replace("%", ""))
            score += max(0, 2 - (error_rate / 5))  # Max 2 points
            total_metrics += 1
        
        # Métriques d'engagement
        if analysis["user_engagement"]["retention_rate"] > 0:
            retention = analysis["user_engagement"]["retention_rate"]
            score += min(retention / 10, 2)  # Max 2 points
            total_metrics += 1
        
        # Métriques business
        if analysis["business_metrics"]["conversion_rate"] > 0:
            conversion = analysis["business_metrics"]["conversion_rate"]
            score += min(conversion / 2, 2)  # Max 2 points
            total_metrics += 1
        
        if analysis["business_metrics"]["churn_rate"] > 0:
            churn = analysis["business_metrics"]["churn_rate"]
            score += max(0, 2 - (churn / 5))  # Max 2 points
            total_metrics += 1
        
        # Score final
        final_score = (score / total_metrics) * 10 if total_metrics > 0 else 5
        return round(final_score, 1)
    
    def _identify_opportunities(self, metrics_analysis: Dict) -> List[Dict]:
        """Identifie les opportunités d'amélioration"""
        opportunities = []
        
        # Opportunités basées sur la performance
        if metrics_analysis["performance"]["uptime"] != "N/A":
            uptime = float(metrics_analysis["performance"]["uptime"].replace("%", ""))
            if uptime < 99.5:
                opportunities.append({
                    "category": "Performance",
                    "priority": "Haute",
                    "description": "Améliorer la disponibilité du service",
                    "current_value": f"{uptime}%",
                    "target_value": "99.9%",
                    "impact": "Réduction des temps d'arrêt"
                })
        
        if metrics_analysis["performance"]["error_rate"] != "N/A":
            error_rate = float(metrics_analysis["performance"]["error_rate"].replace("%", ""))
            if error_rate > 1:
                opportunities.append({
                    "category": "Performance",
                    "priority": "Haute",
                    "description": "Réduire le taux d'erreur",
                    "current_value": f"{error_rate}%",
                    "target_value": "< 0.5%",
                    "impact": "Amélioration de la fiabilité"
                })
        
        # Opportunités basées sur l'engagement
        retention = metrics_analysis["user_engagement"]["retention_rate"]
        if retention < 70:
            opportunities.append({
                "category": "Engagement",
                "priority": "Moyenne",
                "description": "Améliorer la rétention utilisateur",
                "current_value": f"{retention}%",
                "target_value": "> 80%",
                "impact": "Augmentation de l'engagement"
            })
        
        # Opportunités basées sur les métriques business
        conversion = metrics_analysis["business_metrics"]["conversion_rate"]
        if conversion < 5:
            opportunities.append({
                "category": "Business",
                "priority": "Moyenne",
                "description": "Optimiser le taux de conversion",
                "current_value": f"{conversion}%",
                "target_value": "> 8%",
                "impact": "Augmentation des revenus"
            })
        
        return opportunities
    
    def _create_iteration_plan(self, opportunities: List[Dict]) -> Dict:
        """Crée un plan d'itération structuré"""
        if not opportunities:
            return {"message": "Aucune opportunité d'amélioration identifiée"}
        
        # Grouper par priorité
        high_priority = [o for o in opportunities if o["priority"] == "Haute"]
        medium_priority = [o for o in opportunities if o["priority"] == "Moyenne"]
        low_priority = [o for o in opportunities if o["priority"] == "Basse"]
        
        iteration_plan = {
            "sprint_1": {
                "duration": "2 semaines",
                "focus": "Performance et fiabilité",
                "tasks": high_priority[:2],  # Top 2 priorités hautes
                "success_criteria": [
                    "Réduction des erreurs de 50%",
                    "Amélioration de la disponibilité"
                ]
            },
            "sprint_2": {
                "duration": "2 semaines",
                "focus": "Engagement utilisateur",
                "tasks": medium_priority[:2],  # Top 2 priorités moyennes
                "success_criteria": [
                    "Amélioration de la rétention",
                    "Optimisation des conversions"
                ]
            },
            "sprint_3": {
                "duration": "2 semaines",
                "focus": "Optimisations et monitoring",
                "tasks": low_priority + opportunities[4:],  # Reste des opportunités
                "success_criteria": [
                    "Mise en place du monitoring avancé",
                    "Documentation des améliorations"
                ]
            }
        }
        
        return iteration_plan
    
    def _define_deployment_strategy(self, iteration_plan: Dict) -> Dict:
        """Définit la stratégie de déploiement"""
        if "message" in iteration_plan:
            return {"strategy": "Aucun déploiement nécessaire"}
        
        deployment_strategy = {
            "approach": "Rolling Deployment avec Feature Flags",
            "phases": [
                {
                    "phase": "Phase 1 - Tests internes",
                    "duration": "3-5 jours",
                    "users": "Équipe de développement",
                    "rollback": "Immédiat si problème critique"
                },
                {
                    "phase": "Phase 2 - Beta testeurs",
                    "duration": "1 semaine",
                    "users": "5-10% des utilisateurs actifs",
                    "rollback": "Dans les 2 heures si problème"
                },
                {
                    "phase": "Phase 3 - Déploiement progressif",
                    "duration": "1-2 semaines",
                    "users": "100% des utilisateurs",
                    "rollback": "Dans les 24h si nécessaire"
                }
            ],
            "monitoring": [
                "Métriques de performance en temps réel",
                "Alertes automatiques sur les erreurs",
                "Dashboard de suivi des améliorations"
            ],
            "rollback_plan": {
                "triggers": ["Erreur critique", "Performance dégradée > 20%", "Feedback négatif > 30%"],
                "procedure": "Retour à la version précédente via feature flags",
                "timeline": "Maximum 2 heures"
            }
        }
        
        return deployment_strategy
    
    def _calculate_success_probability(self, metrics_analysis: Dict) -> float:
        """Calcule la probabilité de succès des itérations"""
        health_score = metrics_analysis.get("health_score", 5)
        
        # Plus le produit est en bonne santé, plus les itérations ont de chances de réussir
        if health_score >= 8:
            base_probability = 85
        elif health_score >= 6:
            base_probability = 70
        else:
            base_probability = 50
        
        # Ajustements basés sur les métriques
        adjustments = 0
        
        if metrics_analysis["performance"]["uptime"] != "N/A":
            uptime = float(metrics_analysis["performance"]["uptime"].replace("%", ""))
            if uptime < 95:
                adjustments += 10  # Plus d'opportunités d'amélioration
        
        if metrics_analysis["user_engagement"]["retention_rate"] < 60:
            adjustments += 15  # Beaucoup d'espace d'amélioration
        
        final_probability = min(95, base_probability + adjustments)
        return round(final_probability, 1)


# Fonction utilitaire
def create_iteration_plan(product_data: Dict) -> Dict:
    """
    Fonction utilitaire pour créer un plan d'itération
    
    Args:
        product_data: Données du produit
        
    Returns:
        Dict contenant le plan d'itération complet
    """
    agent = AutoIterationAgent()
    return agent.run(product_data)


if __name__ == "__main__":
    # Test de l'agent
    test_product_data = {
        "metrics": {
            "response_time": "200ms",
            "uptime": "98.5%",
            "error_rate": "2.1%",
            "dau": 1500,
            "session_duration": "8m 30s",
            "retention_rate": 65,
            "conversion_rate": 4.2,
            "arpu": 15.50,
            "churn_rate": 8.5
        }
    }
    
    try:
        result = create_iteration_plan(test_product_data)
        print("✅ Test AutoIterationAgent réussi!")
        print(f"Résultat: {json.dumps(result, indent=2)}")
    except Exception as e:
        print(f"❌ Test échoué: {e}")