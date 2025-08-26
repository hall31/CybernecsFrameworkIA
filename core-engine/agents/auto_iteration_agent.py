import json
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
import openai
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

class AutoIterationAgent:
    """
    Agent d'amélioration automatique du produit
    Génère des roadmaps d'amélioration basées sur le feedback et déclenche les DevAgents
    """
    
    def __init__(self, openai_api_key: str = None):
        self.openai_api_key = openai_api_key
        if openai_api_key:
            openai.api_key = openai_api_key
            self.llm = OpenAI(temperature=0.2, openai_api_key=openai_api_key)
        else:
            self.llm = None
        
        # Configuration du logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        # Simulation des DevAgents existants
        self.dev_agents = {
            "frontend": "FrontendDevAgent",
            "backend": "BackendDevAgent", 
            "database": "DatabaseDevAgent",
            "api": "APIIntegrationAgent"
        }
    
    def log_event(self, agent_name: str, message: str):
        """Log un événement avec timestamp"""
        timestamp = datetime.now().isoformat()
        self.logger.info(f"[{timestamp}] {agent_name}: {message}")
    
    def analyze_feedback(self, feedback: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyse le feedback pour identifier les priorités d'amélioration
        """
        if not self.llm:
            return self._fallback_feedback_analysis(feedback)
        
        analysis_prompt = PromptTemplate(
            input_variables=["feedback"],
            template="""
            Analyse ce feedback produit et identifie les améliorations prioritaires.
            
            Feedback: {feedback}
            
            Retourne un JSON avec:
            - priority_levels: ["high", "medium", "low"]
            - improvement_categories: ["ux", "performance", "features", "bugs"]
            - estimated_effort: estimation en jours pour chaque amélioration
            - business_impact: score d'impact business (1-10)
            """
        )
        
        try:
            chain = LLMChain(llm=self.llm, prompt=analysis_prompt)
            feedback_text = json.dumps(feedback, ensure_ascii=False)
            result = chain.run(feedback=feedback_text)
            
            return json.loads(result)
            
        except Exception as e:
            self.logger.error(f"Erreur analyse feedback: {e}")
            return self._fallback_feedback_analysis(feedback)
    
    def _fallback_feedback_analysis(self, feedback: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyse de fallback sans OpenAI
        """
        priority_levels = []
        improvement_categories = []
        
        # Analyse des problèmes
        issues = feedback.get("issues", [])
        if any("bug" in issue.lower() for issue in issues):
            priority_levels.append("high")
            improvement_categories.append("bugs")
        
        # Analyse des demandes de fonctionnalités
        features = feedback.get("features_requested", [])
        if len(features) > 2:
            priority_levels.append("medium")
            improvement_categories.append("features")
        
        # Analyse du sentiment
        sentiment = feedback.get("sentiment", "0% positif")
        if "positif" in sentiment and float(sentiment.split("%")[0]) < 80:
            priority_levels.append("medium")
            improvement_categories.append("ux")
        
        return {
            "priority_levels": list(set(priority_levels)),
            "improvement_categories": list(set(improvement_categories)),
            "estimated_effort": {"high": 3, "medium": 7, "low": 14},
            "business_impact": 7
        }
    
    def generate_user_stories(self, feedback: Dict[str, Any], analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Génère des user stories basées sur le feedback et l'analyse
        """
        user_stories = []
        
        # User stories pour les bugs
        for issue in feedback.get("issues", []):
            if "bug" in issue.lower() or "erreur" in issue.lower():
                user_stories.append({
                    "id": f"bug_{len(user_stories) + 1}",
                    "type": "bug_fix",
                    "title": f"Corriger: {issue}",
                    "description": f"Résoudre le problème: {issue}",
                    "priority": "high",
                    "effort_days": 1,
                    "acceptance_criteria": [
                        "Le bug est résolu",
                        "Tests de régression passent",
                        "Documentation mise à jour"
                    ]
                })
        
        # User stories pour les nouvelles fonctionnalités
        for feature in feedback.get("features_requested", []):
            user_stories.append({
                "id": f"feature_{len(user_stories) + 1}",
                "type": "new_feature",
                "title": f"Implémenter: {feature}",
                "description": f"Développer la fonctionnalité demandée: {feature}",
                "priority": "medium",
                "effort_days": 3,
                "acceptance_criteria": [
                    "Fonctionnalité fonctionnelle",
                    "Tests unitaires et d'intégration",
                    "Documentation utilisateur",
                    "Formation équipe support"
                ]
            })
        
        # User stories d'amélioration UX
        if feedback.get("user_satisfaction_score", 0) < 8:
            user_stories.append({
                "id": f"ux_{len(user_stories) + 1}",
                "type": "ux_improvement",
                "title": "Améliorer l'expérience utilisateur",
                "description": "Optimiser l'interface et les workflows",
                "priority": "medium",
                "effort_days": 5,
                "acceptance_criteria": [
                    "Tests utilisateur positifs",
                    "Amélioration des métriques UX",
                    "Feedback utilisateur positif"
                ]
            })
        
        return user_stories
    
    def create_roadmap(self, user_stories: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Crée une roadmap d'amélioration basée sur les user stories
        """
        # Tri par priorité et effort
        priority_order = {"high": 1, "medium": 2, "low": 3}
        sorted_stories = sorted(user_stories, key=lambda x: (
            priority_order.get(x.get("priority", "low"), 3),
            x.get("effort_days", 0)
        ))
        
        # Groupement par sprint (2 semaines)
        sprints = []
        current_sprint = []
        current_effort = 0
        max_sprint_effort = 10  # 10 jours max par sprint
        
        for story in sorted_stories:
            story_effort = story.get("effort_days", 0)
            
            if current_effort + story_effort > max_sprint_effort and current_sprint:
                sprints.append({
                    "sprint_number": len(sprints) + 1,
                    "stories": current_sprint,
                    "total_effort": current_effort,
                    "estimated_duration": "2 semaines"
                })
                current_sprint = []
                current_effort = 0
            
            current_sprint.append(story)
            current_effort += story_effort
        
        # Ajouter le dernier sprint
        if current_sprint:
            sprints.append({
                "sprint_number": len(sprints) + 1,
                "stories": current_sprint,
                "total_effort": current_effort,
                "estimated_duration": "2 semaines"
            })
        
        roadmap = {
            "created_at": datetime.now().isoformat(),
            "total_stories": len(user_stories),
            "total_effort_days": sum(s.get("effort_days", 0) for s in user_stories),
            "estimated_completion": (datetime.now() + timedelta(days=len(sprints) * 14)).isoformat(),
            "sprints": sprints,
            "priority_distribution": {
                "high": len([s for s in user_stories if s.get("priority") == "high"]),
                "medium": len([s for s in user_stories if s.get("priority") == "medium"]),
                "low": len([s for s in user_stories if s.get("priority") == "low"])
            }
        }
        
        return roadmap
    
    def trigger_dev_agents(self, user_stories: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Déclenche les DevAgents appropriés pour chaque user story
        """
        agent_assignments = {}
        
        for story in user_stories:
            story_type = story.get("type", "")
            
            if story_type == "bug_fix":
                # Bugs peuvent nécessiter plusieurs agents
                agent_assignments[story["id"]] = {
                    "agents": ["backend", "frontend"],
                    "priority": story.get("priority", "medium"),
                    "estimated_completion": (datetime.now() + timedelta(days=story.get("effort_days", 1))).isoformat()
                }
            
            elif story_type == "new_feature":
                # Nouvelles fonctionnalités
                if "api" in story.get("title", "").lower():
                    agent_assignments[story["id"]] = {
                        "agents": ["api", "backend"],
                        "priority": story.get("priority", "medium"),
                        "estimated_completion": (datetime.now() + timedelta(days=story.get("effort_days", 3))).isoformat()
                    }
                else:
                    agent_assignments[story["id"]] = {
                        "agents": ["frontend", "backend"],
                        "priority": story.get("priority", "medium"),
                        "estimated_completion": (datetime.now() + timedelta(days=story.get("effort_days", 3))).isoformat()
                    }
            
            elif story_type == "ux_improvement":
                # Améliorations UX
                agent_assignments[story["id"]] = {
                    "agents": ["frontend"],
                    "priority": story.get("priority", "medium"),
                    "estimated_completion": (datetime.now() + timedelta(days=story.get("effort_days", 5))).isoformat()
                }
        
        return {
            "total_assignments": len(agent_assignments),
            "assignments": agent_assignments,
            "agents_utilized": list(set([agent for assignment in agent_assignments.values() for agent in assignment["agents"]]))
        }
    
    def run(self, project_id: str, feedback: Dict[str, Any]) -> Dict[str, Any]:
        """
        Méthode principale qui exécute l'itération automatique
        """
        try:
            self.log_event("AutoIterationAgent", f"Démarrage itération pour projet {project_id}")
            
            # 1. Analyse du feedback
            analysis = self.analyze_feedback(feedback)
            self.logger.info(f"Analyse feedback terminée: {len(analysis.get('improvement_categories', []))} catégories identifiées")
            
            # 2. Génération des user stories
            user_stories = self.generate_user_stories(feedback, analysis)
            self.logger.info(f"User stories générées: {len(user_stories)} stories créées")
            
            # 3. Création de la roadmap
            roadmap = self.create_roadmap(user_stories)
            self.logger.info(f"Roadmap créée: {len(roadmap.get('sprints', []))} sprints planifiés")
            
            # 4. Déclenchement des DevAgents
            dev_assignments = self.trigger_dev_agents(user_stories)
            self.logger.info(f"DevAgents déclenchés: {dev_assignments.get('total_assignments', 0)} assignations")
            
            # 5. Résultat final
            result = {
                "project_id": project_id,
                "timestamp": datetime.now().isoformat(),
                "status": "improvements_scheduled",
                "analysis": analysis,
                "user_stories": user_stories,
                "roadmap": roadmap,
                "dev_assignments": dev_assignments,
                "summary": {
                    "total_improvements": len(user_stories),
                    "estimated_completion": roadmap.get("estimated_completion"),
                    "total_effort_days": roadmap.get("total_effort_days"),
                    "agents_involved": dev_assignments.get("agents_utilized", [])
                }
            }
            
            self.log_event("AutoIterationAgent", "Nouvelle roadmap générée")
            self.logger.info(f"Itération terminée avec succès pour projet {project_id}")
            
            return result
            
        except Exception as e:
            error_msg = f"Erreur dans AutoIterationAgent: {str(e)}"
            self.logger.error(error_msg)
            self.log_event("AutoIterationAgent", f"ERREUR: {error_msg}")
            
            return {
                "error": error_msg,
                "timestamp": datetime.now().isoformat(),
                "status": "failed"
            }

# Test du agent
if __name__ == "__main__":
    # Feedback simulé
    mock_feedback = {
        "issues": ["Bug checkout", "UI lente"],
        "features_requested": ["Mode sombre", "Intégration PayPal"],
        "sentiment": "78% positif",
        "user_satisfaction_score": 7.8
    }
    
    agent = AutoIterationAgent()
    result = agent.run("test-project-123", mock_feedback)
    print(json.dumps(result, indent=2, ensure_ascii=False))