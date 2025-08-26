"""
Business Optimizer Agent - Agent d'optimisation business
"""

import json
import random
from typing import Dict, List, Optional
from ..utils.logger import log_event

class BusinessOptimizerAgent:
    """Agent d'optimisation des processus business et de la rentabilité"""
    
    def __init__(self):
        self.logger = log_event
        self.optimization_areas = [
            "Processus", "Coûts", "Revenus", "Efficacité", "Qualité"
        ]
        
    def run(self, business_data: Dict) -> Dict:
        """
        Analyse les données business et génère des recommandations d'optimisation
        
        Args:
            business_data: Données business (métriques, processus, etc.)
            
        Returns:
            Dict contenant les recommandations d'optimisation
        """
        try:
            self.logger("BusinessOptimizerAgent", "Démarrage de l'analyse business")
            
            # Analyse des processus
            process_analysis = self._analyze_processes(business_data)
            
            # Analyse des coûts
            cost_analysis = self._analyze_costs(business_data)
            
            # Analyse des revenus
            revenue_analysis = self._analyze_revenue(business_data)
            
            # Recommandations d'optimisation
            optimization_recommendations = self._generate_recommendations(
                process_analysis, cost_analysis, revenue_analysis
            )
            
            # Plan d'implémentation
            implementation_plan = self._create_implementation_plan(optimization_recommendations)
            
            result = {
                "process_analysis": process_analysis,
                "cost_analysis": cost_analysis,
                "revenue_analysis": revenue_analysis,
                "optimization_recommendations": optimization_recommendations,
                "implementation_plan": implementation_plan,
                "estimated_impact": self._calculate_estimated_impact(optimization_recommendations),
                "roi_estimate": "Élevé - Optimisation significative des processus"
            }
            
            self.logger("BusinessOptimizerAgent", "Analyse business terminée avec succès")
            return result
            
        except Exception as e:
            self.logger("BusinessOptimizerAgent", f"Erreur lors de l'analyse: {str(e)}")
            raise
    
    def _analyze_processes(self, business_data: Dict) -> Dict:
        """Analyse l'efficacité des processus business"""
        processes = business_data.get("processes", {})
        
        analysis = {
            "efficiency_score": 0,
            "bottlenecks": [],
            "automation_opportunities": [],
            "process_health": "Moyen"
        }
        
        # Calcul du score d'efficacité
        total_processes = len(processes)
        if total_processes == 0:
            return analysis
        
        efficiency_scores = []
        for process_name, process_data in processes.items():
            # Score basé sur le temps de traitement et la qualité
            time_score = min(100, max(0, 100 - (process_data.get("avg_time_minutes", 60) / 60 * 100)))
            quality_score = process_data.get("quality_score", 70)
            efficiency_score = (time_score + quality_score) / 2
            efficiency_scores.append(efficiency_score)
            
            # Identification des goulots d'étranglement
            if process_data.get("avg_time_minutes", 0) > 120:
                analysis["bottlenecks"].append({
                    "process": process_name,
                    "issue": "Temps de traitement élevé",
                    "current_time": f"{process_data.get('avg_time_minutes', 0)} minutes",
                    "target_time": "60 minutes"
                })
            
            # Opportunités d'automatisation
            if process_data.get("manual_steps", 0) > 5:
                analysis["automation_opportunities"].append({
                    "process": process_name,
                    "manual_steps": process_data.get("manual_steps", 0),
                    "automation_potential": "Élevé",
                    "estimated_savings": "30-50% du temps"
                })
        
        # Score d'efficacité global
        analysis["efficiency_score"] = round(sum(efficiency_scores) / len(efficiency_scores), 1)
        
        # Évaluation de la santé des processus
        if analysis["efficiency_score"] >= 80:
            analysis["process_health"] = "Excellent"
        elif analysis["efficiency_score"] >= 60:
            analysis["process_health"] = "Bon"
        else:
            analysis["process_health"] = "À améliorer"
        
        return analysis
    
    def _analyze_costs(self, business_data: Dict) -> Dict:
        """Analyse la structure des coûts"""
        costs = business_data.get("costs", {})
        
        analysis = {
            "total_monthly_costs": 0,
            "cost_breakdown": {},
            "cost_optimization_opportunities": [],
            "cost_efficiency": "Moyen"
        }
        
        # Calcul des coûts totaux
        total_costs = 0
        for category, amount in costs.items():
            total_costs += amount
            analysis["cost_breakdown"][category] = {
                "amount": amount,
                "percentage": 0  # Sera calculé après
            }
        
        analysis["total_monthly_costs"] = total_costs
        
        # Calcul des pourcentages et identification des opportunités
        if total_costs > 0:
            for category, data in analysis["cost_breakdown"].items():
                data["percentage"] = round((data["amount"] / total_costs) * 100, 1)
                
                # Opportunités d'optimisation des coûts
                if data["percentage"] > 30:
                    analysis["cost_optimization_opportunities"].append({
                        "category": category,
                        "current_percentage": data["percentage"],
                        "recommendation": f"Réduire les coûts {category}",
                        "potential_savings": f"{round(data['percentage'] * 0.2, 1)}% du total"
                    })
        
        # Évaluation de l'efficacité des coûts
        if total_costs < 10000:
            analysis["cost_efficiency"] = "Excellent"
        elif total_costs < 50000:
            analysis["cost_efficiency"] = "Bon"
        else:
            analysis["cost_efficiency"] = "À optimiser"
        
        return analysis
    
    def _analyze_revenue(self, business_data: Dict) -> Dict:
        """Analyse les sources de revenus et la croissance"""
        revenue = business_data.get("revenue", {})
        
        analysis = {
            "total_monthly_revenue": 0,
            "revenue_growth": 0,
            "revenue_sources": {},
            "revenue_optimization_opportunities": [],
            "revenue_health": "Moyen"
        }
        
        # Calcul des revenus totaux
        total_revenue = 0
        for source, amount in revenue.items():
            if isinstance(amount, dict):
                current_amount = amount.get("current", 0)
                previous_amount = amount.get("previous", 0)
                total_revenue += current_amount
                
                # Calcul de la croissance
                if previous_amount > 0:
                    growth = ((current_amount - previous_amount) / previous_amount) * 100
                else:
                    growth = 0
                
                analysis["revenue_sources"][source] = {
                    "current": current_amount,
                    "previous": previous_amount,
                    "growth": round(growth, 1)
                }
            else:
                total_revenue += amount
                analysis["revenue_sources"][source] = {
                    "current": amount,
                    "previous": amount,
                    "growth": 0
                }
        
        analysis["total_monthly_revenue"] = total_revenue
        
        # Calcul de la croissance globale
        total_previous = sum(data.get("previous", 0) for data in analysis["revenue_sources"].values())
        if total_previous > 0:
            analysis["revenue_growth"] = round(((total_revenue - total_previous) / total_previous) * 100, 1)
        
        # Opportunités d'optimisation des revenus
        for source, data in analysis["revenue_sources"].items():
            if data["growth"] < 0:
                analysis["revenue_optimization_opportunities"].append({
                    "source": source,
                    "issue": "Croissance négative",
                    "recommendation": f"Analyser et optimiser {source}",
                    "potential_improvement": "Inverser la tendance négative"
                })
            elif data["growth"] < 10:
                analysis["revenue_optimization_opportunities"].append({
                    "source": source,
                    "issue": "Croissance faible",
                    "recommendation": f"Accélérer la croissance de {source}",
                    "potential_improvement": "Augmentation de 20-30%"
                })
        
        # Évaluation de la santé des revenus
        if analysis["revenue_growth"] >= 20:
            analysis["revenue_health"] = "Excellent"
        elif analysis["revenue_growth"] >= 10:
            analysis["revenue_health"] = "Bon"
        elif analysis["revenue_growth"] >= 0:
            analysis["revenue_health"] = "Stable"
        else:
            analysis["revenue_health"] = "À améliorer"
        
        return analysis
    
    def _generate_recommendations(self, process_analysis: Dict, cost_analysis: Dict, revenue_analysis: Dict) -> List[Dict]:
        """Génère des recommandations d'optimisation basées sur les analyses"""
        recommendations = []
        
        # Recommandations basées sur les processus
        if process_analysis["efficiency_score"] < 70:
            recommendations.append({
                "category": "Processus",
                "priority": "Haute",
                "title": "Améliorer l'efficacité des processus",
                "description": f"Score d'efficacité actuel: {process_analysis['efficiency_score']}/100",
                "actions": [
                    "Identifier et résoudre les goulots d'étranglement",
                    "Automatiser les processus manuels",
                    "Standardiser les procédures"
                ],
                "estimated_impact": "Amélioration de 20-30% de l'efficacité",
                "timeline": "4-6 semaines"
            })
        
        # Recommandations basées sur les coûts
        if cost_analysis["total_monthly_costs"] > 50000:
            recommendations.append({
                "category": "Coûts",
                "priority": "Moyenne",
                "title": "Optimiser la structure des coûts",
                "description": f"Coûts mensuels totaux: {cost_analysis['total_monthly_costs']:,} €",
                "actions": [
                    "Analyser les catégories de coûts les plus élevées",
                    "Négocier avec les fournisseurs",
                    "Identifier les économies d'échelle"
                ],
                "estimated_impact": "Réduction de 15-25% des coûts",
                "timeline": "2-3 mois"
            })
        
        # Recommandations basées sur les revenus
        if revenue_analysis["revenue_growth"] < 10:
            recommendations.append({
                "category": "Revenus",
                "priority": "Haute",
                "title": "Accélérer la croissance des revenus",
                "description": f"Croissance actuelle: {revenue_analysis['revenue_growth']}%",
                "actions": [
                    "Analyser les sources de revenus en déclin",
                    "Développer de nouvelles sources de revenus",
                    "Optimiser les canaux de vente existants"
                ],
                "estimated_impact": "Augmentation de 20-40% de la croissance",
                "timeline": "3-6 mois"
            })
        
        # Recommandations générales
        recommendations.append({
            "category": "Monitoring",
            "priority": "Basse",
            "title": "Mettre en place un système de monitoring avancé",
            "description": "Surveillance continue des métriques business",
            "actions": [
                "Dashboard de métriques en temps réel",
                "Alertes automatiques sur les seuils critiques",
                "Rapports hebdomadaires automatisés"
            ],
            "estimated_impact": "Détection précoce des problèmes",
            "timeline": "2-4 semaines"
        })
        
        return recommendations
    
    def _create_implementation_plan(self, recommendations: List[Dict]) -> Dict:
        """Crée un plan d'implémentation structuré"""
        if not recommendations:
            return {"message": "Aucune recommandation d'optimisation"}
        
        # Trier par priorité
        priority_order = {"Haute": 1, "Moyenne": 2, "Basse": 3}
        sorted_recommendations = sorted(recommendations, key=lambda x: priority_order.get(x["priority"], 4))
        
        implementation_plan = {
            "phase_1": {
                "duration": "4-6 semaines",
                "focus": "Optimisations prioritaires",
                "recommendations": [r for r in sorted_recommendations if r["priority"] == "Haute"],
                "resources_needed": "Équipe dédiée + budget d'investissement",
                "success_criteria": [
                    "Amélioration de l'efficacité des processus",
                    "Réduction des coûts opérationnels",
                    "Accélération de la croissance des revenus"
                ]
            },
            "phase_2": {
                "duration": "2-3 mois",
                "focus": "Optimisations à moyen terme",
                "recommendations": [r for r in sorted_recommendations if r["priority"] == "Moyenne"],
                "resources_needed": "Équipe existante + formation",
                "success_criteria": [
                    "Stabilisation des améliorations",
                    "Mise en place des nouveaux processus",
                    "Formation des équipes"
                ]
            },
            "phase_3": {
                "duration": "1-2 mois",
                "focus": "Monitoring et maintenance",
                "recommendations": [r for r in sorted_recommendations if r["priority"] == "Basse"],
                "resources_needed": "Équipe IT + outils",
                "success_criteria": [
                    "Système de monitoring opérationnel",
                    "Processus de maintenance établi",
                    "Documentation complète"
                ]
            }
        }
        
        return implementation_plan
    
    def _calculate_estimated_impact(self, recommendations: List[Dict]) -> Dict:
        """Calcule l'impact estimé des optimisations"""
        if not recommendations:
            return {"message": "Aucun impact estimé"}
        
        total_impact = {
            "efficiency_improvement": "15-25%",
            "cost_reduction": "10-20%",
            "revenue_increase": "20-35%",
            "timeline": "6-12 mois",
            "roi_estimate": "200-400%"
        }
        
        return total_impact


