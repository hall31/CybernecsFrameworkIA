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