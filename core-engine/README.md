# Epic 9 - Infrastructure DevOps avec Auto-scaling et Monitoring

## 🎯 Vue d'ensemble

L'Epic 9 implémente une infrastructure DevOps complète pour le déploiement automatique de startups avec :
- **Auto-scaling Kubernetes** (2-20 pods)
- **Monitoring Prometheus + Grafana**
- **Système d'alertes** vers Slack/Email
- **LoadBalancer Nginx Ingress**
- **Certificats SSL automatiques**

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Infrastructure DevOps                     │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │ InfraAgent  │  │Monitoring   │  │Alerting     │        │
│  │             │  │Agent        │  │Agent        │        │
│  │ • K8s       │  │ • Prometheus│  │ • Alertes   │        │
│  │ • HPA       │  │ • Grafana   │  │ • Slack     │        │
│  │ • SSL       │  │ • Dashboards│  │ • Email     │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
├─────────────────────────────────────────────────────────────┤
│                    Orchestrateur                            │
│              InfrastructureOrchestrator                     │
├─────────────────────────────────────────────────────────────┤
│                    Dashboard React                           │
│              InfrastructureDashboard                        │
└─────────────────────────────────────────────────────────────┘
```

## 🚀 Utilisation rapide

### 1. Test des agents

```bash
cd core-engine/agents
python3 infra_agent.py
```

### 2. Test de l'orchestrateur

```bash
cd core-engine/orchestrator
python3 main.py
```

### 3. Déploiement complet

```bash
cd core-engine
chmod +x deploy-infrastructure.sh
./deploy-infrastructure.sh startup123
```

## 📁 Structure des fichiers

```
core-engine/
├── agents/
│   └── infra_agent.py          # Agents DevOps (Infra, Monitoring, Alerting)
├── orchestrator/
│   └── main.py                 # Orchestrateur principal
├── dashboard/
│   └── InfrastructureDashboard.jsx  # Dashboard React
├── k8s-manifests/
│   ├── hpa-config.yaml         # Configuration HPA + Ingress
│   ├── monitoring-stack.yaml   # Prometheus + Grafana
│   └── alerting-rules.yaml     # Règles d'alerte
├── deploy-infrastructure.sh     # Script de déploiement
└── README.md                   # Ce fichier
```

## 🔧 Composants détaillés

### InfraAgent

**Responsabilités :**
- Déploiement du cluster Kubernetes (GKE/EKS)
- Configuration de l'auto-scaling horizontal (HPA)
- Configuration du LoadBalancer Nginx Ingress
- Configuration des certificats SSL via cert-manager

**Configuration HPA :**
- Min pods : 2
- Max pods : 20
- Seuil CPU : 70%
- Seuil mémoire : 80%

**Retour :**
```json
{
  "cluster": "gke-startup123-1234567890",
  "url": "https://startup123.app",
  "scaling": "2-20 pods",
  "ssl": "active",
  "loadbalancer": "Nginx Ingress"
}
```

### MonitoringAgent

**Responsabilités :**
- Déploiement de Prometheus dans Kubernetes
- Déploiement de Grafana avec dashboards pré-configurés
- Configuration des métriques système et applicatives

**Dashboards inclus :**
- **Performance** : CPU, RAM, Network I/O, Disk I/O
- **Errors** : HTTP 4xx/5xx, Application Errors, Database Errors
- **Uptime** : Service Status, Response Time, Availability

**Retour :**
```json
{
  "grafana_url": "https://monitoring.startup123.app",
  "dashboards": ["performance", "errors", "uptime"],
  "prometheus_url": "https://prometheus.startup123.app",
  "metrics_count": 15
}
```

### AlertingAgent

**Responsabilités :**
- Configuration des règles d'alerte Prometheus
- Configuration des canaux de notification (Slack, Email, Discord)
- Définition des seuils d'alerte

**Règles d'alerte :**
- **CPU High** : > 80% pendant 5min
- **API Errors** : > 5/min pendant 2min
- **Downtime** : < 99.9% pendant 1min
- **Memory High** : > 85% pendant 5min
- **Response Time** : > 2s pendant 3min

**Retour :**
```json
{
  "alerts": ["CPU High", "API Errors", "Downtime", "Memory High", "Response Time"],
  "channels": ["Slack", "Email"],
  "rules_count": 5
}
```

## 🌐 API REST

### POST /create-startup

**Requête :**
```json
{
  "idea": "SaaS marketplace pour freelances"
}
```

**Réponse :**
```json
{
  "project_id": "startup-1234567890",
  "idea": "SaaS marketplace pour freelances",
  "created_at": 1234567890,
  "status": "created",
  "infra": { /* InfraAgent result */ },
  "monitoring": { /* MonitoringAgent result */ },
  "alerting": { /* AlertingAgent result */ },
  "summary": {
    "cluster": "gke-startup123-1234567890",
    "url": "https://startup123.app",
    "scaling": "2-20 pods",
    "grafana_url": "https://monitoring.startup123.app",
    "alerts": ["CPU High", "API Errors", "Downtime"],
    "channels": ["Slack", "Email"]
  }
}
```

## 🎨 Dashboard React

Le composant `InfrastructureDashboard` affiche 4 cartes principales :

1. **Cluster Kubernetes** (Bleu)
   - Nom du cluster
   - URL de l'application
   - Statut SSL

2. **Auto-scaling** (Vert)
   - Configuration des pods
   - Seuils CPU/Mémoire
   - Barre de progression des pods actifs

3. **Monitoring** (Orange)
   - URL Grafana
   - Dashboards disponibles
   - Nombre de métriques

4. **Alertes** (Rouge)
   - Règles d'alerte actives
   - Canaux de notification
   - Statut du système

## 🚀 Déploiement

### Prérequis

- `kubectl` configuré et connecté à un cluster
- `helm` (installé automatiquement si manquant)
- Cluster Kubernetes avec accès LoadBalancer

### Étapes de déploiement

1. **Vérification des prérequis**
2. **Installation de Nginx Ingress**
3. **Installation de cert-manager**
4. **Configuration Let's Encrypt**
5. **Déploiement de l'application de test**
6. **Configuration de l'auto-scaling**
7. **Déploiement du monitoring**
8. **Configuration des alertes**
9. **Configuration de l'Ingress**

### Commandes utiles

```bash
# Vérifier l'état du déploiement
kubectl get pods -A
kubectl get services -A
kubectl get ingress -A

