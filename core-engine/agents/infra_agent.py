#!/usr/bin/env python3
"""
InfraAgent - Agent DevOps pour déploiement cloud avec auto-scaling
Gère le déploiement Kubernetes, monitoring Prometheus/Grafana et alerting
"""

import os
import json
import time
import random
from typing import Dict, List, Optional
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class InfraAgent:
    """Agent principal pour l'infrastructure DevOps"""
    
    def __init__(self):
        self.cluster_name = None
        self.project_url = None
        self.scaling_config = {"min_pods": 2, "max_pods": 20, "cpu_threshold": 70}
    
    def run(self, project_id: str) -> Dict:
        """
        Déploie l'infrastructure complète pour un projet
        
        Args:
            project_id: Identifiant unique du projet
            
        Returns:
            Dict contenant les informations de déploiement
        """
        try:
            logger.info(f"🚀 Démarrage du déploiement infrastructure pour {project_id}")
            
            # 1. Déploiement du cluster Kubernetes
            cluster_info = self._deploy_kubernetes_cluster(project_id)
            
            # 2. Configuration de l'auto-scaling
            scaling_info = self._configure_autoscaling(project_id)
            
            # 3. Configuration du LoadBalancer
            lb_info = self._configure_loadbalancer(project_id)
            
            # 4. Configuration SSL
            ssl_info = self._configure_ssl(project_id)
            
            # Log de l'événement
            self._log_event("InfraAgent", "Cluster déployé et scaling activé")
            
            return {
                "cluster": cluster_info["name"],
                "url": lb_info["url"],
                "scaling": f"{self.scaling_config['min_pods']}-{self.scaling_config['max_pods']} pods",
                "ssl": ssl_info["status"],
                "loadbalancer": lb_info["type"]
            }
            
        except Exception as e:
            logger.error(f"❌ Erreur lors du déploiement infrastructure: {e}")
            return {"error": str(e)}
    
    def _deploy_kubernetes_cluster(self, project_id: str) -> Dict:
        """Déploie un cluster Kubernetes (EKS ou GKE)"""
        logger.info(f"🔧 Déploiement du cluster Kubernetes pour {project_id}")
        
        # Simulation du déploiement
        time.sleep(2)
        
        # Génération d'un nom de cluster unique
        cluster_name = f"gke-{project_id}-{random.randint(1000, 9999)}"
        self.cluster_name = cluster_name
        
        logger.info(f"✅ Cluster {cluster_name} déployé avec succès")
        
        return {
            "name": cluster_name,
            "provider": "GKE",
            "region": "europe-west1",
            "node_count": 3,
            "status": "running"
        }
    
    def _configure_autoscaling(self, project_id: str) -> Dict:
        """Configure l'auto-scaling horizontal (HPA)"""
        logger.info(f"📈 Configuration de l'auto-scaling pour {project_id}")
        
        # Simulation de la configuration HPA
        time.sleep(1)
        
        hpa_config = {
            "min_replicas": self.scaling_config["min_pods"],
            "max_replicas": self.scaling_config["max_pods"],
            "cpu_threshold": self.scaling_config["cpu_threshold"],
            "memory_threshold": 80,
            "scale_up_cooldown": 300,
            "scale_down_cooldown": 300
        }
        
        logger.info(f"✅ HPA configuré: {hpa_config['min_replicas']}-{hpa_config['max_replicas']} pods")
        
        return hpa_config
    
    def _configure_loadbalancer(self, project_id: str) -> Dict:
        """Configure le LoadBalancer avec Nginx Ingress"""
        logger.info(f"🌐 Configuration du LoadBalancer pour {project_id}")
        
        # Simulation de la configuration
        time.sleep(1)
        
        # Génération de l'URL du projet
        project_url = f"https://{project_id}.app"
        self.project_url = project_url
        
        lb_config = {
            "type": "Nginx Ingress",
            "url": project_url,
            "ip": f"35.195.{random.randint(1, 255)}.{random.randint(1, 255)}",
            "ports": [80, 443],
            "health_check": "/health"
        }
        
        logger.info(f"✅ LoadBalancer configuré: {project_url}")
        
        return lb_config
    
    def _configure_ssl(self, project_id: str) -> Dict:
        """Configure les certificats SSL via cert-manager"""
        logger.info(f"🔒 Configuration SSL pour {project_id}")
        
        # Simulation de la configuration SSL
        time.sleep(1)
        
        ssl_config = {
            "status": "active",
            "provider": "cert-manager",
            "issuer": "letsencrypt-prod",
            "domains": [f"{project_id}.app", f"www.{project_id}.app"],
            "expiry": "2024-11-19",
            "auto_renewal": True
        }
        
        logger.info(f"✅ Certificat SSL configuré pour {project_id}.app")
        
        return ssl_config
    
    def _log_event(self, agent_name: str, message: str):
        """Log un événement d'infrastructure"""
        event = {
            "timestamp": time.time(),
            "agent": agent_name,
            "message": message,
            "level": "info"
        }
        logger.info(f"📝 {agent_name}: {message}")


