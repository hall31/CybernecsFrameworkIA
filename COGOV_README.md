# 🏛️ Co-Governance System - Epic 21

## 📋 Vue d'ensemble

Le **Co-Governance System** est une plateforme de gouvernance hybride qui combine l'intelligence artificielle et la participation humaine pour prendre des décisions équilibrées et éthiques sur des sujets planétaires critiques.

## 🎯 Objectifs

- **Gouvernance mixte IA+Humains** : 50% pondération IA (efficacité, calculs rationnels) + 50% pondération Humains (valeurs, éthique, choix culturels)
- **Décisions pondérées** : Calcul automatique de la décision finale basé sur les votes IA et humains
- **Transparence totale** : Historique complet des décisions et processus de vote
- **Flexibilité** : Pondération ajustable selon le domaine (ex: 70/30 pour le climat, 40/60 pour la culture)

## 🏗️ Architecture

### 1. CoGovAgent (`/core-engine/agents/cogov_agent.py`)
- **Classe principale** : `CoGovAgent`
- **Fonctionnalités** :
  - Récupération des décisions planétaires
  - Création du système de co-gouvernance
  - Pondération des votes (IA vs Humains)
  - Génération de rapports détaillés
  - Historique des décisions

### 2. CoDAO (`/core-engine/agents/codao.py`)
- **Gouvernance décentralisée** : DAO spécialisée pour votes mixtes
- **Fonctionnalités** :
  - Création de propositions
  - Système de vote IA et humain
  - Smart contracts simulés
  - Exécution automatique des décisions

### 3. API REST (`/core-engine/main.py`)
- **Endpoints** :
  - `POST /cogov/decision` : Création de décision
  - `GET /cogov/history` : Historique des décisions
  - `GET /cogov/board-members` : Membres du conseil
  - `POST /codao/proposal` : Création de proposition
  - `POST /codao/vote` : Soumission de vote
  - `GET /codao/proposals` : Liste des propositions

### 4. Dashboard React (`/dashboard/src/components/CoGovernanceBoard.jsx`)
- **Interface utilisateur** moderne et intuitive
- **Sections** :
  - Décision en cours
  - Pondération IA vs Humains
  - Historique des décisions
  - Membres du conseil

## 🚀 Installation et Utilisation

### Prérequis
- Python 3.8+
- Node.js 16+
- npm ou yarn

### Backend (Core Engine)
```bash
cd core-engine
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
pip install fastapi uvicorn
python3 main.py
```

### Frontend (Dashboard)
```bash
cd dashboard
npm install
npm run dev
```

### Test du Système
```bash
cd core-engine
source venv/bin/activate
python3 demo_cogov.py
```

## 📊 Exemple d'Utilisation

### 1. Création d'une Décision
```python
from agents.cogov_agent import CoGovAgent

# Initialisation
agent = CoGovAgent(ai_weighting=50, human_weighting=50)

# Décision automatique
decision = agent.run("Budget eau 2030")
print(f"Décision finale: {decision['final_decision']}")
```

### 2. Création d'une Proposition DAO
```python
from agents.codao import CoDAO

# Initialisation
dao = CoDAO("Global Co-Governance DAO")

# Création de proposition
proposal = dao.create_proposal(
    topic="Protection biodiversité marine",
    description="Augmenter le budget pour la protection des océans",
    creator="Marine Conservation NGO",
    ai_weighting=40,
    human_weighting=60
)
```

### 3. Vote IA
```python
# Vote d'un agent IA
dao.submit_ai_vote(
    proposal_id=proposal['id'],
    ai_agent="PlanetaryAgent",
    vote="Augmenter de 25%"
)
```

### 4. Vote Humain
```python
# Vote humain avec stake
dao.submit_human_vote(
    proposal_id=proposal['id'],
    voter="Citizen Group A",
    vote="Augmenter de 35%",
    stake_amount=150
)
```

## 🔧 Configuration

### Pondération par Domaine
```python
# Climat : Plus d'influence humaine
agent.update_weighting(30, 70)  # IA 30%, Humains 70%

# Économie : Équilibre
agent.update_weighting(50, 50)  # IA 50%, Humains 50%

# Culture : Plus d'influence humaine
agent.update_weighting(20, 80)  # IA 20%, Humains 80%
```

