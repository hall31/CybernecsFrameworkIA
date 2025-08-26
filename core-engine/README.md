# 🚀 Epic 15: Startup Tokenization Marketplace

## 📋 Vue d'ensemble

L'Epic 15 implémente un système complet de marketplace pour l'échange de tokens de startups. Cette fonctionnalité permet aux investisseurs d'acheter et de vendre des parts tokenisées de startups sur un exchange interne sécurisé.

## 🏗️ Architecture

### Core Engine (`/core-engine`)

```
core-engine/
├── agents/
│   ├── __init__.py
│   └── market_agent.py          # Agent principal du marketplace
├── contracts/                   # Smart contracts (futur)
├── utils/                       # Utilitaires
├── main.py                      # API Flask principale
└── requirements.txt             # Dépendances Python
```

### Dashboard React (`/dashboard`)

- **Page Global Market**: Interface complète du marketplace
- **Graphiques interactifs**: Prix, volumes, répartition portefeuille
- **Tableau des tokens**: Liste des startups avec actions Acheter/Vendre

## 🔧 Composants Techniques

### 1. MarketAgent (`market_agent.py`)

**Responsabilités :**
- Gestion du marketplace des startups tokenisées
- Listing automatique des tokens sur l'exchange
- Création de smart contracts marketplace
- Génération de données de marché simulées

**Méthodes principales :**
- `run()`: Point d'entrée principal
- `get_tokenised_startups()`: Récupération des startups
- `list_startup_on_exchange()`: Listing sur l'exchange
- `create_marketplace_contract()`: Création du smart contract
- `generate_price_history()`: Historique des prix
- `get_market_stats()`: Statistiques globales

**Données simulées :**
- 5 startups tokenisées (TechFlow, GreenEnergy, HealthTech, FinTech, AI Dynamics)
- Prix basés sur valuation + volatilité
- Volumes d'échange aléatoires
- Variations de prix 24h

### 2. API Flask (`main.py`)

**Endpoints :**
- `GET /market` - Données complètes du marketplace
- `GET /market/token/<symbol>` - Détails d'un token
- `GET /market/stats` - Statistiques globales
- `GET /market/orderbook/<symbol>` - Order book d'un token
- `GET /market/price-history/<symbol>` - Historique des prix

**Fonctionnalités :**
- Gestion d'erreurs robuste
- Logging détaillé
- CORS activé pour le dashboard
- Réponses JSON standardisées

### 3. Dashboard Global Market

**Interface inspirée Nasdaq/Binance :**
- Header premium avec gradient bleu/violet
- Tableau des tokens avec actions Acheter/Vendre
- Panneau de détails du token sélectionné
- Graphiques interactifs (Recharts)
- Statistiques en temps réel

**Composants visuels :**
- 📊 Tableau des startups tokenisées
- 📈 Graphique d'évolution des prix (7j/30j)
- 📊 Graphique des volumes par startup
- 🥧 Répartition du portefeuille (Pie chart)
- 🎨 Icônes sectorielles et badges de stage

## 🚀 Démarrage Rapide

### 1. Backend Python

```bash
cd core-engine
pip install -r requirements.txt
python main.py
```

**API accessible sur :** `http://localhost:5000`

### 2. Dashboard React

```bash
cd dashboard
npm install
npm run dev
```

**Dashboard accessible sur :** `http://localhost:5173`

## 📊 Données du Marketplace

### Startups Simulées

| Symbol | Nom | Secteur | Stage | Valuation | Prix Token |
|--------|-----|---------|-------|-----------|------------|
| STK001 | TechFlow Solutions | SaaS | Series A | 2.5M € | 2.50 € |
| STK002 | GreenEnergy Corp | CleanTech | Seed | 1.8M € | 0.90 € |
| STK003 | HealthTech Innovations | HealthTech | Series B | 3.2M € | 2.13 € |
| STK004 | FinTech Revolution | FinTech | Series A | 4.5M € | 1.50 € |
| STK005 | AI Dynamics | AI | Seed | 2.8M € | 3.50 € |

### Statistiques Globales

- **Total Tokens Listés :** 5
- **Market Cap Total :** 14.8M €
- **Volume 24h :** Variable (simulé)
- **Sentiment :** Bullish/Neutral

## 🔮 Fonctionnalités Futures

### Smart Contracts
- Intégration Ethereum/Polygon
- Achat/Vente automatisés
- Gestion de la liquidité
- Settlement automatique

### Trading Avancé
- Order book en temps réel
- Stop-loss et take-profit
- Trading algorithmique
- Notifications de prix

### Analytics
- Indicateurs techniques
- Analyse fondamentale
- Comparaison sectorielle
- Prédictions IA

## 🧪 Tests

### Test du MarketAgent

```bash
cd core-engine
python -c "
from agents.market_agent import MarketAgent
agent = MarketAgent()
result = agent.run()
print('Marketplace initialisé avec succès!')
print(f'Tokens listés: {len(result[\"listed_tokens\"])}')
"
```

### Test de l'API

```bash
# Test de santé
curl http://localhost:5000/health

# Récupération du marché
curl http://localhost:5000/market

# Détails d'un token
curl http://localhost:5000/market/token/STK001
```

## 📝 Logs

Le système génère des logs détaillés pour :
- Initialisation du marketplace
- Listing des startups
- Création des smart contracts
- Erreurs et exceptions
- Activité des utilisateurs

## 🔒 Sécurité

- Validation des données d'entrée
- Gestion d'erreurs robuste
- Logs de sécurité
- CORS configuré
- Rate limiting (futur)

## 📈 Métriques

- Performance de l'API
- Temps de réponse
- Taux d'erreur
- Utilisation des ressources
- Activité des utilisateurs

---

**🎯 Epic 15 - Marketplace des Startups Tokenisées**  
*Développé avec ❤️ pour la révolution de la finance décentralisée*