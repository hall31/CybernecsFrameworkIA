# 🚀 Epic 8 - Agents Connectés aux Services Réels

## Vue d'ensemble

L'Epic 8 implémente 3 agents connectés à des services réels pour exécuter automatiquement la stratégie de création de startups SaaS :

1. **GitOpsAgent** - Déploiement automatique via GitHub
2. **PaymentsAgent** - Monétisation via Stripe
3. **AdsAgent** - Acquisition clients via LinkedIn Ads/Google Ads

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   GitOpsAgent   │    │ PaymentsAgent   │    │    AdsAgent     │
│                 │    │                 │    │                 │
│ • GitHub API    │    │ • Stripe API    │    │ • LinkedIn Ads  │
│ • CI/CD Setup   │    │ • Plans Pricing │    │ • Google Ads    │
│ • Code Push     │    │ • Checkout      │    │ • Campaigns     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                    ┌─────────────────┐
                    │   Orchestrateur  │
                    │   (main.py)      │
                    │                 │
                    │ POST /create-    │
                    │ startup          │
                    └─────────────────┘
                                 │
                    ┌─────────────────┐
                    │   Dashboard     │
                    │   React         │
                    │                 │
                    │ • Déploiement   │
                    │ • Monétisation  │
                    │ • Acquisition   │
                    └─────────────────┘
```

## 📦 Installation

### 1. Prérequis

```bash
# Python 3.8+
python --version

# Node.js 18+ (pour le frontend)
node --version
```

### 2. Installation des dépendances

```bash
# Dépendances Python
pip install -r requirements.txt

# Dépendances frontend (optionnel)
cd frontend
npm install
```

### 3. Configuration des variables d'environnement

```bash
# Copier le template
cp .env.example .env

# Configurer vos clés API
GITHUB_TOKEN=ghp_your_github_token
GITHUB_USERNAME=your_github_username
STRIPE_SECRET_KEY=sk_test_your_stripe_key
LINKEDIN_ACCESS_TOKEN=your_linkedin_token
# ... autres variables
```

## 🚀 Utilisation

### 1. Démarrer l'API

```bash
python main.py
```

L'API sera disponible sur `http://localhost:8000`

### 2. Créer une startup

```bash
curl -X POST "http://localhost:8000/create-startup" \
  -H "Content-Type: application/json" \
  -d '{
    "idea": "SaaS marketplace pour freelances",
    "description": "Plateforme de mise en relation"
  }'
```

### 3. Réponse attendue

```json
{
  "project_id": "a1b2c3d4",
  "idea": "SaaS marketplace pour freelances",
  "status": "created",
  "gitops": {
    "repo_url": "https://github.com/user/startup-a1b2c3d4",
    "status": "pushed",
    "repo_name": "startup-a1b2c3d4"
  },
  "payments": {
    "stripe_plans": [...],
    "checkout_url": "https://checkout.stripe.com/...",
    "status": "configured"
  },
  "ads": {
    "ads_platform": "LinkedIn",
    "campaign_id": "camp_a1b2c3d4",
    "status": "active"
  },
  "message": "Startup créée avec succès !"
}
```

## 🔧 Agents

### GitOpsAgent

**Responsabilité** : Déploiement automatique et CI/CD

**Actions** :
- Crée un repository GitHub
- Pousse le code généré
- Configure GitHub Actions
- Met en place le déploiement automatique

**Configuration requise** :
```bash
GITHUB_TOKEN=ghp_...
GITHUB_USERNAME=your_username
```

**Utilisation** :
```python
from agents.gitops_agent import GitOpsAgent

agent = GitOpsAgent()
result = agent.run("project-123")
print(f"Repo créé: {result['repo_url']}")
```

### PaymentsAgent

**Responsabilité** : Monétisation et plans de pricing

**Actions** :
- Crée des plans Stripe adaptés à l'idée
- Configure les produits et prix
- Génère une page de checkout
- Gère les abonnements

