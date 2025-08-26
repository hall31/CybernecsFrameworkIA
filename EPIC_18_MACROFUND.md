# 🚀 EPIC 18: MacroFund - Fonds Multi-Actifs Global

## 📋 Vue d'ensemble

L'épic 18 implémente un système de gestion de portefeuille multi-actifs global avec arbitrages intelligents et hedging automatique. Le MacroFundAgent analyse les corrélations entre marchés et exécute des stratégies d'allocation dynamiques.

## 🏗️ Architecture

### 1. MacroFundAgent (`/core-engine/agents/macrofund_agent.py`)

**Responsabilités :**
- Analyse multi-actifs globale (startups IA, crypto, actions, matières premières, forex)
- Calcul des corrélations entre marchés
- Création d'allocations macro dynamiques
- Exécution d'arbitrages automatiques
- Gestion des positions de hedge

**Fonctionnalités clés :**
- Récupération de données internes (tokens startups, ETF IA, positions hedge)
- Récupération de données externes (APIs crypto, actions, commodities)
- Analyse des corrélations Nasdaq-IA, BTC-tokens IA, etc.
- Ajustements automatiques d'allocation basés sur les corrélations
- Logging complet des événements et arbitrages

### 2. GlobalTraderContract (`/core-engine/agents/global_trader_contract.py`)

**Responsabilités :**
- Exécution des transactions multi-actifs
- Gestion des positions et de l'historique
- Calcul des frais par type d'actif
- Rééquilibrage automatique du portefeuille

**Types d'actifs supportés :**
- **Startup Tokens** : AI_Startup_1, AI_Startup_2, AI_Startup_3
- **Crypto** : BTC, ETH, AI_Token
- **Stocks** : NASDAQ_ETF, S&P500_ETF, Tech_ETF
- **Commodities** : Gold, Oil, Silver
- **Forex** : EUR/USD, XAF/EUR

**Structure des frais :**
- Startup tokens : 1%
- Crypto : 0.2%
- Stocks : 0.1%
- Commodities : 0.15%
- Forex : 0.05%

### 3. API Endpoints (`/core-engine/main.py`)

**GET `/macrofund`**
- Retourne l'état complet du portefeuille
- Allocations actuelles, hedges, arbitrages récents
- Performance YTD, Sharpe ratio, drawdown maximum

**POST `/macrofund/execute`**
- Lance l'analyse macro et l'exécution des arbitrages
- Retourne le résumé des actions effectuées

### 4. Dashboard React (`/dashboard/src/components/MacroFund.jsx`)

**Sections principales :**
- **Allocation** : Pie chart des allocations avec couleurs par actif
- **Valeur Totale** : NAV, performance YTD, métriques de risque
- **Arbitrages** : Liste des derniers arbitrages avec statuts
- **Hedging** : Positions de hedge actives/inactives
- **Performance** : Graphique NAV sur 30 jours