class MonitoringAgent:
    """Agent pour le monitoring et l'observabilité"""
    
    def __init__(self):
        self.grafana_url = None
        self.dashboards = []
    
    def run(self, project_id: str) -> Dict:
        """
        Déploie le stack de monitoring Prometheus + Grafana
        
        Args:
            project_id: Identifiant unique du projet
            
        Returns:
            Dict contenant les informations de monitoring
        """
        try:
            logger.info(f"📊 Démarrage du déploiement monitoring pour {project_id}")
            
            # 1. Déploiement Prometheus
            prometheus_info = self._deploy_prometheus(project_id)
            
            # 2. Déploiement Grafana
            grafana_info = self._deploy_grafana(project_id)
            
            # 3. Configuration des dashboards
            dashboards_info = self._configure_dashboards(project_id)
            
            # 4. Configuration des métriques
            metrics_info = self._configure_metrics(project_id)
            
            # Log de l'événement
            self._log_event("MonitoringAgent", "Monitoring déployé avec Grafana")
            
            return {
                "grafana_url": grafana_info["url"],
                "dashboards": dashboards_info["names"],
                "prometheus_url": prometheus_info["url"],
                "metrics_count": metrics_info["count"]
            }
            
        except Exception as e:
            logger.error(f"❌ Erreur lors du déploiement monitoring: {e}")
            return {"error": str(e)}
    
    def _deploy_prometheus(self, project_id: str) -> Dict:
        """Déploie Prometheus dans Kubernetes"""
        logger.info(f"🔍 Déploiement de Prometheus pour {project_id}")
        
        time.sleep(1)
        
        prometheus_config = {
            "url": f"https://prometheus.{project_id}.app",
            "storage": "50Gi",
            "retention": "15d",
            "scrape_interval": "15s",
            "targets": ["pods", "services", "nodes"]
        }
        
        logger.info(f"✅ Prometheus déployé: {prometheus_config['url']}")
        
        return prometheus_config
    
    def _deploy_grafana(self, project_id: str) -> Dict:
        """Déploie Grafana dans Kubernetes"""
        logger.info(f"📈 Déploiement de Grafana pour {project_id}")
        
        time.sleep(1)
        
        grafana_config = {
            "url": f"https://monitoring.{project_id}.app",
            "admin_user": "admin",
            "admin_password": "admin123",
            "plugins": ["prometheus", "kubernetes", "grafana-worldmap"],
            "datasources": ["prometheus", "kubernetes"]
        }
        
        self.grafana_url = grafana_config["url"]
        logger.info(f"✅ Grafana déployé: {self.grafana_url}")
        
        return grafana_config
    
    def _configure_dashboards(self, project_id: str) -> Dict:
        """Configure les dashboards Grafana"""
        logger.info(f"📋 Configuration des dashboards pour {project_id}")
        
        time.sleep(1)
        
        dashboard_configs = [
            {
                "name": "performance",
                "title": "Performance Dashboard",
                "panels": ["CPU Usage", "Memory Usage", "Network I/O", "Disk I/O"]
            },
            {
                "name": "errors",
                "title": "Errors Dashboard", 
                "panels": ["HTTP Errors 4xx", "HTTP Errors 5xx", "Application Errors", "Database Errors"]
            },
            {
                "name": "uptime",
                "title": "Uptime Dashboard",
                "panels": ["Service Status", "Response Time", "Availability", "Health Checks"]
            }
        ]
        
        self.dashboards = [d["name"] for d in dashboard_configs]
        
        logger.info(f"✅ Dashboards configurés: {', '.join(self.dashboards)}")
        
        return {
            "names": self.dashboards,
            "count": len(self.dashboards),
            "configs": dashboard_configs
        }
    
    def _configure_metrics(self, project_id: str) -> Dict:
        """Configure la collecte de métriques"""
        logger.info(f"📊 Configuration des métriques pour {project_id}")
        
        time.sleep(1)
        
        metrics_config = {
            "count": 15,
            "types": [
                "cpu_usage", "memory_usage", "network_io", "disk_io",
                "http_requests", "http_errors", "response_time", "throughput",
                "pod_count", "node_status", "service_health", "api_latency",
                "database_connections", "cache_hit_rate", "queue_length"
            ],
            "scrape_interval": "15s"
        }
        
        logger.info(f"✅ {metrics_config['count']} métriques configurées")
        
        return metrics_config
    
    def _log_event(self, agent_name: str, message: str):
        """Log un événement de monitoring"""
        event = {
            "timestamp": time.time(),
            "agent": agent_name,
            "message": message,
            "level": "info"
        }
        logger.info(f"📝 {agent_name}: {message}")


