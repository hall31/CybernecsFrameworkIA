# 🚀 Dashboard d'Orchestration Admin

## 📋 Description

Le dashboard d'orchestration permet de gérer en temps réel vos agents et épics. Il offre une interface moderne et intuitive pour :

- **Agents** : Activer/désactiver et surveiller le statut
- **Épics** : Activer/désactiver, exécuter et surveiller le statut
- **Monitoring** : Visualisation en temps réel des états

## 🎯 Fonctionnalités

### 🤖 Gestion des Agents
- Liste des agents avec statut en temps réel
- Switch ON/OFF pour activer/désactiver
- Badges de statut : 🟢 Actif, 🟡 Désactivé, 🔴 Erreur
- Interface responsive avec grille adaptative

### 📋 Gestion des Épics
- Liste des épics avec statut détaillé
- Switch ON/OFF pour activer/désactiver
- Bouton "Run" pour exécuter les épics
- Badges de statut : 🔄 En cours, ✅ Terminé, ⏸️ Désactivé, ❌ Échec, ⏳ En attente

### 🔄 Fonctionnalités Globales
- Bouton "Rafraîchir" pour synchroniser les données
- Gestion d'erreurs avec messages utilisateur
- État de chargement avec spinner
- Interface responsive et moderne

## 🏗️ Architecture

### Composants
- **`Orchestration.jsx`** : Page principale avec logique métier
- **`AgentCard.jsx`** : Carte individuelle pour chaque agent
- **`EpicCard.jsx`** : Carte individuelle pour chaque épic

### API Endpoints
```
GET    /agents                    → Liste des agents
POST   /agents/{name}/toggle     → Activer/désactiver un agent
GET    /epics                     → Liste des épics
POST   /epics/{id}/toggle        → Activer/désactiver un épic
POST   /epics/{id}/run           → Exécuter un épic
```

## 🚀 Installation et Utilisation

### 1. Démarrage
```bash
cd dashboard
npm install
npm run dev
```

### 2. Navigation
- Accédez à la page "Orchestration" via la sidebar
- Utilisez les switches pour activer/désactiver
- Cliquez sur "Run" pour exécuter un épic
- Utilisez le bouton "Rafraîchir" pour synchroniser

### 3. Mode Développement
En mode développement, l'application utilise des données de test (`mockData.js`) :
- 5 agents avec différents statuts
- 6 épics avec différents états
- Simulation des appels API

## 🎨 Design

### Technologies
- **React 18** avec hooks modernes
- **Tailwind CSS** pour le styling
- **Responsive Design** avec grilles adaptatives
- **Animations** et transitions fluides

### Palette de Couleurs
- **Bleu** : Actions principales, liens
- **Vert** : Statuts positifs, succès
- **Rouge** : Erreurs, statuts critiques
- **Jaune** : Statuts neutres, désactivés
- **Gris** : Éléments secondaires, arrière-plans

## 🔧 Configuration

### Variables d'Environnement
```bash
# Mode développement (utilise mockData)
NODE_ENV=development

# Mode production (utilise API réelle)
NODE_ENV=production
```

### Personnalisation
- Modifiez `mockData.js` pour changer les données de test
- Ajustez les couleurs dans les composants
- Personnalisez les statuts dans `statusConfig`

## 📱 Responsive

Le dashboard s'adapte à tous les écrans :
- **Mobile** : 1 colonne
- **Tablet** : 2 colonnes
- **Desktop** : 3-4 colonnes
- **Large** : 4+ colonnes

## 🚨 Gestion d'Erreurs

- Messages d'erreur utilisateur
- Fallback sur données de test en développement
- Logs console pour le debugging
- États de chargement et d'erreur

## 🔮 Évolutions Futures

- [ ] Notifications en temps réel
- [ ] Graphiques de performance
- [ ] Historique des exécutions
- [ ] Configuration avancée des agents
- [ ] Logs détaillés des épics
- [ ] Métriques et analytics

---

**Développé avec ❤️ pour la Startup Factory**