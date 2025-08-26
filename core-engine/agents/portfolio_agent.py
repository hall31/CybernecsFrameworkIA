import logging
from typing import Dict, List, Any
from datetime import datetime
import json

class PortfolioAgent:
    """
    AI Portfolio Manager - Gère l'analyse et l'allocation des ressources
    pour un portefeuille de startups
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.portfolio_data = {}
        
    def log_event(self, agent_name: str, message: str, level: str = "INFO"):
        """Log un événement avec timestamp"""
        timestamp = datetime.now().isoformat()
        log_entry = {
            "timestamp": timestamp,
            "agent": agent_name,
            "message": message,
            "level": level
        }
        
        if level == "INFO":
            self.logger.info(f"[{agent_name}] {message}")
        elif level == "WARNING":
            self.logger.warning(f"[{agent_name}] {message}")
        elif level == "ERROR":
            self.logger.error(f"[{agent_name}] {message}")
            
        return log_entry
    
    def get_all_startups(self) -> List[Dict[str, Any]]:
        """Récupère toutes les startups depuis la base de données"""
        # Simulation des données startups (en production, ceci viendrait de la DB)
        startups = [
            {
                "id": "startup001",
                "name": "CloudFlow",
                "idea": "Plateforme de gestion cloud multi-tenant",
                "valuation": "12M €",
                "mrr": 45000,
                "cac": 120,
                "churn": 0.08,
                "status": "Investir",
                "kpis": {"growth_rate": 0.25, "ltv": 1800}
            },
            {
                "id": "startup002", 
                "name": "DataViz",
                "idea": "Outils de visualisation de données en temps réel",
                "valuation": "8M €",
                "mrr": 32000,
                "cac": 95,
                "churn": 0.12,
                "status": "Hold",
                "kpis": {"growth_rate": 0.18, "ltv": 1400}
            },
            {
                "id": "startup003",
                "name": "AIHelper",
                "idea": "Assistant IA pour support client",
                "valuation": "15M €", 
                "mrr": 68000,
                "cac": 150,
                "churn": 0.05,
                "status": "Investir",
                "kpis": {"growth_rate": 0.32, "ltv": 2200}
            },
            {
                "id": "startup004",
                "name": "SecurePay",
                "idea": "Solution de paiement sécurisé B2B",
                "valuation": "6M €",
                "mrr": 28000,
                "cac": 110,
                "churn": 0.15,
                "status": "Drop",
                "kpis": {"growth_rate": 0.08, "ltv": 900}
            },
            {
                "id": "startup005",
                "name": "GreenTech",
                "idea": "Monitoring environnemental IoT",
                "valuation": "10M €",
                "mrr": 52000,
                "cac": 130,
                "churn": 0.09,
                "status": "Investir",
                "kpis": {"growth_rate": 0.22, "ltv": 1600}
            },
            {
                "id": "startup006",
                "name": "EduTech",
                "idea": "Plateforme d'apprentissage adaptatif",
                "valuation": "7M €",
                "mrr": 38000,
                "cac": 85,
                "churn": 0.11,
                "status": "Hold",
                "kpis": {"growth_rate": 0.19, "ltv": 1200}
            },
            {
                "id": "startup007",
                "name": "HealthAI",
                "idea": "Diagnostic médical assisté par IA",
                "valuation": "20M €",
                "mrr": 95000,
                "cac": 200,
                "churn": 0.04,
                "status": "Investir",
                "kpis": {"growth_rate": 0.45, "ltv": 2800}
            },
            {
                "id": "startup008",
                "name": "LogiChain",
                "idea": "Blockchain pour la logistique",
                "valuation": "5M €",
                "mrr": 22000,
                "cac": 140,
                "churn": 0.18,
                "status": "Drop",
                "kpis": {"growth_rate": 0.06, "ltv": 750}
            },
            {
                "id": "startup009",
                "name": "SocialCRM",
                "idea": "CRM intégré aux réseaux sociaux",
                "valuation": "9M €",
                "mrr": 41000,
                "cac": 100,
                "churn": 0.10,
                "status": "Hold",
                "kpis": {"growth_rate": 0.20, "ltv": 1300}
            },
            {
                "id": "startup010",
                "name": "QuantumML",
                "idea": "Machine Learning quantique",
                "valuation": "25M €",
                "mrr": 120000,
                "cac": 300,
                "churn": 0.03,
                "status": "Investir",
                "kpis": {"growth_rate": 0.55, "ltv": 3500}
            }
        ]
        
        self.log_event("PortfolioAgent", f"Récupération de {len(startups)} startups")
        return startups
    
    def evaluate_startup(self, startup: Dict[str, Any]) -> Dict[str, Any]:
        """Évalue une startup via l'InvestorAgent (simulation)"""
        # Simulation de l'évaluation par InvestorAgent
        score = 0
        
        # Score basé sur MRR
        if startup["mrr"] > 50000:
            score += 30
        elif startup["mrr"] > 30000:
            score += 20
        else:
            score += 10
            
        # Score basé sur Churn
        if startup["churn"] < 0.08:
            score += 25
        elif startup["churn"] < 0.12:
            score += 15
        else:
            score += 5
            
        # Score basé sur croissance
        if startup["kpis"]["growth_rate"] > 0.25:
            score += 25
        elif startup["kpis"]["growth_rate"] > 0.15:
            score += 15
        else:
            score += 5
            
        # Score basé sur LTV
        if startup["kpis"]["ltv"] > 2000:
            score += 20
        elif startup["kpis"]["ltv"] > 1200:
            score += 15
        else:
            score += 10
            
        # Détermination du status basé sur le score
        if score >= 80:
            startup["status"] = "Investir"
        elif score >= 60:
            startup["status"] = "Hold"
        else:
            startup["status"] = "Drop"
            
        startup["evaluation_score"] = score
        return startup
    
    def calculate_portfolio_value(self, startups: List[Dict[str, Any]]) -> str:
        """Calcule la valeur totale du portefeuille"""
        total_value = 0
        for startup in startups:
            # Extraction de la valeur numérique robuste (ex: "12M €", "500K €", "1.2B €")
            value = self._parse_valuation(startup.get("valuation", ""))
            if value is not None:
                total_value += value
                
        # Formatage en millions d'euros
        if total_value >= 1000000:
            return f"{total_value / 1000000:.1f}M €"
        else:
            return f"{total_value / 1000:.1f}K €"
    
    def identify_best_startup(self, startups: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Identifie la meilleure startup du portefeuille"""
        best_startup = None
        best_score = 0
        
        for startup in startups:
            if startup.get("evaluation_score", 0) > best_score:
                best_score = startup["evaluation_score"]
                best_startup = startup
                
        return best_startup or {}
    
    def identify_underperformers(self, startups: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Identifie les startups sous-performantes"""
        underperformers = []
        for startup in startups:
            if startup["status"] == "Drop" or startup.get("evaluation_score", 0) < 50:
                underperformers.append({
                    "id": startup["id"],
                    "idea": startup["idea"],
                    "churn": startup["churn"],
                    "score": startup.get("evaluation_score", 0)
                })
        return underperformers
    
    def calculate_resource_allocation(self, startups: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calcule l'allocation des ressources basée sur la performance"""
        allocation = {
            "cloud_credits": {},
            "ad_budget": {},
            "dev_agents": {}
        }
        
        # Allocation basée sur le score d'évaluation
        for startup in startups:
            score = startup.get("evaluation_score", 0)
            if score >= 80:  # Top performers
                allocation["cloud_credits"][startup["id"]] = "25%"
                allocation["ad_budget"][startup["id"]] = "30%"
                allocation["dev_agents"][startup["id"]] = "40%"
            elif score >= 60:  # Moyens
                allocation["cloud_credits"][startup["id"]] = "15%"
                allocation["ad_budget"][startup["id"]] = "20%"
                allocation["dev_agents"][startup["id"]] = "25%"
            else:  # Sous-performants
                allocation["cloud_credits"][startup["id"]] = "5%"
                allocation["ad_budget"][startup["id"]] = "5%"
                allocation["dev_agents"][startup["id"]] = "10%"
                
        return allocation
    
    def generate_recommendations(self, startups: List[Dict[str, Any]]) -> List[str]:
        """Génère des recommandations d'allocation des ressources"""
        recommendations = []
        
        # Analyse des tendances
        invest_count = len([s for s in startups if s["status"] == "Investir"])
        hold_count = len([s for s in startups if s["status"] == "Hold"])
        drop_count = len([s for s in startups if s["status"] == "Drop"])
        
        if invest_count > len(startups) * 0.6:
            recommendations.append("Portefeuille très performant - Augmenter les investissements")
        elif drop_count > len(startups) * 0.3:
            recommendations.append("Attention: Trop de startups sous-performantes - Révision nécessaire")
            
        # Recommandations par type de ressource
        total_mrr = sum(s["mrr"] for s in startups)
        for startup in startups:
            if startup["mrr"] > total_mrr / len(startups):
                recommendations.append(f"Augmenter budget pub pour {startup['name']} (MRR élevé)")
            if startup["kpis"]["growth_rate"] > 0.3:
                recommendations.append(f"Allouer plus de dev agents à {startup['name']} (croissance forte)")
                
        return recommendations
    
    def run(self) -> Dict[str, Any]:
        """Méthode principale - Exécute l'analyse complète du portefeuille"""
        try:
            self.log_event("PortfolioAgent", "Démarrage de l'analyse du portefeuille")
            
            # 1. Récupération des startups
            startups = self.get_all_startups()
            
            # 2. Évaluation de chaque startup
            evaluated_startups = []
            for startup in startups:
                evaluated_startup = self.evaluate_startup(startup)
                evaluated_startups.append(evaluated_startup)
            
            # 3. Calculs du portefeuille
            portfolio_value = self.calculate_portfolio_value(evaluated_startups)
            best_startup = self.identify_best_startup(evaluated_startups)
            underperformers = self.identify_underperformers(evaluated_startups)
            resource_allocation = self.calculate_resource_allocation(evaluated_startups)
            recommendations = self.generate_recommendations(evaluated_startups)
            
            # 4. Construction du tableau de bord
            dashboard = {
                "total_startups": len(evaluated_startups),
                "portfolio_value": portfolio_value,
                "best_startup": {
                    "id": best_startup.get("id", ""),
                    "name": best_startup.get("name", ""),
                    "idea": best_startup.get("idea", ""),
                    "valuation": best_startup.get("valuation", ""),
                    "score": best_startup.get("evaluation_score", 0)
                },
                "underperformers": underperformers,
                "resource_allocation": resource_allocation,
                "recommendations": recommendations,
                "startups_summary": {
                    "invest": len([s for s in evaluated_startups if s["status"] == "Investir"]),
                    "hold": len([s for s in evaluated_startups if s["status"] == "Hold"]),
                    "drop": len([s for s in evaluated_startups if s["status"] == "Drop"])
                },
                "timestamp": datetime.now().isoformat()
            }
            
            self.portfolio_data = dashboard
            self.log_event("PortfolioAgent", "Analyse du portefeuille complétée")
            
            return dashboard
            
        except Exception as e:
            error_msg = f"Erreur lors de l'analyse du portefeuille: {str(e)}"
            self.log_event("PortfolioAgent", error_msg, "ERROR")
            return {"error": error_msg, "timestamp": datetime.now().isoformat()}
    
    def get_portfolio_summary(self) -> Dict[str, Any]:
        """Retourne un résumé du portefeuille"""
        if not self.portfolio_data:
            return {"message": "Aucune analyse disponible. Exécutez run() d'abord."}
        return self.portfolio_data

if __name__ == "__main__":
    # Test du PortfolioAgent
    logging.basicConfig(level=logging.INFO)
    agent = PortfolioAgent()
    result = agent.run()
    print(json.dumps(result, indent=2, ensure_ascii=False))