class AlertingAgent:
    """Agent pour la configuration des alertes"""
    
    def __init__(self):
        self.alerts = []
        self.channels = []
    
    def run(self, project_id: str) -> Dict:
        """
        Configure les alertes Grafana vers Slack/Discord/Email
        
        Args:
            project_id: Identifiant unique du projet
            
        Returns:
            Dict contenant les informations d'alerting
        """
        try:
            logger.info(f"🚨 Configuration des alertes pour {project_id}")
            
            # 1. Configuration des règles d'alerte
            alert_rules = self._configure_alert_rules(project_id)
            
            # 2. Configuration des canaux de notification
            notification_channels = self._configure_notification_channels(project_id)
            
            # 3. Configuration des seuils
            thresholds = self._configure_thresholds(project_id)
            
            # Log de l'événement
            self._log_event("AlertingAgent", "Alertes configurées")
            
            return {
                "alerts": self.alerts,
                "channels": self.channels,
                "rules_count": len(alert_rules),
                "thresholds": thresholds
            }
            
        except Exception as e:
            logger.error(f"❌ Erreur lors de la configuration des alertes: {e}")
            return {"error": str(e)}
    
    def _configure_alert_rules(self, project_id: str) -> List[Dict]:
        """Configure les règles d'alerte"""
        logger.info(f"⚙️ Configuration des règles d'alerte pour {project_id}")
        
        time.sleep(1)
        
        alert_rules = [
            {
                "name": "CPU High",
                "condition": "cpu_usage > 80%",
                "duration": "5m",
                "severity": "warning"
            },
            {
                "name": "API Errors",
                "condition": "http_5xx_errors > 5/min",
                "duration": "2m", 
                "severity": "critical"
            },
            {
                "name": "Downtime",
                "condition": "uptime < 99.9%",
                "duration": "1m",
                "severity": "critical"
            },
            {
                "name": "Memory High",
                "condition": "memory_usage > 85%",
                "duration": "5m",
                "severity": "warning"
            },
            {
                "name": "Response Time",
                "condition": "api_response_time > 2s",
                "duration": "3m",
                "severity": "warning"
            }
        ]
        
        self.alerts = [rule["name"] for rule in alert_rules]
        
        logger.info(f"✅ {len(alert_rules)} règles d'alerte configurées")
        
        return alert_rules
    
    def _configure_notification_channels(self, project_id: str) -> List[Dict]:
        """Configure les canaux de notification"""
        logger.info(f"📢 Configuration des canaux de notification pour {project_id}")
        
        time.sleep(1)
        
        channels = [
            {
                "type": "Slack",
                "webhook": f"https://hooks.slack.com/services/{project_id}/webhook",
                "channel": "#alerts",
                "enabled": True
            },
            {
                "type": "Email",
                "addresses": ["admin@startup.com", "devops@startup.com"],
                "enabled": True
            },
            {
                "type": "Discord",
                "webhook": f"https://discord.com/api/webhooks/{project_id}",
                "channel": "alerts",
                "enabled": False
            }
        ]
        
        self.channels = [channel["type"] for channel in channels if channel["enabled"]]
        
        logger.info(f"✅ Canaux configurés: {', '.join(self.channels)}")
        
        return channels
    
    def _configure_thresholds(self, project_id: str) -> Dict:
        """Configure les seuils d'alerte"""
        logger.info(f"🎯 Configuration des seuils pour {project_id}")
        
        time.sleep(1)
        
        thresholds = {
            "cpu_warning": 70,
            "cpu_critical": 80,
            "memory_warning": 75,
            "memory_critical": 85,
            "error_rate_warning": 2,
            "error_rate_critical": 5,
            "response_time_warning": 1.5,
            "response_time_critical": 2.0,
            "uptime_critical": 99.9
        }
        
        logger.info(f"✅ Seuils configurés pour {len(thresholds)} métriques")
        
        return thresholds
    
    def _log_event(self, agent_name: str, message: str):
        """Log un événement d'alerting"""
        event = {
            "timestamp": time.time(),
            "agent": agent_name,
            "message": message,
            "level": "info"
        }
        logger.info(f"📝 {agent_name}: {message}")


# Fonction utilitaire pour logger les événements
def log_event(agent_name: str, message: str):
    """Fonction utilitaire pour logger les événements d'infrastructure"""
    logger.info(f"📝 {agent_name}: {message}")


if __name__ == "__main__":
    # Test des agents
    project_id = "test-startup"
    
    print("🧪 Test des agents d'infrastructure...")
    
    # Test InfraAgent
    infra = InfraAgent()
    infra_result = infra.run(project_id)
    print(f"InfraAgent: {infra_result}")
    
    # Test MonitoringAgent
    monitoring = MonitoringAgent()
    monitoring_result = monitoring.run(project_id)
    print(f"MonitoringAgent: {monitoring_result}")
    
    # Test AlertingAgent
    alerting = AlertingAgent()
    alerting_result = alerting.run(project_id)
    print(f"AlertingAgent: {alerting_result}")