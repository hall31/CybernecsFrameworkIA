# 🏛️ StartupDAO - Agent DAO Blockchain

Plateforme de tokenisation et gouvernance décentralisée pour startups, intégrant des agents IA spécialisés dans la création de DAOs, la tokenisation et la gestion de trésorerie.

## 🚀 Architecture

### Core Engine (`/core-engine`)

#### Agents DAO (`/agents/dao_agent.py`)

**TokenisationAgent** 🪙
- Déploie des smart contracts ERC20/ERC1400 pour les startups
- Gère la distribution des tokens (20% fondateur, 10% équipe, 70% investisseurs)
- Calcule automatiquement le prix par token basé sur la valorisation

**GovernanceAgent** 🏛️
- Crée des DAOs via smart contracts Governor
- Implémente le système de vote "1 token = 1 vote"
- Définit les règles de gouvernance et quorum

**TreasuryAgent** 💰
- Gère la trésorerie DAO
- Contrôle l'allocation des fonds via votes
- Distribue les dividendes selon un calendrier défini

**DAOOrchestrator** 🎯
- Orchestre la création complète d'une DAO
- Coordonne les trois agents en séquence
- Retourne un résultat unifié

#### Smart Contracts (`/contracts`)

**StartupToken.sol**
- Contrat ERC20 personnalisé pour les startups
- Gestion des allocations et valorisations
- Fonctions de pause d'urgence et récupération

### Frontend React (`/frontend`)

**Page DAO & Tokenisation** (`/src/pages/DAOAndTokenisation.jsx`)
- Dashboard moderne avec thème crypto/fintech
- Visualisations Recharts (distribution tokens, allocation fonds)
- Navigation intuitive vers les contrats blockchain

**Navigation** (`/src/components/Navigation.jsx`)
- Menu principal avec lien vers la page DAO
- Design responsive et thème cohérent

## 🛠️ Installation

### Prérequis
- Python 3.8+
- Node.js 16+
- Solidity 0.8.19+

### Backend Python
```bash
cd core-engine
pip install -r requirements.txt
```

### Frontend React
```bash
cd frontend
npm install
npm run dev
```

### Variables d'environnement
```bash
cp .env.example .env
# Configurer ETHEREUM_RPC_URL et PRIVATE_KEY
```

## 🧪 Tests

### Test de l'agent DAO
```bash
python test_dao_agent.py
```

### Test de l'orchestrateur
```bash
cd core-engine
python main.py
```

## 📊 Workflow Complet

1. **POST /create-startup** avec une idée
2. **InvestorAgent** → Valorisation de la startup
3. **TokenisationAgent** → Token ERC20 déployé
4. **GovernanceAgent** → DAO créée avec contrats Governor
5. **TreasuryAgent** → Trésorerie déployée et configurée
6. **Dashboard** → Visualisation complète de la DAO

## 🔧 Configuration

### Réseaux supportés
- Ethereum Mainnet
- Sepolia Testnet
- Polygon
- Local (Ganache/Hardhat)

### Paramètres DAO
- Quorum: 10% des tokens
- Période de vote: 7 jours
- Limite retrait trésorerie: 5% par mois
- Distribution dividendes: Trimestrielle

## 📱 Interface Utilisateur

### Design System
- **Thème**: Crypto/Fintech avec dégradés bleus/violets
- **Icônes**: FontAwesome avec émojis thématiques
- **Graphiques**: Recharts pour visualisations
- **Responsive**: Mobile-first avec navigation adaptative

### Composants Principaux
- **Section Token**: Symbole, valorisation, distribution
- **Section DAO**: Adresse, règles, pouvoir de vote
- **Section Trésorerie**: Fonds, allocation, règles
- **Statistiques**: Métriques globales de la plateforme

## 🔐 Sécurité

### Smart Contracts
- OpenZeppelin pour les standards ERC20
- Pausable pour arrêt d'urgence
- ReentrancyGuard contre les attaques
- Ownable pour contrôle d'accès

### Agents Python
- Gestion d'erreurs robuste
- Logging centralisé
- Validation des paramètres
- Isolation des composants