**Configuration requise** :
```bash
STRIPE_SECRET_KEY=sk_test_...
```

**Utilisation** :
```python
from agents.payments_agent import PaymentsAgent

agent = PaymentsAgent()
result = agent.run("SaaS marketplace")
print(f"Plans créés: {len(result['stripe_plans'])}")
```

### AdsAgent

**Responsabilité** : Acquisition clients et publicité

**Actions** :
- Analyse l'idée pour définir la stratégie
- Choisit la plateforme appropriée (LinkedIn/Google)
- Crée des campagnes publicitaires
- Configure le targeting et le budget

**Configuration requise** :
```bash
LINKEDIN_ACCESS_TOKEN=...
GOOGLE_ADS_DEVELOPER_TOKEN=...
```

**Utilisation** :
```python
from agents.ads_agent import AdsAgent

agent = AdsAgent()
growth_data = {"channel": "paid_ads", "budget": "100€/jour"}
result = agent.run("Plateforme IA", growth_data)
print(f"Campagne {result['ads_platform']} créée")
```

## 🎨 Dashboard React

### Composant Execution

Le composant `Execution.tsx` affiche 3 cartes colorées :

1. **Déploiement (Bleu)** : Status GitHub, repo URL, bouton "Ouvrir sur GitHub"
2. **Monétisation (Vert)** : Plans Stripe, bouton "Ouvrir checkout"
3. **Acquisition (Violet)** : Campagne Ads, bouton "Voir campagne"

### Utilisation

```tsx
import Execution from './components/Execution'

function Dashboard() {
  return (
    <div>
      <h1>Mon ShipFast</h1>
      <Execution projectId="a1b2c3d4" idea="SaaS marketplace" />
    </div>
  )
}
```

## 🧪 Tests

### Lancer les tests

```bash
python test_agents.py
```

### Tests disponibles

- ✅ GitOpsAgent
- ✅ PaymentsAgent  
- ✅ AdsAgent
- ✅ API Integration

## 📊 Monitoring

### Logs des agents

Chaque agent log ses actions avec timestamp :

```json
{
  "timestamp": "2024-01-15T10:30:00Z",
  "agent": "GitOpsAgent",
  "action": "Code poussé sur GitHub",
  "details": {
    "repo_url": "https://github.com/user/startup-123",
    "files_count": 15
  }
}
```

### Endpoints de monitoring

```bash
# Statut de l'API
GET /health

# Statut des agents
GET /agents/status

# Statut d'une startup
GET /startup/{project_id}
```

## 🚨 Dépannage

### Erreurs courantes

1. **GitHub API rate limit**
   - Vérifiez votre token GitHub
   - Attendez la réinitialisation du quota

2. **Stripe API key invalide**
   - Utilisez des clés de test pour le développement
   - Vérifiez la variable `STRIPE_SECRET_KEY`

3. **LinkedIn Ads non configuré**
   - L'agent fonctionne en mode simulation
   - Configurez `LINKEDIN_ACCESS_TOKEN` pour la production

### Logs de debug

```bash
# Activer les logs détaillés
export PYTHONPATH=.
python -c "
from agents.gitops_agent import GitOpsAgent
import logging
logging.basicConfig(level=logging.DEBUG)
agent = GitOpsAgent()
"
```

## 🔮 Évolutions futures

- [ ] Intégration avec d'autres plateformes (Facebook Ads, Twitter Ads)
- [ ] Support multi-régions pour Stripe
- [ ] Analytics avancés des campagnes
- [ ] A/B testing automatique
- [ ] Optimisation des budgets en temps réel

## 📚 Ressources

- [GitHub API Documentation](https://docs.github.com/en/rest)
- [Stripe API Reference](https://stripe.com/docs/api)
- [LinkedIn Marketing API](https://developer.linkedin.com/docs/marketing-apis)
- [Google Ads API](https://developers.google.com/google-ads/api/docs/start)

---

**Mon ShipFast Epic 8** - Créez votre startup SaaS en quelques clics avec exécution automatique ! 🚀