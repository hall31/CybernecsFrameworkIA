# 🏦 Epic 16: Fonds Décentralisés (ETF) pour Startups IA

## 📋 Vue d'ensemble

L'Epic 16 implémente un système complet de gestion de fonds décentralisés (ETF) pour les startups IA, permettant aux investisseurs de diversifier automatiquement leurs investissements dans plusieurs startups via un seul token.

## 🏗️ Architecture

### 1. Backend (Core Engine)

#### FundAgent (`/core-engine/agents/fund_agent.py`)
- **Classe principale** : `FundAgent`
- **Responsabilités** :
  - Création de fonds décentralisés
  - Gestion de la composition des portefeuilles
  - Génération de smart contracts simulés
  - Calcul du NAV (Net Asset Value)

#### Endpoints API (`/core-engine/main.py`)
- `POST /funds` : Création d'un nouveau fonds
- `GET /funds` : Récupération de tous les fonds
- `GET /funds/{symbol}` : Détails d'un fonds spécifique
- `PUT /funds/{symbol}/nav` : Mise à jour du NAV

### 2. Frontend (Dashboard React)

#### Composants créés
- **FundsPage** : Page principale de gestion des fonds
- **FundCard** : Carte d'affichage d'un fonds
- **FundCreationForm** : Formulaire de création de fonds
- **FundDetails** : Vue détaillée d'un fonds

#### Fonctionnalités
- Interface moderne inspirée des dashboards ETF
- Création de fonds avec sélection de startups
- Visualisation de la composition des portefeuilles
- Actions d'investissement et de vente
- Navigation entre les pages

## 🚀 Fonctionnalités

### Création de Fonds
1. **Sélection de startups** : Interface intuitive avec checkboxes
2. **Calcul automatique des poids** : Distribution équilibrée des pourcentages
3. **Génération de smart contract** : Adresse Ethereum simulée
4. **Symbole unique** : Format ETF + 3 chiffres (ex: ETF001)

### Gestion des Portefeuilles
- **Composition dynamique** : Support de 2 à N startups
- **Poids équilibrés** : Distribution intelligente des pourcentages
- **NAV en temps réel** : Valeur nette du portefeuille
- **Statut des fonds** : Actif/Inactif

### Interface Utilisateur
- **Design moderne** : Inspiré de Robinhood/Binance
- **Responsive** : Adaptation mobile et desktop
- **Graphiques** : Placeholders pour futurs intégrations
- **Navigation fluide** : Entre les différentes vues

## 📊 Structure des Données

### Fonds
```json
{
  "fund_address": "0xFUND123...",
  "fund_symbol": "ETF001",
  "composition": [
    {"token": "STK001", "weight": "40%", "percentage": 40},
    {"token": "STK002", "weight": "30%", "percentage": 30},
    {"token": "STK003", "weight": "30%", "percentage": 30}
  ],
  "nav": "100.00 €",
  "created_at": "2024-01-15T10:30:00",
  "status": "active"
}
```

### Composition des Poids
- **2 startups** : 60% / 40%
- **3 startups** : 40% / 30% / 30%
- **4 startups** : 30% / 25% / 25% / 20%
- **N startups** : Distribution équilibrée

## 🧪 Tests

### Script de Test
- **Fichier** : `test_funds_api.py`
- **Fonctionnalités** :
  - Test de création de fonds
  - Test de récupération
  - Test de mise à jour NAV
  - Test de validation des erreurs

### Exécution
```bash
cd core-engine
python test_funds_api.py
```

## 🔧 Installation et Démarrage

### Backend
```bash
cd core-engine
pip install -r requirements.txt
python main.py
```

### Frontend
```bash
cd dashboard
npm install
npm run dev
```

## 🌐 Endpoints API

### Créer un Fonds
```http
POST /funds
Content-Type: application/json

{
  "startups": ["STK001", "STK002", "STK003"]
}
```

### Récupérer Tous les Fonds
```http
GET /funds
```

### Récupérer un Fonds
```http
GET /funds/ETF001
```

### Mettre à Jour le NAV
```http
PUT /funds/ETF001/nav?nav=105.50 €
```

## 🎨 Interface Utilisateur

### Couleurs et Style
- **Fond principal** : `#F9FAFB` (gris très clair)
- **Cartes** : Blanc avec ombres `shadow-xl`
- **Boutons primaires** : Bleu `#2563EB`
- **Boutons d'action** : Vert (investir) / Rouge (vendre)
- **Bordures** : `rounded-2xl` pour un look moderne

### Composants Visuels
- **Statistiques** : Cards avec icônes et métriques
- **Tableaux** : Grilles responsives pour les fonds
- **Formulaires** : Modales avec validation
- **Navigation** : Sidebar avec icônes FontAwesome

## 🔮 Évolutions Futures

### Intégrations Réelles
- **Smart Contracts** : Déploiement sur Ethereum/Polygon
- **Oracles** : Prix en temps réel des tokens
- **DEX** : Intégration avec Uniswap/PancakeSwap
- **Wallet** : Connexion MetaMask/Phantom

### Fonctionnalités Avancées
- **Rebalancing** : Rééquilibrage automatique des portefeuilles
- **Staking** : Récompenses pour les détenteurs de fonds
- **Governance** : Vote sur les compositions
- **Analytics** : Graphiques de performance avancés

### Données Réelles
- **Market Data** : Intégration avec CoinGecko/CoinMarketCap
- **News Feed** : Actualités des startups incluses
- **Social Trading** : Suivi des investisseurs influents
- **Notifications** : Alertes sur les mouvements de prix

## 📈 Métriques de Succès

### Technique
- ✅ API fonctionnelle avec tous les endpoints
- ✅ Interface utilisateur responsive et moderne
- ✅ Gestion d'état et navigation fluide
- ✅ Validation des données et gestion d'erreurs

### Fonctionnel
- ✅ Création de fonds avec composition dynamique
- ✅ Gestion des portefeuilles diversifiés
- ✅ Interface d'investissement intuitive
- ✅ Visualisation des données de fonds

### Utilisateur
- ✅ Expérience similaire aux plateformes ETF existantes
- ✅ Navigation claire entre les différentes vues
- ✅ Actions d'investissement et de vente
- ✅ Informations détaillées sur chaque fonds

## 🎯 Résultat Final

L'Epic 16 délivre un système complet de gestion de fonds décentralisés pour startups IA, permettant aux investisseurs de :

1. **Créer des portefeuilles diversifiés** en sélectionnant plusieurs startups
2. **Investir via un seul token** représentant le fonds complet
3. **Suivre la performance** avec des métriques en temps réel
4. **Gérer leurs investissements** via une interface moderne et intuitive

Le système est prêt pour l'intégration avec de vrais smart contracts et des données de marché en temps réel, offrant une base solide pour une plateforme d'investissement DeFi complète.