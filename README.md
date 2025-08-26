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

## 🤝 Contribution

1. Fork le projet
2. Créer une branche feature (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
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