## 🚀 Déploiement

### Production
```bash
# Compiler les smart contracts
npx hardhat compile

# Déployer sur le réseau cible
npx hardhat deploy --network mainnet

# Lancer l'API
cd core-engine
python main.py

# Build du frontend
cd frontend
npm run build
```

### Développement
```bash
# Lancer Hardhat local
npx hardhat node

# Déployer en local
npx hardhat deploy --network localhost

# Lancer les tests
npm run test
```

## 📈 Roadmap

### Phase 1 (Actuelle)
- ✅ Agents DAO de base
- ✅ Smart contracts ERC20
- ✅ Dashboard React
- ✅ Tests unitaires

### Phase 2
- 🔄 Intégration Web3.js
- 🔄 Connecteurs wallet (MetaMask, WalletConnect)
- 🔄 Système de votes en temps réel
- 🔄 Notifications push

### Phase 3
- 📋 Marketplace de tokens
- 📋 Système de staking
- 📋 Intégration DeFi
- 📋 Analytics avancés
=======
# 🚀 Epic4 - Générateur de Startups IA

Un système complet de génération automatique de startups utilisant des agents IA spécialisés pour créer des entreprises complètes en quelques minutes.

## 🎯 Fonctionnalités

### 🤖 Agents IA Spécialisés

- **CEO Agent** : Stratégie business, roadmap et modèle économique
- **CTO Agent** : Architecture technique et stack technologique  
- **Dev Agent** : Développement MVP backend et frontend
- **Marketing Agent** : Contenu marketing, logo et landing page

### 🎨 Marketing Agent (Nouveau !)

Le **MarketingAgent** génère automatiquement :

- **Contenu marketing** : Headlines, taglines, features, pricing
- **Logo SVG** : Design minimal et moderne en SVG
- **Landing page React** : Page complète avec Tailwind CSS
  - Hero section avec logo et CTA
  - Features section avec cartes
  - Pricing section avec 3 plans
  - Footer avec contact

## 🏗️ Architecture

```
core-engine/
├── agents/
│   ├── marketing_agent.py      # Agent marketing principal
│   └── marketing_agent_simple.py  # Version simplifiée
├── logger.py                   # Système de logging
└── __init__.py

generated/
├── branding/
│   └── logo.svg               # Logo généré
├── landing-page/              # Landing page React
│   ├── LandingPage.jsx        # Composant principal
│   ├── src/main.jsx           # Point d'entrée
│   ├── index.css              # Styles Tailwind
│   ├── package.json           # Dépendances
│   └── tailwind.config.js     # Configuration Tailwind
└── startup_result.json        # Résultat complet

main_simple.py                  # Orchestrateur principal
```

## 🚀 Utilisation

### 1. Test du Marketing Agent

```bash
python3 test_simple.py
```

### 2. Génération complète d'une startup

```bash
python3 main_simple.py
```

### 3. Utilisation programmatique

```python
from main_simple import create_startup

# Créer une startup complète
result = create_startup("SaaS marketplace pour freelances")
print(f"Startup créée: {result['startup']['idea']}")
```

## 📋 Résultat attendu

1. **POST /create-startup** avec `{"idea": "SaaS marketplace"}`
2. **CEO Agent** → roadmap business
3. **CTO Agent** → stack technique  
4. **Dev Agents** → MVP backend + frontend
5. **Marketing Agent** → logo.svg + landing page React
6. **`/generated/landing-page`** contient une landing page marketing complète

## 🎨 Landing Page React

### Structure
- **Hero Section** : Logo + headline + tagline + CTA
- **Features Section** : 4 cartes avec fonctionnalités
- **Pricing Section** : 3 plans (Starter, Pro, Enterprise)
- **Footer** : Contact et copyright