# Accéder aux services de monitoring
kubectl port-forward -n monitoring svc/grafana 3000:3000
kubectl port-forward -n monitoring svc/prometheus 9090:9090
kubectl port-forward -n monitoring svc/alertmanager 9093:9093

# Vérifier l'auto-scaling
kubectl get hpa -A
kubectl describe hpa startup-app-hpa -n default

# Logs des services
kubectl logs -n monitoring deployment/prometheus
kubectl logs -n monitoring deployment/grafana
kubectl logs -n monitoring deployment/alertmanager
```

## 🔍 Monitoring et Alertes

### Métriques collectées

- **Système** : CPU, Mémoire, Disque, Réseau
- **Kubernetes** : Pods, Services, Nodes
- **Application** : Requêtes HTTP, Latence, Erreurs
- **Infrastructure** : Uptime, Disponibilité

### Seuils d'alerte

- **Warning** : CPU > 70%, Mémoire > 75%, Latence > 1.5s
- **Critical** : CPU > 80%, Mémoire > 85%, Latence > 2s, Erreurs > 5/min

### Canaux de notification

- **Slack** : #alerts (général), #critical-alerts (critique)
- **Email** : admin@startup.com, devops@startup.com
- **Discord** : #alerts (optionnel)

## 🧪 Tests

### Test unitaire des agents

```bash
cd core-engine/agents
python3 -c "
from infra_agent import InfraAgent, MonitoringAgent, AlertingAgent

# Test InfraAgent
infra = InfraAgent()
result = infra.run('test-startup')
print('InfraAgent:', result)

# Test MonitoringAgent
monitoring = MonitoringAgent()
result = monitoring.run('test-startup')
print('MonitoringAgent:', result)

# Test AlertingAgent
alerting = AlertingAgent()
result = alerting.run('test-startup')
print('AlertingAgent:', result)
"
```

### Test de l'orchestrateur

```bash
cd core-engine/orchestrator
python3 -c "
from main import create_startup_with_infrastructure
result = create_startup_with_infrastructure('SaaS marketplace')
print('Résultat:', result)
"
```

## 🔧 Configuration avancée

### Personnalisation des seuils

Modifiez les valeurs dans `infra_agent.py` :

```python
self.scaling_config = {
    "min_pods": 3,        # Au lieu de 2
    "max_pods": 30,       # Au lieu de 20
    "cpu_threshold": 60   # Au lieu de 70
}
```

### Ajout de nouvelles métriques

Ajoutez des métriques dans `monitoring-stack.yaml` :

```yaml
- job_name: 'custom-metrics'
  static_configs:
    - targets: ['localhost:9090']
```

### Configuration des alertes personnalisées

Modifiez `alerting-rules.yaml` pour ajouter vos propres règles.

## 🚨 Dépannage

### Problèmes courants

1. **LoadBalancer IP non assignée**
   ```bash
   kubectl get service -n ingress-nginx
   # Attendre que l'IP soit assignée
   ```

2. **Certificats SSL non générés**
   ```bash
   kubectl get certificat -A
   kubectl describe certificat -n default
   ```

3. **Prometheus ne collecte pas de métriques**
   ```bash
   kubectl logs -n monitoring deployment/prometheus
   # Vérifier la configuration
   ```

4. **Alertes non envoyées**
   ```bash
   kubectl logs -n monitoring deployment/alertmanager
   # Vérifier la configuration Slack/Email
   ```

### Logs utiles

```bash
# Logs de l'ingress
kubectl logs -n ingress-nginx deployment/nginx-ingress-controller

# Logs de cert-manager
kubectl logs -n cert-manager deployment/cert-manager

# Événements Kubernetes
kubectl get events --sort-by='.lastTimestamp'
```

## 📚 Ressources supplémentaires

- [Kubernetes HPA Documentation](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)
- [Prometheus Configuration](https://prometheus.io/docs/prometheus/latest/configuration/)
- [Grafana Dashboards](https://grafana.com/docs/grafana/latest/dashboards/)
- [AlertManager Configuration](https://prometheus.io/docs/alerting/latest/configuration/)

## 🤝 Contribution

Pour contribuer à l'Epic 9 :

1. Créez une branche pour votre fonctionnalité
2. Ajoutez des tests pour les nouvelles fonctionnalités
3. Mettez à jour la documentation
4. Soumettez une pull request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.