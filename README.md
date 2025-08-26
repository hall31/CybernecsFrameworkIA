# 🏛️ Cybernecs Framework IA - Système de Co-Governance

## 🌟 Vue d'ensemble

Le **Cybernecs Framework IA** est un système de gouvernance hybride IA+Humains qui combine l'efficacité de l'intelligence artificielle avec la sagesse et les valeurs humaines pour la prise de décisions stratégiques.

## 🎯 Objectifs

- **Gouvernance hybride** : Combiner IA et humains pour des décisions optimales
- **Transparence totale** : Tous les votes et décisions sont tracés
- **Pondération flexible** : Ajuster l'influence IA vs Humains selon le domaine
- **DAO intégré** : Gestion décentralisée des propositions et votes
- **Interface moderne** : Dashboard React avec visualisations avancées

## 🏗️ Architecture

### 1. **CoGovAgent** (`/core-engine/agents/cogov_agent.py`)
- Agent principal de co-gouvernance
- Gestion des votes IA et humains
- Calcul des décisions pondérées
- Historique complet des décisions
- Membres du conseil IA et humains

### 2. **CoDAO** (`/core-engine/agents/codao.py`)
- Organisation autonome décentralisée
- Gestion des propositions et votes
- Smart contracts simulés
- Exécution automatique des décisions
- Système de pondération configurable

### 3. **API REST** (`/core-engine/main.py`)
- Endpoints complets pour co-gouvernance
- Gestion des propositions DAO
- Système de vote hybride
- Historique et métriques

### 4. **Dashboard React** (`/dashboard/src/components/CoGovernanceBoard.jsx`)
- Interface moderne et intuitive
- Visualisation des votes IA vs Humains
- Ajustement de pondération en temps réel
- Historique et membres du conseil

## 🚀 Installation et Démarrage

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

pip install flask flask-cors openai
python3 main.py
```

### Frontend (Dashboard)
```bash
cd dashboard
npm install
npm run dev
```

## 📊 Utilisation

### 1. **Créer une Décision**
```bash
curl -X POST "http://localhost:8000/cogov/decision" \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "Budget eau 2030",
    "ai_vote": "Augmenter de 20%",
    "human_vote": "Augmenter de 30%"
  }'
```

### 2. **Créer une Proposition DAO**
```bash
curl -X POST "http://localhost:8000/codao/proposal" \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "Nouvelle politique environnementale",
    "description": "Mise en place de mesures écologiques",
    "creator": "Équipe Green",
    "ai_weighting": 60.0,
    "human_weighting": 40.0
  }'
```

### 3. **Voter sur une Proposition**
```bash
curl -X POST "http://localhost:8000/codao/vote" \
  -H "Content-Type: application/json" \
  -d '{
    "proposal_id": "abc123",
    "voter": "Jean Dupont",
    "vote": "Approuver",
    "stake_amount": 100.0
  }'