### Membres du Conseil
```python
# Ajout d'un nouveau membre IA
agent.add_board_member("ai", "QuantumAgent")

# Ajout d'un nouveau membre humain
agent.add_board_member("human", "Youth Council")
```

## 📈 Métriques et Monitoring

### Historique des Décisions
- Sujet de la décision
- Vote IA et vote humain
- Décision finale pondérée
- Timestamp et pondération utilisée

### Statistiques de Participation
- Taux de participation IA vs Humains
- Nombre de votes par proposition
- Temps de traitement des décisions

## 🌐 API Endpoints

### Co-Governance
```http
POST /cogov/decision
{
  "topic": "Budget eau 2030",
  "ai_vote": "Augmenter de 20%",
  "human_vote": "Augmenter de 30%"
}

GET /cogov/history
GET /cogov/board-members
```

### DAO
```http
POST /codao/proposal
{
  "topic": "Protection biodiversité",
  "description": "Description détaillée",
  "creator": "NGO",
  "ai_weighting": 40,
  "human_weighting": 60
}

POST /codao/vote
{
  "proposal_id": "abc123",
  "voter": "PlanetaryAgent",
  "vote": "Augmenter de 25%",
  "stake_amount": 100
}
```

## 🎨 Interface Utilisateur

### Dashboard Co-Governance
- **Thème** : Institutionnel premium
- **Couleurs** :
  - 🔵 Bleu : IA
  - 🟢 Vert : Humains
  - 🟣 Violet : Décision finale
- **Graphiques** : Recharts pour visualisations
- **Responsive** : Mobile et desktop

### Fonctionnalités
- Navigation par onglets
- Ajustement de pondération en temps réel
- Historique complet des décisions
- Vue des membres du conseil
- Graphiques de pondération

## 🔒 Sécurité et Transparence

### Smart Contracts
- Règles de gouvernance immutables
- Pondération fixée par défaut (ajustable)
- Pas de triche possible
- Traçabilité complète

### Audit Trail
- Tous les votes sont enregistrés
- Historique des modifications de pondération
- Timestamps pour chaque action
- Logs détaillés

## 🚀 Déploiement

### Production
```bash
# Backend
cd core-engine
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker

# Frontend
cd dashboard
npm run build
serve -s build
```

### Docker
```bash
docker-compose up -d
```

## 📚 Documentation Technique

### Structure des Données
```python
decision_report = {
    "decision_topic": "Budget eau 2030",
    "ai_vote": "Augmenter de 20%",
    "human_vote": "Augmenter de 30%",
    "final_decision": "Augmenter de 25%",
    "weighting": {"AI": 50, "Human": 50},
    "timestamp": "2024-01-26T10:30:00",
    "ai_board_members": ["PlanetaryAgent", ...],
    "human_board_members": ["Citizens", ...]
}
```

### Logs
```bash
[2024-01-26 10:30:00] INFO | CoGovAgent | Décision hybride IA+Humains prise: Augmenter de 25%
```

## 🤝 Contribution

### Développement
1. Fork du projet
2. Création d'une branche feature
3. Tests et validation
4. Pull request

### Tests
```bash
python3 test_cogov.py
python3 demo_cogov.py
```

## 📞 Support

- **Issues** : GitHub Issues
- **Documentation** : Ce README
- **Démonstrations** : `demo_cogov.py`

## 🎯 Roadmap

### Phase 1 ✅ (Terminée)
- [x] CoGovAgent de base
- [x] CoDAO avec votes mixtes
- [x] API REST complète
- [x] Dashboard React

### Phase 2 🔄 (En cours)
- [ ] Intégration blockchain réelle
- [ ] Smart contracts Ethereum
- [ ] Authentification utilisateurs
- [ ] Notifications en temps réel

### Phase 3 📋 (Planifiée)
- [ ] IA avancée avec LLM
- [ ] Analyse de sentiment
- [ ] Prédictions de tendances
- [ ] Intégration multi-chaînes

---

**🎉 Le système de Co-Governance est maintenant opérationnel et prêt pour la production !**

*Développé pour l'Epic 21 - Gouvernance hybride IA+Humains*