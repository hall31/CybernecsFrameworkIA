#!/usr/bin/env python3
"""
Orchestrateur principal pour l'epic 9 - Infrastructure DevOps
Exécute InfraAgent, MonitoringAgent et AlertingAgent après AdsAgent
"""

import sys
import os
import json
import time
from typing import Dict, Any

# Ajout du chemin des agents
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'agents'))

from infra_agent import InfraAgent, MonitoringAgent, AlertingAgent


class InfrastructureOrchestrator:
    """Orchestrateur pour l'infrastructure DevOps"""
    
    def __init__(self):
        self.infra_agent = InfraAgent()
        self.monitoring_agent = MonitoringAgent()
        self.alerting_agent = AlertingAgent()
    
    def deploy_infrastructure(self, project_id: str) -> Dict[str, Any]:
        """
        Déploie l'infrastructure complète pour un projet
        
        Args:
            project_id: Identifiant unique du projet
            
        Returns:
            Dict contenant tous les résultats d'infrastructure
        """
        print(f"🚀 Démarrage du déploiement infrastructure pour {project_id}")
        
        try:
            # 1. Déploiement de l'infrastructure de base
            print("📦 Déploiement de l'infrastructure de base...")
            infra_result = self.infra_agent.run(project_id)
            
            if "error" in infra_result:
                return {"error": f"Erreur infrastructure: {infra_result['error']}"}
            
            # 2. Déploiement du monitoring
            print("📊 Déploiement du monitoring...")
            monitoring_result = self.monitoring_agent.run(project_id)
            
            if "error" in monitoring_result:
                return {"error": f"Erreur monitoring: {monitoring_result['error']}"}
            
            # 3. Configuration des alertes
            print("🚨 Configuration des alertes...")
            alerting_result = self.alerting_agent.run(project_id)
            
            if "error" in alerting_result:
                return {"error": f"Erreur alerting: {alerting_result['error']}"}
            
            # 4. Compilation des résultats
            infrastructure_summary = {
                "infra": infra_result,
                "monitoring": monitoring_result,
                "alerting": alerting_result,
                "deployment_time": time.time(),
                "status": "success"
            }
            
            print("✅ Infrastructure déployée avec succès!")
            return infrastructure_summary
            
        except Exception as e:
            error_msg = f"Erreur lors du déploiement infrastructure: {str(e)}"
            print(f"❌ {error_msg}")
            return {"error": error_msg, "status": "failed"}
    
    def get_infrastructure_status(self, project_id: str) -> Dict[str, Any]:
        """
        Récupère le statut de l'infrastructure d'un projet
        
        Args:
            project_id: Identifiant unique du projet
            
        Returns:
            Dict contenant le statut de l'infrastructure
        """
        try:
            # Simulation de la récupération du statut
            status = {
                "project_id": project_id,
                "cluster_status": "running",
                "pods_count": 3,
                "cpu_usage": 45.2,
                "memory_usage": 67.8,
                "uptime": "99.95%",
                "last_deployment": time.time() - 3600,  # 1 heure ago
                "monitoring_status": "active",
                "alerts_count": 0
            }
            
            return status
            
        except Exception as e:
            return {"error": f"Erreur lors de la récupération du statut: {str(e)}"}
    
    def scale_infrastructure(self, project_id: str, target_pods: int) -> Dict[str, Any]:
        """
        Met à l'échelle l'infrastructure d'un projet
        
        Args:
            project_id: Identifiant unique du projet
            target_pods: Nombre de pods cible
            
        Returns:
            Dict contenant le résultat du scaling
        """
        try:
            print(f"📈 Scaling de l'infrastructure {project_id} vers {target_pods} pods...")
            
            # Simulation du scaling
            time.sleep(2)
            
            scaling_result = {
                "project_id": project_id,
                "previous_pods": 3,
                "target_pods": target_pods,
                "current_pods": target_pods,
                "scaling_time": time.time(),
                "status": "completed"
            }
            
            print(f"✅ Scaling terminé: {scaling_result['previous_pods']} → {scaling_result['current_pods']} pods")
            return scaling_result
            
        except Exception as e:
            return {"error": f"Erreur lors du scaling: {str(e)}"}


def create_startup_with_infrastructure(idea: str) -> Dict[str, Any]:
    """
    Fonction principale pour créer une startup avec infrastructure complète
    
    Args:
        idea: Idée de la startup
        
    Returns:
        Dict contenant toutes les informations de la startup
    """
    print(f"🎯 Création de la startup: {idea}")
    
    # Génération d'un ID de projet unique
    project_id = f"startup-{int(time.time())}"
    
    # Création de l'orchestrateur
    orchestrator = InfrastructureOrchestrator()
    
    # Déploiement de l'infrastructure
    infrastructure_result = orchestrator.deploy_infrastructure(project_id)
    
    if "error" in infrastructure_result:
        return {"error": infrastructure_result["error"]}
    
    # Compilation du résultat final
    startup_result = {
        "project_id": project_id,
        "idea": idea,
        "created_at": time.time(),
        "status": "created",
        "infra": infrastructure_result["infra"],
        "monitoring": infrastructure_result["monitoring"],
        "alerting": infrastructure_result["alerting"],
        "summary": {
            "cluster": infrastructure_result["infra"]["cluster"],
            "url": infrastructure_result["infra"]["url"],
            "scaling": infrastructure_result["infra"]["scaling"],
            "grafana_url": infrastructure_result["monitoring"]["grafana_url"],
            "alerts": infrastructure_result["alerting"]["alerts"],
            "channels": infrastructure_result["alerting"]["channels"]
        }
    }
    
    print("🎉 Startup créée avec succès!")
    print(f"📊 Cluster: {startup_result['summary']['cluster']}")
    print(f"🌐 URL: {startup_result['summary']['url']}")
    print(f"📈 Scaling: {startup_result['summary']['scaling']}")
    print(f"📊 Monitoring: {startup_result['summary']['grafana_url']}")
    print(f"🚨 Alertes: {', '.join(startup_result['summary']['alerts'])}")
    
    return startup_result


# Fonction pour l'API REST
def handle_create_startup_request(request_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Gère une requête POST /create-startup
    
    Args:
        request_data: Données de la requête (doit contenir 'idea')
        
    Returns:
        Dict contenant la réponse
    """
    try:
        # Validation des données d'entrée
        if "idea" not in request_data:
            return {"error": "Le champ 'idea' est requis"}
        
        idea = request_data["idea"]
        if not idea or not isinstance(idea, str):
            return {"error": "Le champ 'idea' doit être une chaîne non vide"}
        
        # Création de la startup avec infrastructure
        result = create_startup_with_infrastructure(idea)
        
        return result
        
    except Exception as e:
        return {"error": f"Erreur lors du traitement de la requête: {str(e)}"}


if __name__ == "__main__":
    # Test de l'orchestrateur
    print("🧪 Test de l'orchestrateur d'infrastructure...")
    
    # Test avec une idée de startup
    test_idea = "SaaS marketplace pour freelances"
    result = create_startup_with_infrastructure(test_idea)
    
    print("\n📋 Résultat final:")
    print(json.dumps(result, indent=2, ensure_ascii=False))