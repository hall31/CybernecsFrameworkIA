# 🚀 EPIC 17: Hedge Fund IA - Système de Trading Automatisé

## 📋 Vue d'ensemble

L'Epic 17 implémente un système complet de hedge fund IA automatisé, combinant intelligence artificielle, analyse de données en temps réel, et smart contracts pour la gestion automatisée de portefeuilles d'investissement.

## 🏗️ Architecture du Système

### 1. HedgeFundAgent (`/core-engine/agents/hedgefund_agent.py`)

**Agent IA spécialisé en trading quantitatif**

- **Stratégies ML implémentées :**
  - **Momentum** (40% du poids) : Détection des tendances de marché
  - **Mean Reversion** (30% du poids) : Retour à la moyenne des prix
  - **Volatilité** (30% du poids) : Gestion du risque

- **Fonctionnalités :**
  - Analyse de données de marché en temps réel
  - Génération de signaux de trading
  - Optimisation de portefeuille
  - Calcul de métriques de performance (ROI, Sharpe ratio, volatilité)

- **Portefeuille géré :**
  - Positions long sur startups et ETF prometteurs
  - Positions short sur actifs surévalués
  - Réserve de liquidités dynamique

### 2. TraderContract (`/core-engine/contracts/trader_contract.py`)

**Smart contract pour l'exécution des trades**

- **Méthodes principales :**
  - `buy(token, amount, price, caller)` : Achat de tokens
  - `sell(token, amount, price, caller)` : Vente de tokens
  - `rebalance(caller)` : Rebalancement du portefeuille

- **Sécurité :**
  - Seul le HedgeFundAgent peut exécuter des trades
  - Ledger on-chain de toutes les positions
  - Calcul automatique des frais (0.1% par trade)

### 3. API Backend (`/core-engine/main.py`)

**Endpoints REST pour le hedge fund**

- `GET /hedgefund` : Statut complet du portefeuille
- `POST /hedgefund/rebalance` : Rebalancement manuel

### 4. Dashboard React (`/dashboard/src/components/HedgeFund.jsx`)

**Interface utilisateur professionnelle style trading**

- **Sections principales :**
  - **Ticker en temps réel** : Prix des tokens avec animations
  - **Métriques de performance** : ROI, volatilité, Sharpe ratio
  - **Positions** : Vue détaillée long/short
  - **Stratégie IA** : Commentaire automatique de la stratégie
  - **Rebalancement** : Bouton pour forcer le rebalancement

## 🎯 Fonctionnalités Clés

### Trading Automatisé
- Exécution automatique de stratégies ML
- Gestion dynamique des positions
- Optimisation continue du portefeuille

### Analyse en Temps Réel
- Données de marché simulées
- Signaux de trading générés automatiquement
- Métriques de performance calculées en continu

### Interface Professionnelle
- Design inspiré des plateformes Bloomberg/Binance
- Animations de prix en temps réel
- Indicateurs visuels de performance

## 🚀 Installation et Démarrage

### 1. Backend (Core Engine)

```bash
cd core-engine

# Installation des dépendances
pip install -r requirements.txt

# Test du système
python test_hedgefund.py

# Démarrage du serveur
python main.py
```

### 2. Frontend (Dashboard)

```bash
cd dashboard

# Installation des dépendances
npm install

# Démarrage en mode développement
npm run dev
```

## 🧪 Tests

Le système inclut une suite de tests complète :

```bash
cd core-engine
python test_hedgefund.py
```

**Tests inclus :**
- ✅ HedgeFundAgent : Stratégies ML et optimisation
- ✅ TraderContract : Smart contract et sécurité
- ✅ Intégration : Communication agent-contrat

## 📊 Exemple d'Utilisation

### 1. Démarrage Automatique

L'agent HedgeFund s'exécute automatiquement et :
- Analyse les données de marché
- Génère des signaux de trading
- Optimise le portefeuille
- Met à jour les positions

### 2. Consultation du Portefeuille

```bash
curl http://localhost:8000/hedgefund
```

**Réponse :**
```json
{
  "portfolio": {
    "long_positions": [
      {"token": "STK001", "allocation": "25.0%", "amount_usd": 250000}
    ],
    "short_positions": [
      {"token": "STK005", "allocation": "15.0%", "amount_usd": 150000}
    ],
    "cash_reserve": "40.0%"
  },
  "performance": {
    "roi": 12.5,
    "volatility": 18.2,
    "sharpe_ratio": 1.8
  },
  "strategy_commentary": "Nous renforçons notre position long sur les startups technologiques..."
}
```

### 3. Rebalancement Manuel

```bash
curl -X POST http://localhost:8000/hedgefund/rebalance
```

## 🔧 Configuration

### Stratégies de Trading

Les poids des stratégies sont configurables dans `HedgeFundAgent` :

```python
self.strategies = {
    "momentum": {"weight": 0.4, "lookback_days": 30},
    "mean_reversion": {"weight": 0.3, "lookback_days": 60},
    "volatilité": {"weight": 0.3, "lookback_days": 20}
}
```

### Tokens Supportés

```python
self.available_tokens = {
    "STK001": {"name": "FinTech Startup", "type": "startup"},
    "STK002": {"name": "AI Startup", "type": "startup"},
    "ETF001": {"name": "AI Technology ETF", "type": "etf"},
    # ... autres tokens
}
```

## 📈 Métriques de Performance

### ROI (Return on Investment)
- Calculé en temps réel
- Comparaison avec capital initial ($1M)

### Sharpe Ratio
- Ratio risque/rendement
- Cible : > 1.0 (bonne performance)

### Volatilité
- Mesure du risque
- Annualisée sur 252 jours de trading

## 🔒 Sécurité

- **Authentification** : Seul HedgeFundAgent peut trader
- **Validation** : Vérification des montants et tokens
- **Audit trail** : Historique complet des trades
- **Frais** : Calcul automatique et transparent

## 🚧 Limitations Actuelles

- **Simulation** : Données de marché simulées
- **Tokens** : Support limité aux tokens définis
- **Stratégies** : Algorithmes ML basiques (ARIMA, LSTM à implémenter)

## 🔮 Évolutions Futures

### Phase 2 : ML Avancé
- Implémentation de LSTM/Transformer
- Intégration d'APIs de données réelles
- Backtesting des stratégies

### Phase 3 : DeFi
- Intégration avec Uniswap/SushiSwap
- Yield farming automatisé
- Gestion des liquidités

### Phase 4 : Multi-Chain
- Support Ethereum, Polygon, BSC
- Cross-chain arbitrage
- Gestion des gas fees

## 📞 Support

Pour toute question ou problème :
1. Vérifier les logs dans la console
2. Exécuter les tests : `python test_hedgefund.py`
3. Consulter la documentation API : `http://localhost:8000/docs`

---

**🎉 Epic 17 déployé avec succès ! Le Hedge Fund IA est maintenant opérationnel et prêt à trader !**