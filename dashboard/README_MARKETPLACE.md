# 🌐 Global Market - Epic 15

## 🚀 Démarrage Rapide

### 1. Démarrer l'API Backend

```bash
# Dans un terminal
cd core-engine
python3 main.py
```

**L'API sera accessible sur :** `http://localhost:5000`

### 2. Démarrer le Dashboard React

```bash
# Dans un autre terminal
cd dashboard
npm run dev
```

**Le dashboard sera accessible sur :** `http://localhost:5173`

### 3. Accéder au Global Market

1. Ouvrir le dashboard dans le navigateur
2. Cliquer sur "Global Market" dans la sidebar
3. Vérifier que l'API est connectée via le composant de statut

## 📊 Fonctionnalités du Marketplace

### Tableau des Tokens
- **5 startups tokenisées** avec données simulées
- **Prix en temps réel** avec variations 24h
- **Actions Acheter/Vendre** pour chaque token
- **Filtres par secteur** et stage de développement

### Graphiques Interactifs
- 📈 **Évolution des prix** (7j/30j)
- 📊 **Volume par startup** (Bar chart)
- 🥧 **Répartition du portefeuille** (Pie chart)

### Détails des Startups
- **Informations complètes** : secteur, stage, valuation
- **Statistiques de trading** : volume, market cap
- **Actions rapides** : achat/vente direct

## 🔧 Configuration

### API Endpoints

| Endpoint | Description | Méthode |
|----------|-------------|---------|
| `/market` | Données complètes du marketplace | GET |
| `/market/token/<symbol>` | Détails d'un token | GET |
| `/market/stats` | Statistiques globales | GET |
| `/market/orderbook/<symbol>` | Order book d'un token | GET |
| `/market/price-history/<symbol>` | Historique des prix | GET |

### Startups Simulées

| Symbol | Nom | Secteur | Stage | Valuation |
|--------|-----|---------|-------|-----------|
| STK001 | TechFlow Solutions | SaaS | Series A | 2.5M € |
| STK002 | GreenEnergy Corp | CleanTech | Seed | 1.8M € |
| STK003 | HealthTech Innovations | HealthTech | Series B | 3.2M € |
| STK004 | FinTech Revolution | FinTech | Series A | 4.5M € |
| STK005 | AI Dynamics | AI | Seed | 2.8M € |

## 🧪 Tests

### Test de l'API

```bash
cd core-engine
python3 demo.py
```

### Test du Dashboard

1. Vérifier la connectivité API via le composant de statut
2. Naviguer vers "Global Market"
3. Vérifier l'affichage des tokens
4. Tester les graphiques interactifs

## 🎨 Design

### Style Nasdaq/Binance
- **Fond sombre premium** (#0F172A)
- **Gradients bleu/violet** pour les headers
- **Icônes crypto** et sectorielles
- **Graphiques interactifs** avec Recharts

### Composants Visuels
- 📊 Tableau responsive des tokens
- 🎯 Panneau de détails contextuel
- 📈 Graphiques temps réel
- 🎨 Badges et indicateurs visuels

## 🔮 Fonctionnalités Futures

### Smart Contracts
- Intégration blockchain
- Trading automatisé
- Gestion de la liquidité

### Analytics Avancés
- Indicateurs techniques
- Prédictions IA
- Comparaisons sectorielles

### Trading Social
- Portefeuilles publics
- Suivi des investisseurs
- Notifications de prix

## 🐛 Dépannage

### API non accessible
```bash
# Vérifier que l'API est démarrée
cd core-engine
python3 main.py

# Vérifier le port 5000
netstat -tulpn | grep 5000
```

### Dashboard ne charge pas
```bash
# Vérifier les dépendances
cd dashboard
npm install

# Redémarrer le serveur
npm run dev
```

### Erreurs CORS
- Vérifier que l'API Flask a CORS activé
- Vérifier les URLs dans `config.js`

## 📝 Logs

### Backend
- Logs détaillés dans la console
- Événements du MarketAgent
- Erreurs et exceptions

### Frontend
- Console du navigateur
- Composant de statut API
- Gestion d'erreurs utilisateur

---

**🎯 Epic 15 - Marketplace des Startups Tokenisées**  
*Interface moderne et fonctionnelle pour l'échange de tokens*