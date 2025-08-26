# Epic2 - Startup Creator avec Agents IA

## 🚀 Description

Système de création de startups automatisé utilisant des agents IA spécialisés :
- **CEOAgent** : Génère la roadmap business
- **CTOAgent** : Définit la stack technique et génère le scaffold du projet

## 🏗️ Architecture

```
core-engine/
├── agents/
│   ├── __init__.py
│   ├── base_agent.py      # Classe de base pour tous les agents
│   ├── ceo_agent.py       # Agent CEO pour la roadmap business
│   └── cto_agent.py       # Agent CTO pour la stack technique
├── __init__.py
main.py                     # Application Flask principale
requirements.txt            # Dépendances Python
generated/                  # Scaffold généré (créé automatiquement)
```

## 🎯 Fonctionnalités

### CEOAgent
- Analyse l'idée de startup
- Génère une roadmap business complète
- Définit le modèle économique, marché cible, fonctionnalités clés

### CTOAgent
- Définit la stack technique (Laravel + React + PostgreSQL)
- Génère automatiquement les fichiers Docker
- Crée le scaffold du projet dans `/generated`

## 🚀 Installation et Utilisation

### 1. Installation des dépendances
```bash
pip install -r requirements.txt
```

### 2. Lancement de l'application
```bash
python main.py
```

L'application sera accessible sur `http://localhost:5000`

### 3. Création d'une startup

#### Endpoint : `POST /create-startup`

**Exemple de requête :**
```bash
curl -X POST http://localhost:5000/create-startup \
  -H "Content-Type: application/json" \
  -d '{"idea": "SaaS e-commerce"}'
```

**Réponse attendue :**
```json
{
  "success": true,
  "idea": "SaaS e-commerce",
  "roadmap": {
    "idea": "SaaS e-commerce",
    "business_model": "SaaS",
    "target_market": "E-commerce",
    "revenue_streams": ["subscription", "transaction_fees"],
    "key_features": [
      "Gestion des produits",
      "Panier d'achat",
      "Système de paiement",
      "Dashboard admin",
      "Analytics"
    ],
    "timeline": {
      "phase_1": "MVP - 3 mois",
      "phase_2": "Beta - 6 mois",
      "phase_3": "Launch - 9 mois"
    },
    "team_size": "5-10 personnes",
    "budget": "100k-500k EUR"
  },
  "technical_stack": {
    "stack": "Laravel + React + PostgreSQL",
    "services": ["backend", "frontend", "db"],
    "files": ["docker-compose.yml", "backend/Dockerfile", "frontend/Dockerfile"]
  },
  "message": "Startup créée avec succès! Consultez le dossier /generated pour le scaffold du projet."
}
```

### 4. Vérification de santé
```bash
curl http://localhost:5000/health
```

## 📁 Fichiers Générés

Après l'exécution, le dossier `/generated` contiendra :

```
generated/
├── docker-compose.yml      # Orchestration des services
├── backend/
│   └── Dockerfile         # Container PHP/Laravel
└── frontend/
    └── Dockerfile         # Container Node.js/React
```

### Docker Compose
- **Backend** : Port 9000 (Laravel)
- **Frontend** : Port 3000 (React)
- **Database** : Port 5432 (PostgreSQL)

## 🔧 Configuration

### Variables d'environnement
- `POSTGRES_USER`: admin (par défaut)
- `POSTGRES_PASSWORD`: secret (par défaut)
- `POSTGRES_DB`: appdb (par défaut)

### Ports
- Application Flask : 5000
- Backend Laravel : 9000
- Frontend React : 3000
- PostgreSQL : 5432

## 📊 Logs

Tous les événements sont loggés avec :
- Timestamp
- Nom de l'agent
- Message détaillé

Exemples de logs :
```
[CEOAgent] Démarrage de l'analyse de l'idée: SaaS e-commerce
[CEOAgent] Roadmap business générée avec succès
[CTOAgent] Démarrage de la génération de la stack technique
[CTOAgent] Docker-compose généré
[CTOAgent] Backend Dockerfile généré
[CTOAgent] Frontend Dockerfile généré
[CTOAgent] Stack technique générée avec succès
```

## 🚀 Démarrage Rapide

1. **Cloner et installer :**
```bash
pip install -r requirements.txt
```

2. **Lancer l'application :**
```bash
python main.py
```

3. **Créer une startup :**
```bash
curl -X POST http://localhost:5000/create-startup \
  -H "Content-Type: application/json" \
  -d '{"idea": "Mon idée de startup"}'
```

4. **Vérifier les fichiers générés :**
```bash
ls -la generated/
```

## 🔍 Dépannage

### Erreur d'import
Si vous rencontrez des erreurs d'import, vérifiez que la structure des dossiers est correcte et que tous les `__init__.py` sont présents.

### Ports déjà utilisés
Si les ports sont déjà utilisés, modifiez les configurations dans `main.py` et `cto_agent.py`.

### Permissions
Assurez-vous d'avoir les permissions d'écriture pour créer le dossier `generated/`.

## 🤝 Contribution

Pour contribuer :
1. Fork le projet
2. Créer une branche feature
3. Implémenter les améliorations
4. Tester avec différents cas d'usage
5. Soumettre une pull request

## 📄 Licence

Ce projet est sous licence MIT.