### Style
- Fond blanc avec accent bleu (#2563EB)
- Cards arrondies avec hover effects
- Police Inter
- Responsive design
- Animations CSS

## 🔧 Technologies

- **Python 3.8+** : Agents IA et orchestration
- **React 18** : Landing page
- **Tailwind CSS** : Styling moderne
- **Vite** : Build tool
- **SVG** : Logo vectoriel

## 📁 Fichiers générés

- ✅ **Logo SVG** : Design minimal et moderne
- ✅ **Landing page React** : Interface complète
- ✅ **Configuration Tailwind** : Styles optimisés
- ✅ **Package.json** : Dépendances prêtes
- ✅ **Documentation** : README et guides

## 🚀 Démarrage rapide

```bash
# 1. Cloner le projet
git clone <repository>
cd epic4-startup-generator

# 2. Tester le marketing agent
python3 test_simple.py

# 3. Générer une startup complète
python3 main_simple.py

# 4. Voir les résultats
ls -la generated/
```

## 📊 Exemple de sortie

```
🎉 STARTUP GÉNÉRÉE AVEC SUCCÈS !
==================================================
Idée: SaaS marketplace pour freelances
Status: ready
Phases complétées: 4
Taux de succès: 100%

📁 Fichiers générés:
  - Logo: generated/branding/logo.svg
  - Landing page: generated/landing-page
  - Résumé complet: generated/startup_result.json
```

## 🔍 Logs et monitoring

Le système génère des logs détaillés dans le dossier `logs/` :
- Timestamps pour chaque étape
- Succès et erreurs
- Traçabilité complète du processus

## 🎯 Prochaines étapes

- [ ] API REST pour l'intégration
- [ ] Interface web de gestion
- [ ] Plus d'agents spécialisés
- [ ] Templates de landing pages
- [ ] Intégration avec des APIs externes

# Epic6 - Core Engine avec Persistance

## 🎯 Vue d'ensemble

Epic6 est une plateforme complète de génération de startups avec un backend FastAPI robuste et persistant, une interface React moderne, et une architecture WebSocket pour les logs en temps réel.

## 🏗️ Architecture

```
epic6/
├── core-engine/          # Backend FastAPI + PostgreSQL
│   ├── api/             # Routes et schémas API
│   ├── core/            # Configuration et base de données
│   ├── models/          # Modèles SQLAlchemy
│   ├── utils/           # Utilitaires (logger)
│   ├── generated/       # Code généré des projets
│   └── main.py          # Point d'entrée FastAPI
├── frontend/            # Interface React
│   ├── src/
│   │   ├── components/  # Composants React
│   │   └── ...
│   └── package.json
└── README.md
```

## 🚀 Fonctionnalités Principales

### Backend (Core Engine)
- **API REST complète** avec FastAPI
- **Persistance PostgreSQL** avec SQLAlchemy async
- **WebSockets** pour les logs en temps réel
- **Gestion des projets** avec CRUD complet
- **Téléchargement ZIP** des projets générés
- **Logs persistants** avec niveaux et timestamps
- **Migrations Alembic** pour la base de données

### Frontend (React)
- **Dashboard Startups** avec table responsive
- **Modal de détails** pour roadmap et stack
- **Téléchargement direct** des projets
- **Composant Logs** avec WebSocket en temps réel
- **Interface moderne** et responsive

## 📋 Prérequis

- Docker et Docker Compose
- Node.js 16+ (pour le frontend)
- Python 3.11+ (pour le développement backend)

## 🚀 Démarrage Rapide

### 1. Démarrer le Backend

```bash
cd core-engine
./start.sh
```

Le backend sera disponible sur `http://localhost:8000`

### 2. Démarrer le Frontend

```bash
cd frontend
npm install
npm start
```

Le frontend sera disponible sur `http://localhost:3000`

### 3. Vérifier l'Installation

```bash
# Test de l'API
cd core-engine
python test_api.py

# Ouverture de la documentation
open http://localhost:8000/docs
```

## 🌐 API Endpoints

### Projets
- `POST /api/v1/create-startup` - Créer un projet
- `GET /api/v1/projects` - Lister les projets
- `GET /api/v1/projects/{id}` - Détails d'un projet
- `GET /api/v1/projects/{id}/download` - Télécharger le code

### WebSocket
- `WS /ws/logs/{project_id}` - Logs en temps réel

### Santé
- `GET /health` - Vérification de l'état

## 📊 Modèles de Données

### Project
```python
{
  "id": "uuid",
  "idea": "Description de l'idée",
  "roadmap": {"phase1": "MVP", "phase2": "Beta"},
  "stack": {"frontend": "React", "backend": "FastAPI"},
  "created_at": "2024-01-01T00:00:00Z",
  "path": "/generated/uuid"
}
```

### Log
```python
{
  "id": "uuid",
  "project_id": "uuid",
  "message": "Message du log",
  "timestamp": "2024-01-01T00:00:00Z"
}
```

## 🎨 Interface Utilisateur

### Dashboard Startups
- Table responsive avec hover effects
- Boutons d'action (Voir détails, Télécharger)
- Modal pour afficher roadmap et stack
- Formatage des dates en français

### Composant Logs
- Connexion WebSocket automatique
- Affichage en temps réel des logs
- Contrôles de navigation (haut/bas)
- Auto-scroll configurable
- Indicateur de statut de connexion

## 🔧 Configuration

### Variables d'Environnement Backend
```bash
DATABASE_URL=postgresql+asyncpg://admin:secret@db:5432/appdb
SECRET_KEY=your-secret-key-here
```

### Variables d'Environnement Frontend
```bash
REACT_APP_API_URL=http://localhost:8000/api/v1
REACT_APP_WS_URL=ws://localhost:8000
```

## 📝 Utilisation

### 1. Créer une Startup
```bash
curl -X POST "http://localhost:8000/api/v1/create-startup" \
  -H "Content-Type: application/json" \
  -d '{"idea": "SaaS marketplace"}'
```

### 2. Consulter les Projets
- Ouvrir `http://localhost:3000`
- Naviguer vers le dashboard Startups
- Voir la liste des projets créés

### 3. Télécharger un Projet
- Cliquer sur "Télécharger" dans le dashboard
- Le fichier ZIP sera téléchargé automatiquement

### 4. Suivre les Logs
- Utiliser le composant Logs avec un project_id
- Les logs s'affichent en temps réel via WebSocket

## 🛠️ Développement

### Backend
```bash
cd core-engine

# Installer les dépendances
pip install -r requirements.txt

# Lancer en mode développement
uvicorn main:app --reload

# Migrations
alembic upgrade head
```

### Frontend
```bash
cd frontend

# Installer les dépendances
npm install

# Lancer en mode développement
npm start

# Build de production
npm run build
```

## 🧪 Tests

### Tests API
```bash
cd core-engine
python test_api.py
```

### Tests Frontend
```bash
cd frontend
npm test
```

## 📚 Documentation


- **API**: http://localhost:8000/docs (Swagger UI)
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

## 🚨 Dépannage

### Problèmes Courants

1. **Base de données non accessible**
   ```bash
   docker-compose logs db
   docker-compose restart db
   ```

2. **WebSocket non connecté**
   - Vérifier l'URL WebSocket
   - Contrôler les CORS

3. **Erreurs de migration**
   ```bash
   docker-compose down -v
   docker-compose up --build
   ```

### Logs
```bash
# Backend
docker-compose logs -f app

# Base de données
docker-compose logs -f db

# Frontend
npm start

**Epic4** - Transformez vos idées en startups complètes en quelques minutes ! 🚀

## 🔮 Roadmap

- [ ] Authentification JWT
- [ ] Gestion des rôles utilisateurs
- [ ] API de génération de code
- [ ] Intégration CI/CD
- [ ] Monitoring et métriques
- [ ] Tests automatisés
- [ ] Documentation utilisateur


## 🤝 Contribution

1. Fork le projet

2. Créer une branche feature (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)

2. Créer une branche feature
3. Commit les changements
4. Push vers la branche

5. Ouvrir une Pull Request

## 📄 Licence


Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.


## 🆘 Support

- **Issues**: GitHub Issues
- **Documentation**: Wiki du projet
- **Discord**: Serveur communautaire
- **Email**: support@startupdao.com

---

**Développé avec ❤️ par l'équipe StartupDAO**

- **Documentation**: README et /docs
- **API**: Swagger UI sur /docs

---

**Epic6** - Transformez vos idées en startups fonctionnelles 🚀