```

## 🎨 Interface Utilisateur

### **Co-Governance Board**
- **Décision en cours** : Affichage du sujet, votes IA (bleu), votes humains (vert), décision finale (violet)
- **Pondération** : Slider et graphique pour ajuster l'influence IA vs Humains
- **Historique** : Liste complète des décisions passées
- **Membres du conseil** : Vue des participants IA et humains

### **Navigation**
- Onglets pour basculer entre Startup Factory et Co-Governance Board
- Interface responsive et moderne
- Thème institutionnel premium

## 🔧 Configuration

### Pondération par Défaut
```python
# Dans CoGovAgent
ai_weighting = 50.0    # 50% IA
human_weighting = 50.0 # 50% Humains
```

### Pondération par Domaine
```python
# Exemples de pondération spécialisée
climate_decisions = {"AI": 70.0, "Human": 30.0}  # IA majoritaire pour le climat
cultural_decisions = {"AI": 40.0, "Human": 60.0} # Humains majoritaires pour la culture
```

## 📈 Métriques et Monitoring

### **Statistiques du Système**
- Nombre total de décisions
- Taux de participation
- Distribution des votes
- Performance des agents IA

### **API de Statut**
```bash
curl "http://localhost:8000/status"
```

## 🧪 Tests

### **Test Automatique**
```bash
cd core-engine
python3 test_simple.py
```

### **Tests Manuels**
- Test des endpoints API
- Validation du dashboard React
- Vérification des calculs de pondération

## 🔒 Sécurité

- Validation des données d'entrée
- Gestion des erreurs robuste
- Logs complets de toutes les activités
- Isolation des composants

## 🚀 Déploiement

### **Production**
- Serveur WSGI (Gunicorn)
- Base de données PostgreSQL
- Load balancer
- Monitoring et alertes

### **Docker**
```bash
docker-compose up -d
```

## 📚 Documentation Technique

### **Structure des Données**
```python
# Décision de co-gouvernance
{
    "decision_topic": "Budget eau 2030",
    "ai_vote": "Augmenter de 20%",
    "human_vote": "Augmenter de 30%",
    "final_decision": "Augmenter de 25.0%",
    "weighting": {"AI": 50.0, "Human": 50.0},
    "timestamp": "2025-08-26T19:18:05",
    "ai_board_members": [...],
    "human_board_members": [...]
}
```

### **Endpoints API**
- `POST /cogov/decision` - Créer une décision
- `GET /cogov/history` - Historique des décisions
- `GET /cogov/board-members` - Membres du conseil
- `POST /codao/proposal` - Créer une proposition
- `POST /codao/vote` - Soumettre un vote
- `GET /codao/proposals` - Lister les propositions
- `POST /codao/execute/{id}` - Exécuter une proposition

## 🌟 Fonctionnalités Avancées

### **Intelligence Artificielle**
- Analyse contextuelle des sujets
- Génération automatique de votes IA
- Optimisation des pondérations
- Apprentissage des préférences

### **Gouvernance Humaine**
- Interface de vote intuitive
- Système de stake et réputation
- Délégation de votes
- Participation démocratique

### **DAO Features**
- Propositions avec quorum
- Périodes de vote configurables
- Exécution automatique
- Gestion des conflits

## 🔮 Roadmap

### **Phase 1** ✅ (Terminée)
- [x] Système de co-gouvernance de base
- [x] API REST complète
- [x] Dashboard React
- [x] Tests et validation

### **Phase 2** 🚧 (En cours)
- [ ] Intégration blockchain
- [ ] Smart contracts réels
- [ ] Système de réputation avancé
- [ ] Analytics et reporting

### **Phase 3** 📋 (Planifiée)
- [ ] IA prédictive pour les décisions
- [ ] Intégration multi-organisations
- [ ] Interface mobile
- [ ] Internationalisation

## 🤝 Contribution

### **Comment Contribuer**
1. Fork le projet
2. Créer une branche feature
3. Implémenter les changements
4. Ajouter des tests
5. Soumettre une pull request

### **Standards de Code**
- PEP 8 pour Python
- ESLint pour JavaScript/React
- Tests unitaires obligatoires
- Documentation des APIs

## 📞 Support

### **Communauté**
- Issues GitHub pour les bugs
- Discussions pour les features
- Wiki pour la documentation
- Slack pour le support en temps réel

### **Contact**
- **Email** : support@cybernecs.ai
- **GitHub** : [CybernecsFrameworkIA](https://github.com/hall31/CybernecsFrameworkIA)
- **Documentation** : [docs.cybernecs.ai](https://docs.cybernecs.ai)

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## 🎯 Résumé

Le **Cybernecs Framework IA** représente l'avenir de la gouvernance hybride, combinant la puissance de l'IA avec la sagesse humaine pour créer un système de prise de décision plus intelligent, transparent et équitable.

**🚀 Prêt à révolutionner la gouvernance ? Commencez dès maintenant !**

