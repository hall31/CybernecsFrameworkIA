# 🚀 ShipFast Dashboard

Un dashboard SaaS moderne et élégant pour gérer vos startups avec l'IA, construit avec React, Next.js et Tailwind CSS.

## ✨ Fonctionnalités

### 🏠 **Home**
- Formulaire pour saisir votre idée de startup
- Génération automatique de roadmap via l'IA CEO Agent
- Redirection automatique vers la roadmap après génération

### 📊 **Logs**
- Stream de logs en temps réel via WebSocket
- Connexion automatique à `ws://localhost:8000/ws/logs`
- Interface terminal avec pause/play et nettoyage
- Reconnexion automatique en cas de déconnexion

### 🗺️ **Roadmap**
- Affichage des épics générés par l'IA
- Chaque épic contient des user stories détaillées
- Statuts visuels (Terminé, En cours, En attente)
- Estimations de temps pour chaque épic

### 🏢 **Startups**
- Historique de toutes vos startups générées
- Tableau moderne avec tri et filtres
- Bouton de téléchargement ZIP pour chaque projet
- Statuts et dates de création

## 🛠️ Technologies

- **Frontend**: React 18 + Next.js 13
- **Styling**: Tailwind CSS + Inter font
- **Icons**: Heroicons + Lucide React
- **State Management**: React Hooks
- **WebSocket**: Native WebSocket API
- **Build Tool**: Next.js built-in

## 🚀 Installation

1. **Cloner le projet**
   ```bash
   cd dashboard
   ```

2. **Installer les dépendances**
   ```bash
   npm install
   ```

3. **Lancer en mode développement**
   ```bash
   npm run dev
   ```

4. **Ouvrir dans le navigateur**
   ```
   http://localhost:3000
   ```

## 📁 Structure du Projet

```
dashboard/
├── components/          # Composants réutilisables
│   ├── Layout.jsx      # Layout principal avec sidebar et topbar
│   ├── Sidebar.jsx     # Navigation latérale
│   ├── Topbar.jsx      # Barre supérieure
│   ├── Toast.jsx       # Notifications
│   ├── LogStream.jsx   # Stream de logs WebSocket
│   └── RoadmapCard.jsx # Carte d'épic
├── pages/              # Pages Next.js
│   ├── index.jsx       # Page d'accueil
│   ├── logs.jsx        # Page des logs
│   ├── roadmap.jsx     # Page de la roadmap
│   ├── startups.jsx    # Page des startups
│   ├── _app.js         # Configuration Next.js
│   └── _document.js    # Document HTML
├── styles/             # Styles CSS
│   └── globals.css     # Styles globaux + Tailwind
├── utils/              # Utilitaires (à venir)
├── package.json        # Dépendances et scripts
├── tailwind.config.js  # Configuration Tailwind
├── postcss.config.js   # Configuration PostCSS
└── next.config.js      # Configuration Next.js

# 🚀 Startup Factory Dashboard

Un dashboard React moderne et élégant pour la Startup Factory, construit avec **Vite**, **React 18**, et **Tailwind CSS**.

## ✨ Features

- 🎨 **Design SaaS US moderne** avec Tailwind CSS
- 📱 **Interface responsive** et intuitive
- 🔄 **Gestion d'état** avec React Hooks
- 📊 **Affichage de roadmap** avec cartes visuelles
- 📝 **Stream de logs** en temps réel
- 🎯 **Formulaire d'idée** pour lancer de nouvelles startups

## 🛠️ Technologies

- **Frontend**: React 18 + Vite
- **Styling**: Tailwind CSS
- **Icons**: React Icons
- **Fonts**: Inter (Google Fonts)

## 🚀 Installation

1. **Cloner le projet** :
```bash
cd dashboard
```

2. **Installer les dépendances** :
```bash
npm install
```

3. **Lancer en mode développement** :
```bash
npm run dev
```

4. **Ouvrir dans le navigateur** :
```
http://localhost:5173
```

## 📁 Structure du projet

```
dashboard/
├── src/
│   ├── components/
│   │   ├── Sidebar.jsx      # Navigation latérale
│   │   ├── Topbar.jsx       # En-tête avec profil
│   │   ├── RoadmapCard.jsx  # Carte d'épic roadmap
│   │   └── LogStream.jsx    # Terminal de logs
│   ├── App.jsx              # Composant principal
│   ├── main.jsx             # Point d'entrée
│   └── index.css            # Styles Tailwind
├── package.json
├── vite.config.js
├── tailwind.config.js
└── postcss.config.js
```

## 🔧 Configuration

### Tailwind CSS
Le projet utilise Tailwind CSS avec une configuration personnalisée :
- Couleur d'accent : `#2563EB` (bleu)
- Fond principal : `#F9FAFB` (gris clair)
- Police : Inter (Google Fonts)
- Animations : transitions et hover effects