**Design :**
- Fond sombre premium (#111827)
- Couleurs thématiques : bleu (IA), orange (crypto), vert (stocks), jaune (or)
- Animations et transitions fluides
- Interface responsive et moderne

## 🔄 Flux de fonctionnement

### 1. Cycle d'exécution
```
1. Récupération données internes (tokens, ETF, positions)
2. Récupération données externes (APIs marchés)
3. Analyse des corrélations entre marchés
4. Calcul des nouvelles allocations cibles
5. Exécution des arbitrages via GlobalTraderContract
6. Mise à jour du portefeuille et des hedges
7. Logging des événements et résultats
```

### 2. Logique d'arbitrage
- **Seuil de déclenchement** : 2% de différence d'allocation
- **Exemple Nasdaq-IA** : Si Nasdaq chute, réduire exposition SaaS de 5%
- **Exemple BTC-IA** : Si BTC monte, augmenter crypto de 5%, réduire IA de 3%
- **Hedging dynamique** : Activation automatique des hedges selon le sentiment de risque

### 3. Gestion des risques
- **Diversification** : Répartition sur 5 classes d'actifs
- **Hedging** : Short Nasdaq ETF, Long Gold
- **Corrélations** : Ajustements automatiques basés sur les relations inter-marchés
- **Seuils** : Limites de position et de réallocation

## 📊 Métriques et KPIs

### Performance
- **NAV** : Valeur nette du portefeuille
- **Performance YTD** : Rendement année en cours
- **Sharpe Ratio** : Ratio risque/rendement ajusté
- **Max Drawdown** : Perte maximale historique

### Allocations
- **IA Startups** : 40% (innovation technologique)
- **ETF IA** : 20% (exposition sectorielle)
- **Crypto** : 25% (actifs numériques)
- **Stocks** : 10% (marchés traditionnels)
- **Commodities** : 5% (matières premières)

### Hedges
- **Short Nasdaq ETF** : 5% (protection contre chute tech)
- **Long Gold** : 3% (refuge en période de risque)

## 🚀 Démarrage et utilisation

### 1. Installation des dépendances
```bash
# Core Engine
cd core-engine
pip install -r requirements.txt

# Dashboard
cd dashboard
npm install
```

### 2. Lancement des services
```bash
# Core Engine (Terminal 1)
cd core-engine
python main.py

# Dashboard (Terminal 2)
cd dashboard
npm run dev
```

### 3. Test du système
```bash
# Test des agents
cd core-engine
python test_macrofund.py

# Test des endpoints
curl http://localhost:8000/macrofund
curl -X POST http://localhost:8000/macrofund/execute
```

### 4. Accès au dashboard
- **Startup Factory** : http://localhost:5173/ (onglet par défaut)
- **Macro Fund** : http://localhost:5173/ → Onglet "📊 Macro Fund"

## 🔧 Configuration et personnalisation

### Variables d'environnement
```bash
# Taille du portefeuille (défaut: 50M €)
PORTFOLIO_SIZE=50000000

# Seuils d'arbitrage (défaut: 2%)
ARBITRAGE_THRESHOLD=0.02

# Fréquence d'exécution (cron)
MACROFUND_CRON="0 */4 * * *"  # Toutes les 4 heures
```

### Personnalisation des corrélations
```python
# Dans macrofund_agent.py
correlations = {
    "nasdaq_ai_correlation": -0.75,      # Ajustable selon l'historique
    "btc_ai_tokens_correlation": 0.60,   # Relation crypto-IA
    "gold_risk_off": 0.80,               # Sentiment de risque
    "oil_inflation": 0.45,               # Pression inflationniste
    "eur_usd_risk": -0.30                # Sentiment EUR
}
```

## 📈 Roadmap et évolutions

### Phase 2 (Prochaine itération)
- [ ] Intégration d'APIs réelles (CoinGecko, Yahoo Finance, Alpha Vantage)
- [ ] Machine Learning pour prédiction des corrélations
- [ ] Backtesting des stratégies historiques
- [ ] Alertes et notifications en temps réel

### Phase 3 (Évolutions avancées)
- [ ] Support des options et dérivés
- [ ] Gestion des devises multiples
- [ ] Intégration DeFi (liquidity pools, yield farming)
- [ ] Dashboard avancé avec métriques ESG

## 🧪 Tests et validation

### Tests unitaires
```bash
python -m pytest test_macrofund.py -v
```

### Tests d'intégration
```bash
# Démarrer le serveur
python main.py

# Dans un autre terminal
python test_macrofund.py
```

### Validation des endpoints
```bash
# Test GET
curl -s http://localhost:8000/macrofund | jq '.'

# Test POST
curl -X POST http://localhost:8000/macrofund/execute | jq '.'
```

## 🐛 Dépannage

### Problèmes courants

**1. Erreur de connexion API**
```bash
# Vérifier que le serveur est démarré
netstat -tlnp | grep :8000

# Vérifier les logs
tail -f core-engine/logs/app.log
```

**2. Erreur de dépendances**
```bash
# Mettre à jour pip
pip install --upgrade pip

# Réinstaller les dépendances
pip install -r requirements.txt --force-reinstall
```

**3. Erreur de port dashboard**
```bash
# Vérifier le port 5173
netstat -tlnp | grep :5173

# Changer le port si nécessaire
npm run dev -- --port 3000
```

## 📚 Ressources et références

### Documentation technique
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Recharts Documentation](https://recharts.org/)
- [Tailwind CSS](https://tailwindcss.com/)

### Concepts financiers
- [Modern Portfolio Theory](https://en.wikipedia.org/wiki/Modern_portfolio_theory)
- [Correlation Analysis](https://en.wikipedia.org/wiki/Correlation_and_dependence)
- [Hedging Strategies](https://en.wikipedia.org/wiki/Hedge_(finance))

### APIs de marché
- [CoinGecko API](https://www.coingecko.com/en/api)
- [Yahoo Finance API](https://finance.yahoo.com/)
- [Alpha Vantage](https://www.alphavantage.co/)

---

## 🎯 Résultat attendu

L'épic 18 délivre un système complet de gestion de portefeuille multi-actifs avec :

1. **MacroFundAgent** qui s'exécute automatiquement et analyse les marchés
2. **Allocation globale** entre startups IA et marchés traditionnels
3. **Endpoint `/macrofund`** qui donne une vision complète multi-actifs
4. **Dashboard Macro Fund** avec vue globale type "fonds souverain"
5. **Arbitrages en live** avec exécution automatique
6. **Hedges actifs** (or, indices) pour la protection du capital

Le système fonctionne comme un "fonds souverain" intelligent qui optimise en permanence l'allocation entre innovation technologique et marchés établis, avec une gestion proactive des risques via le hedging dynamique.