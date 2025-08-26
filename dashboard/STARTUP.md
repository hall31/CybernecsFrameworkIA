# 🚀 Démarrage Rapide - Dashboard d'Orchestration

## ⚡ Démarrage en 3 étapes

### 1️⃣ Lancer le Dashboard
```bash
cd dashboard
npm run dev
```
📍 **Dashboard accessible sur :** http://localhost:5173

### 2️⃣ Lancer l'API (Optionnel - pour tester avec une vraie API)
```bash
cd dashboard
pip install -r requirements.txt
python demo_api.py
```
🔌 **API accessible sur :** http://localhost:8000

### 3️⃣ Naviguer vers Orchestration
- Ouvrez http://localhost:5173
- Cliquez sur "Orchestration" dans la sidebar
- 🎉 Votre dashboard est prêt !

## 🔧 Modes de Fonctionnement

### Mode Développement (Par défaut)
- ✅ Utilise les données de test (`mockData.js`)
- ✅ Fonctionne sans API backend
- ✅ Simulation des interactions
- ✅ Parfait pour le développement

### Mode Production
- 🔌 Se connecte à votre API backend
- 🔌 Endpoints réels : `/agents`, `/epics`
- 🔌 Actions réelles : toggle, run
- 🔌 Données en temps réel

## 📱 Fonctionnalités à Tester

### 🤖 Agents
- [ ] Voir la liste des 5 agents
- [ ] Toggle ON/OFF avec les switches
- [ ] Observer les changements de statut
- [ ] Voir les badges colorés

### 📋 Épics
- [ ] Voir la liste des 6 épics
- [ ] Toggle ON/OFF des épics
- [ ] Cliquer sur "Run" pour exécuter
- [ ] Observer les changements de statut

### 🔄 Actions Globales
- [ ] Bouton "Rafraîchir" pour synchroniser
- [ ] Gestion des erreurs
- [ ] États de chargement
- [ ] Interface responsive

## 🎯 URLs Importantes

| Service | URL | Description |
|---------|-----|-------------|
| **Dashboard** | http://localhost:5173 | Interface principale |
| **Orchestration** | http://localhost:5173/#/orchestration | Page d'orchestration |
| **API Demo** | http://localhost:8000 | API de test |
| **API Docs** | http://localhost:8000/docs | Documentation Swagger |

## 🚨 Dépannage

### Dashboard ne se charge pas
```bash
# Vérifier les dépendances
npm install

# Redémarrer le serveur
npm run dev
```

### API ne répond pas
```bash
# Vérifier Python et pip
python --version
pip --version

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'API
python demo_api.py
```

### Erreurs CORS
- ✅ L'API est configurée pour accepter localhost:5173
- ✅ Vérifiez que l'API tourne sur le port 8000
- ✅ Redémarrez l'API après modification

## 🎨 Personnalisation

### Modifier les Données de Test
Éditez `src/mockData.js` :
```javascript
export const mockAgents = [
  {
    name: "Mon-Agent",
    enabled: true,
    status: "active"
  }
  // ... ajoutez vos agents
];
```

### Changer les Couleurs
Modifiez les composants `AgentCard.jsx` et `EpicCard.jsx` :
```javascript
const statusColors = {
  active: "bg-green-100 text-green-700", // Changez ici
  // ...
};
```

### Ajouter de Nouveaux Statuts
```javascript
const statusConfig = {
  // ... statuts existants
  newStatus: { 
    color: "bg-purple-100 text-purple-700", 
    icon: "🟣", 
    label: "Nouveau Statut" 
  }
};
```

## 🔮 Prochaines Étapes

1. **Intégrer avec votre API réelle**
   - Modifiez les URLs dans `Orchestration.jsx`
   - Configurez l'authentification si nécessaire

2. **Ajouter des fonctionnalités**
   - Notifications en temps réel
   - Graphiques de performance
   - Logs détaillés

3. **Déployer en production**
   - Build : `npm run build`
   - Serveur : Nginx, Apache, ou Vercel/Netlify

---

## 🎉 Félicitations !

Votre dashboard d'orchestration est maintenant opérationnel ! 

**Prochain objectif :** Connectez-le à votre vraie infrastructure et gérez vos agents et épics en production ! 🚀

---

**Besoin d'aide ?** Consultez `README_ORCHESTRATION.md` pour plus de détails.