### WebSocket
Le composant LogStream se connecte automatiquement à :
```
ws://localhost:8000/ws/logs
```

## 🌐 API Endpoints

### POST `/create-startup`
- **Body**: `{ "idea": "Description de votre startup" }`
- **Response**: Redirection vers `/roadmap`

### GET `/projects`
- **Response**: Liste des startups sauvegardées
- **Format**: `[{ id, idea, created_at, status, estimated_hours }]`

## 🎨 Composants UI

### Layout
- Sidebar fixe à gauche (256px)
- Topbar fixe en haut (64px)
- Contenu principal avec padding et marges

### Cards
- Fond blanc avec ombres
- Coins arrondis (`rounded-2xl`)
- Hover effects avec `hover:shadow-xl`
- Transitions fluides

### Boutons
- **Primary**: Bleu avec hover effects
- **Secondary**: Blanc avec bordure
- Animations : `hover:scale-105`

## 📱 Responsive Design

Le dashboard est optimisé pour :
- **Desktop** : Layout complet avec sidebar
- **Tablet** : Sidebar adaptée
- **Mobile** : Navigation mobile (à implémenter)

## 🔌 Intégration Backend

### Core Engine
Pour une intégration complète, votre backend doit implémenter :

1. **WebSocket `/ws/logs`**
   ```python
   # Exemple Python avec FastAPI
   @app.websocket("/ws/logs")
   async def websocket_endpoint(websocket: WebSocket):
       await websocket.accept()
       # Envoyer les logs des agents IA
   ```

2. **API `/projects`**
   ```python
   @app.get("/projects")
   async def get_projects():
       # Retourner la liste des startups
       return projects
   ```

## 🚀 Déploiement

### Vercel (Recommandé)
```bash
npm run build
vercel --prod
```

### Docker
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["npm", "start"]
```

## 🎯 Roadmap Future

- [ ] Authentification utilisateur
- [ ] Gestion des rôles (Admin/User)
- [ ] Notifications push
- [ ] Export PDF des roadmaps
- [ ] Intégration avec Git
- [ ] Analytics et métriques
- [ ] Mode sombre
- [ ] Internationalisation (i18n)

## 🤝 Contribution

1. Fork le projet
2. Créer une branche feature
3. Commit vos changements
4. Push vers la branche
5. Ouvrir une Pull Request

## 📄 Licence

MIT License - voir le fichier `LICENSE` pour plus de détails.

---

**Développé avec ❤️ par l'équipe ShipFast**
Le dashboard utilise Tailwind CSS pour un design moderne et responsive. La configuration se trouve dans `tailwind.config.js`.

### Vite
Configuration de build optimisée avec le plugin React dans `vite.config.js`.

## 🎯 Utilisation

1. **Saisir une idée** dans le champ de texte
2. **Cliquer sur "Lancer"** pour créer une startup
3. **Visualiser la roadmap** générée automatiquement
4. **Suivre les logs** en temps réel dans le terminal

## 🔌 API Backend

Le dashboard se connecte à l'API backend sur `http://localhost:8000` :

- **Endpoint** : `POST /create-startup`
- **Body** : `{ "idea": "description de l'idée" }`
- **Response** : `{ "roadmap": { "epics": [...] } }`

## 🚀 Build Production

```bash
npm run build
```

Les fichiers optimisés seront générés dans le dossier `dist/`.

## 📱 Responsive Design

Le dashboard s'adapte automatiquement à toutes les tailles d'écran :
- **Desktop** : Sidebar fixe + contenu principal
- **Tablet** : Layout adaptatif avec grille responsive
- **Mobile** : Interface optimisée pour petits écrans

## 🎨 Personnalisation

### Couleurs
Modifiez les classes Tailwind dans les composants pour changer le thème :
- **Primary** : `text-blue-600`, `bg-blue-600`
- **Background** : `bg-gray-100`, `bg-white`
- **Shadows** : `shadow-md`, `shadow-xl`

### Typography
La police Inter est configurée par défaut. Modifiez `index.css` pour changer.

## 🔍 Développement

### Hot Reload
Vite offre un hot reload automatique pour le développement.

### ESLint
Configuration ESLint incluse pour la qualité du code.

## 📄 Licence

MIT License - Libre d'utilisation et de modification.

---

**Développé avec ❤️ pour la Startup Factory**
