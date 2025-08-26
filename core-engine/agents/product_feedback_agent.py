import json
import logging
from typing import Dict, List, Any
from datetime import datetime
import openai
from langchain_openai.llms import OpenAI
from langchain_core.chains import LLMChain
from langchain_core.prompts import PromptTemplate

class ProductFeedbackAgent:
    """
    Agent d'analyse du feedback produit avec NLP
    Collecte et analyse les retours utilisateurs pour identifier problèmes et demandes
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
    
    def log_event(self, agent_name: str, message: str):
        """Log un événement avec timestamp"""
        timestamp = datetime.now().isoformat()
        self.logger.info(f"[{timestamp}] {agent_name}: {message}")
    
    def collect_user_feedback(self, project_id: str) -> Dict[str, Any]:
        """
        Collecte le feedback utilisateur depuis différentes sources
        Simulation des données réelles
        """
        # TODO: Intégrer avec vraies APIs (Intercom, Zendesk, etc.)
        mock_feedback = {
            "reviews": [
                {"rating": 4, "comment": "Interface intuitive mais checkout lent", "date": "2024-01-15"},
                {"rating": 5, "comment": "Excellent outil, ajoutez un mode sombre", "date": "2024-01-14"},
                {"rating": 3, "comment": "Bug sur la page de paiement", "date": "2024-01-13"},
                {"rating": 4, "comment": "Intégration PayPal manquante", "date": "2024-01-12"},
                {"rating": 5, "comment": "Parfait pour mon workflow", "date": "2024-01-11"}
            ],
            "support_tickets": [
                {"priority": "high", "issue": "Erreur 500 sur checkout", "status": "resolved"},
                {"priority": "medium", "issue": "Demande mode sombre", "status": "open"},
                {"priority": "low", "issue": "Intégration PayPal", "status": "open"}
            ],
            "analytics": {
                "bounce_rate": 23.5,
                "avg_session_duration": "4m 32s",
                "conversion_rate": 12.8
            }
        }
        
        return mock_feedback
    
    def analyze_with_nlp(self, feedback_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyse le feedback avec NLP pour extraire insights
        """
        if not self.llm:
            # Fallback sans OpenAI
            return self._fallback_analysis(feedback_data)
        
        # Prompt pour l'analyse NLP
        analysis_prompt = PromptTemplate(
            input_variables=["feedback"],
            template="""
            Analyse ce feedback utilisateur et extrait les informations suivantes au format JSON:
            
            Feedback: {feedback}
            
            Retourne un JSON avec:
            - issues: liste des problèmes/bugs identifiés
            - features_requested: liste des fonctionnalités demandées
            - sentiment: pourcentage de sentiment positif (0-100%)
            - priority_issues: problèmes prioritaires à résoudre
            - user_satisfaction_score: score de satisfaction (1-10)
            """
        )
        
        try:
            chain = LLMChain(llm=self.llm, prompt=analysis_prompt)
            feedback_text = json.dumps(feedback_data, ensure_ascii=False)
            result = chain.run(feedback=feedback_text)
            
            # Parse du résultat JSON
            analysis = json.loads(result)
            return analysis
            
        except Exception as e:
            self.logger.error(f"Erreur analyse NLP: {e}")
            return self._fallback_analysis(feedback_data)
    
    def _fallback_analysis(self, feedback_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyse de fallback sans OpenAI
        """
        issues = []
        features_requested = []
        
        # Analyse des reviews
        for review in feedback_data.get("reviews", []):
            comment = review.get("comment", "").lower()
            if any(word in comment for word in ["bug", "erreur", "problème", "lent"]):
                issues.append(f"Problème: {review['comment']}")
            if any(word in comment for word in ["ajoutez", "intégration", "mode"]):
                features_requested.append(f"Demande: {review['comment']}")
        
        # Analyse des tickets support
        for ticket in feedback_data.get("support_tickets", []):
            if ticket.get("priority") == "high":
                issues.append(f"Ticket prioritaire: {ticket['issue']}")
            if "demande" in ticket.get("issue", "").lower():
                features_requested.append(f"Demande support: {ticket['issue']}")
        
        # Calcul sentiment basique
        total_reviews = len(feedback_data.get("reviews", []))
        positive_reviews = sum(1 for r in feedback_data.get("reviews", []) if r.get("rating", 0) >= 4)
        sentiment = round((positive_reviews / total_reviews * 100) if total_reviews > 0 else 0, 1)
        
        return {
            "issues": list(set(issues))[:5],  # Top 5 problèmes
            "features_requested": list(set(features_requested))[:5],  # Top 5 demandes
            "sentiment": f"{sentiment}% positif",
            "priority_issues": [i for i in issues if "prioritaire" in i.lower()],
            "user_satisfaction_score": round(sentiment / 10, 1)
        }
    
    def generate_report(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """
        Génère un rapport final structuré
        """
        report = {
            "timestamp": datetime.now().isoformat(),
            "summary": {
                "total_issues": len(analysis.get("issues", [])),
                "total_features_requested": len(analysis.get("features_requested", [])),
                "sentiment_score": analysis.get("sentiment", "N/A"),
                "satisfaction_score": analysis.get("user_satisfaction_score", 0)
            },
            "issues": analysis.get("issues", []),
            "features_requested": analysis.get("features_requested", []),
            "sentiment": analysis.get("sentiment", "N/A"),
            "priority_issues": analysis.get("priority_issues", []),
            "recommendations": self._generate_recommendations(analysis)
        }
        
        return report
    
    def _generate_recommendations(self, analysis: Dict[str, Any]) -> List[str]:
        """
        Génère des recommandations basées sur l'analyse
        """
        recommendations = []
        
        if analysis.get("user_satisfaction_score", 0) < 7:
            recommendations.append("Priorité haute: Améliorer l'expérience utilisateur")
        
        if len(analysis.get("priority_issues", [])) > 0:
            recommendations.append("Résoudre immédiatement les problèmes prioritaires")
        
        if len(analysis.get("features_requested", [])) > 3:
            recommendations.append("Évaluer les fonctionnalités les plus demandées")
        
        if not recommendations:
            recommendations.append("Maintenir la qualité actuelle du produit")
        
        return recommendations
    
    def run(self, project_id: str) -> Dict[str, Any]:
        """
        Méthode principale qui exécute l'analyse complète
        """
        try:
            self.log_event("ProductFeedbackAgent", f"Démarrage analyse pour projet {project_id}")
            
            # 1. Collecte du feedback
            feedback_data = self.collect_user_feedback(project_id)
            self.logger.info(f"Feedback collecté: {len(feedback_data.get('reviews', []))} reviews")
            
            # 2. Analyse NLP
            analysis = self.analyze_with_nlp(feedback_data)
            self.logger.info(f"Analyse NLP terminée: {len(analysis.get('issues', []))} problèmes identifiés")
            
            # 3. Génération du rapport
            report = self.generate_report(analysis)
            
            self.log_event("ProductFeedbackAgent", "Analyse feedback générée")
            self.logger.info(f"Rapport généré avec succès pour projet {project_id}")
            
            return report
            
        except Exception as e:
            error_msg = f"Erreur dans ProductFeedbackAgent: {str(e)}"
            self.logger.error(error_msg)
            self.log_event("ProductFeedbackAgent", f"ERREUR: {error_msg}")
            
            return {
                "error": error_msg,
                "timestamp": datetime.now().isoformat(),
                "status": "failed"
            }

# Test du agent
if __name__ == "__main__":
    agent = ProductFeedbackAgent()
    result = agent.run("test-project-123")
    print(json.dumps(result, indent=2, ensure_ascii=False))