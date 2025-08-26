"""
Product Feedback Agent - Agent d'analyse des retours utilisateurs
"""

import json
import random
from typing import Dict, List, Optional
from ..utils.logger import log_event

class ProductFeedbackAgent:
    """Agent d'analyse des retours utilisateurs et d'amélioration produit"""
    
    def __init__(self):
        self.logger = log_event
        self.feedback_categories = [
            "UX/UI", "Performance", "Fonctionnalités", "Support", "Prix"
        ]
        
    def run(self, feedback_data: List[Dict]) -> Dict:
        """
        Analyse les retours utilisateurs et génère des recommandations
        
        Args:
            feedback_data: Liste des retours utilisateurs
            
        Returns:
            Dict contenant l'analyse et les recommandations
        """
        try:
            self.logger("ProductFeedbackAgent", "Démarrage de l'analyse des retours utilisateurs")
            
            # Analyse des retours
            analysis = self._analyze_feedback(feedback_data)
            
            # Génération des recommandations
            recommendations = self._generate_recommendations(analysis)
            
            # Plan d'action prioritaire
            action_plan = self._create_action_plan(recommendations)
            
            result = {
                "feedback_analysis": analysis,
                "recommendations": recommendations,
                "action_plan": action_plan,
                "priority_score": self._calculate_priority_score(analysis),
                "estimated_impact": "Élevé - Amélioration significative de l'expérience utilisateur"
            }
            
            self.logger("ProductFeedbackAgent", "Analyse des retours terminée avec succès")
            return result
            
        except Exception as e:
            self.logger("ProductFeedbackAgent", f"Erreur lors de l'analyse: {str(e)}")
            raise
    
    def _analyze_feedback(self, feedback_data: List[Dict]) -> Dict:
        """Analyse les retours utilisateurs"""
        if not feedback_data:
            return {"error": "Aucun retour utilisateur fourni"}
        
        # Statistiques de base
        total_feedback = len(feedback_data)
        categories = {}
        sentiment_scores = []
        
        for feedback in feedback_data:
            # Catégorie
            category = feedback.get("category", "Général")
            categories[category] = categories.get(category, 0) + 1
            
            # Sentiment (simulation)
            sentiment = feedback.get("sentiment", random.choice(["positif", "neutre", "négatif"]))
            sentiment_scores.append(sentiment)
        
        # Calcul des métriques
        positive_count = sentiment_scores.count("positif")
        negative_count = sentiment_scores.count("négatif")
        neutral_count = sentiment_scores.count("neutre")
        
        analysis = {
            "total_feedback": total_feedback,
            "categories_distribution": categories,
            "sentiment_analysis": {
                "positive": positive_count,
                "negative": negative_count,
                "neutral": neutral_count,
                "satisfaction_rate": (positive_count / total_feedback) * 100 if total_feedback > 0 else 0
            },
            "top_issues": self._identify_top_issues(feedback_data),
            "user_satisfaction": "Moyenne" if (positive_count / total_feedback) > 0.6 else "Faible"
        }
        
        return analysis
    
    def _identify_top_issues(self, feedback_data: List[Dict]) -> List[str]:
        """Identifie les problèmes principaux"""
        issues = []
        for feedback in feedback_data:
            if feedback.get("sentiment") == "négatif":
                issue = feedback.get("issue", "Problème non spécifié")
                issues.append(issue)
        
        # Retourner les 3 problèmes les plus fréquents
        issue_counts = {}
        for issue in issues:
            issue_counts[issue] = issue_counts.get(issue, 0) + 1
        
        sorted_issues = sorted(issue_counts.items(), key=lambda x: x[1], reverse=True)
        return [issue for issue, count in sorted_issues[:3]]
    
    def _generate_recommendations(self, analysis: Dict) -> List[Dict]:
        """Génère des recommandations basées sur l'analyse"""
        recommendations = []
        
        # Recommandations basées sur la satisfaction
        satisfaction_rate = analysis["sentiment_analysis"]["satisfaction_rate"]
        
        if satisfaction_rate < 70:
            recommendations.append({
                "priority": "Haute",
                "category": "UX/UI",
                "action": "Audit complet de l'interface utilisateur",
                "impact": "Amélioration significative de la satisfaction utilisateur",
                "effort": "Moyen",
                "timeline": "2-3 semaines"
            })
        
        # Recommandations basées sur les catégories
        for category, count in analysis["categories_distribution"].items():
            if count > len(analysis["total_feedback"]) * 0.3:  # Plus de 30% des retours
                recommendations.append({
                    "priority": "Moyenne",
                    "category": category,
                    "action": f"Amélioration de la catégorie {category}",
                    "impact": f"Réduction des retours négatifs dans {category}",
                    "effort": "Faible",
                    "timeline": "1-2 semaines"
                })
        
        # Recommandations générales
        recommendations.append({
            "priority": "Basse",
            "category": "Processus",
            "action": "Mise en place d'un système de feedback continu",
            "impact": "Amélioration de la collecte et analyse des retours",
            "effort": "Faible",
            "timeline": "1 semaine"
        })
        
        return recommendations
    
    def _create_action_plan(self, recommendations: List[Dict]) -> Dict:
        """Crée un plan d'action prioritaire"""
        # Trier par priorité
        priority_order = {"Haute": 1, "Moyenne": 2, "Basse": 3}
        sorted_recommendations = sorted(recommendations, key=lambda x: priority_order.get(x["priority"], 4))
        
        action_plan = {
            "immediate_actions": [r for r in sorted_recommendations if r["priority"] == "Haute"],
            "short_term": [r for r in sorted_recommendations if r["priority"] == "Moyenne"],
            "long_term": [r for r in sorted_recommendations if r["priority"] == "Basse"],
            "total_effort": "Moyen",
            "estimated_timeline": "4-6 semaines",
            "success_metrics": [
                "Amélioration de 20% du taux de satisfaction",
                "Réduction de 30% des retours négatifs",
                "Augmentation de 15% de l'engagement utilisateur"
            ]
        }
        
        return action_plan
    
    def _calculate_priority_score(self, analysis: Dict) -> float:
        """Calcule un score de priorité basé sur l'analyse"""
        satisfaction_rate = analysis["sentiment_analysis"]["satisfaction_rate"]
        negative_count = analysis["sentiment_analysis"]["negative"]
        total_feedback = analysis["total_feedback"]
        
        # Score basé sur la satisfaction (0-100)
        satisfaction_score = satisfaction_rate
        
        # Score basé sur la proportion de retours négatifs (0-100)
        negative_score = (negative_count / total_feedback) * 100 if total_feedback > 0 else 0
        
        # Score final (moyenne pondérée)
        priority_score = (satisfaction_score * 0.7) + (negative_score * 0.3)
        
        return round(priority_score, 2)


# Fonction utilitaire
def analyze_user_feedback(feedback_data: List[Dict]) -> Dict:
    """
    Fonction utilitaire pour analyser les retours utilisateurs
    
    Args:
        feedback_data: Liste des retours utilisateurs
        
    Returns:
        Dict contenant l'analyse complète
    """
    agent = ProductFeedbackAgent()
    return agent.run(feedback_data)


if __name__ == "__main__":
    # Test de l'agent
    test_feedback = [
        {"category": "UX/UI", "sentiment": "négatif", "issue": "Interface trop complexe"},
        {"category": "Performance", "sentiment": "positif", "issue": "Rapide et efficace"},
        {"category": "Fonctionnalités", "sentiment": "neutre", "issue": "Fonctionnalités de base OK"}
    ]
    
    try:
        result = analyze_user_feedback(test_feedback)
        print("✅ Test ProductFeedbackAgent réussi!")
        print(f"Résultat: {json.dumps(result, indent=2)}")
    except Exception as e:
        print(f"❌ Test échoué: {e}")