# Fonction utilitaire
def optimize_business(business_data: Dict) -> Dict:
    """
    Fonction utilitaire pour optimiser les processus business
    
    Args:
        business_data: Données business
        
    Returns:
        Dict contenant les recommandations d'optimisation
    """
    agent = BusinessOptimizerAgent()
    return agent.run(business_data)


if __name__ == "__main__":
    # Test de l'agent
    test_business_data = {
        "processes": {
            "onboarding": {"avg_time_minutes": 45, "quality_score": 85, "manual_steps": 3},
            "billing": {"avg_time_minutes": 30, "quality_score": 90, "manual_steps": 2},
            "support": {"avg_time_minutes": 180, "quality_score": 70, "manual_steps": 8}
        },
        "costs": {
            "personnel": 35000,
            "infrastructure": 8000,
            "marketing": 12000,
            "operations": 5000
        },
        "revenue": {
            "subscriptions": {"current": 45000, "previous": 42000},
            "consulting": {"current": 15000, "previous": 18000},
            "training": {"current": 8000, "previous": 6000}
        }
    }
    
    try:
        result = optimize_business(test_business_data)
        print("✅ Test BusinessOptimizerAgent réussi!")
        print(f"Résultat: {json.dumps(result, indent=2)}")
    except Exception as e:
        print(f"❌ Test échoué: {e}")