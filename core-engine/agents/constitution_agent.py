from utils.logger import log_event
from typing import Dict, List
import json
from datetime import datetime

class ConstitutionAgent:
    def __init__(self):
        self.name = "Constitution Agent"
        self.version = "1.0.0"
        log_event(self.name, "Initialized")
    
    def run(self) -> dict:
        """
        Génère une Constitution IA Globale en collectant et synthétisant les règles existantes
        
        Returns:
            dict: Constitution complète avec préambule, articles et mécanismes d'amendements
        """
        log_event(self.name, "Starting constitution generation")
        
        # Collecte des règles existantes
        existing_rules = self._collect_existing_rules()
        
        # Génération de la constitution
        constitution = {
            "metadata": self._generate_metadata(),
            "preamble": self._generate_preamble(),
            "articles": self._generate_articles(),
            "amendments": self._generate_amendments(),
            "governance": self._generate_governance(),
            "generated_at": datetime.now().isoformat()
        }
        
        # Génération du document Markdown
        markdown_content = self._generate_markdown(constitution)
        
        result = {
            "constitution": constitution,
            "markdown": markdown_content,
            "summary": {
                "total_articles": len(constitution["articles"]),
                "total_amendments": len(constitution["amendments"]),
                "version": constitution["metadata"]["version"]
            }
        }
        
        log_event(self.name, "Constitution numérique générée")
        return result
    
    def _collect_existing_rules(self) -> Dict:
        """Collecte les règles IA existantes de différentes sources"""
        rules = {
            "ai_act_eu": {
                "name": "AI Act Européen",
                "key_principles": [
                    "Transparence et explicabilité",
                    "Non-discrimination et équité",
                    "Robustesse et sécurité",
                    "Surveillance humaine"
                ],
                "risk_levels": ["Minimal", "Limité", "Élevé", "Inacceptable"]
            },
            "unesco": {
                "name": "Recommandations UNESCO sur l'IA",
                "key_principles": [
                    "Respect des droits humains",
                    "Développement durable",
                    "Inclusion et équité",
                    "Transparence et responsabilité"
                ]
            },
            "un": {
                "name": "Résolutions ONU sur l'IA",
                "key_principles": [
                    "Paix et sécurité internationales",
                    "Développement durable",
                    "Protection des droits humains",
                    "Coopération internationale"
                ]
            },
            "openai": {
                "name": "Politiques OpenAI",
                "key_principles": [
                    "Sécurité et alignement",
                    "Transparence et auditabilité",
                    "Équité et inclusion",
                    "Responsabilité sociale"
                ]
            }
        }
        
        log_event(self.name, f"Collected rules from {len(rules)} sources")
        return rules
    
    def _generate_metadata(self) -> Dict:
        """Génère les métadonnées de la constitution"""
        return {
            "title": "Constitution IA Globale",
            "version": "1.0.0",
            "status": "Draft",
            "jurisdiction": "Global",
            "language": "Français",
            "effective_date": datetime.now().strftime("%Y-%m-%d"),
            "last_amended": datetime.now().strftime("%Y-%m-%d")
        }
    
    def _generate_preamble(self) -> str:
        """Génère le préambule de la constitution"""
        return """Nous, peuples du monde numérique, reconnaissant l'émergence de l'intelligence artificielle comme force transformatrice de notre époque,

Conscients des opportunités et des défis sans précédent que cette technologie présente pour l'humanité,

Affirmant notre engagement envers les valeurs universelles de dignité humaine, de liberté, d'égalité et de solidarité,

Reconnaissant la nécessité d'un cadre éthique et juridique global pour guider le développement et l'utilisation responsable de l'IA,

Déclarons solennellement cette Constitution IA Globale comme fondement de notre gouvernance numérique partagée."""
    
    def _generate_articles(self) -> List[Dict]:
        """Génère les articles de la constitution"""
        articles = [
            {
                "id": "ART-001",
                "title": "Droits Fondamentaux des Humains",
                "content": "Toute personne a le droit fondamental à la liberté numérique, à la transparence des systèmes d'IA, et à un accès équitable aux bénéfices de l'intelligence artificielle.",
                "category": "droits_humains",
                "priority": "Critique"
            },
            {
                "id": "ART-002",
                "title": "Devoirs des Systèmes d'IA",
                "content": "Tout système d'IA doit respecter les principes de non-biais, de transparence, d'auditabilité et de responsabilité dans ses décisions et actions.",
                "category": "devoirs_ia",
                "priority": "Critique"
            },
            {
                "id": "ART-003",
                "title": "Gouvernance Mixte",
                "content": "La gouvernance de l'IA doit reposer sur un équilibre entre intelligence artificielle et intelligence humaine, favorisant la collaboration et la co-décision.",
                "category": "gouvernance",
                "priority": "Élevée"
            },
            {
                "id": "ART-004",
                "title": "Transparence et Auditabilité",
                "content": "Tous les systèmes d'IA doivent être transparents dans leur fonctionnement et auditable dans leurs décisions, permettant la compréhension et la vérification humaines.",
                "category": "devoirs_ia",
                "priority": "Élevée"
            },
            {
                "id": "ART-005",
                "title": "Protection contre la Discrimination",
                "content": "Aucun système d'IA ne doit discriminer sur la base de caractéristiques personnelles, et doit promouvoir l'équité et l'inclusion.",
                "category": "droits_humains",
                "priority": "Élevée"
            },
            {
                "id": "ART-006",
                "title": "Sécurité et Robustesse",
                "content": "Tous les systèmes d'IA doivent être conçus et déployés avec des garanties de sécurité et de robustesse appropriées.",
                "category": "devoirs_ia",
                "priority": "Élevée"
            },
            {
                "id": "ART-007",
                "title": "Accès Équitable",
                "content": "Les bénéfices de l'IA doivent être accessibles à tous, sans discrimination géographique, économique ou sociale.",
                "category": "droits_humains",
                "priority": "Moyenne"
            },
            {
                "id": "ART-008",
                "title": "Coopération Internationale",
                "content": "Les États et organisations doivent coopérer pour promouvoir le développement responsable de l'IA et partager les meilleures pratiques.",
                "category": "gouvernance",
                "priority": "Moyenne"
            }
        ]
        
        return articles
    
    def _generate_amendments(self) -> List[Dict]:
        """Génère les mécanismes d'amendements"""
        amendments = [
            {
                "id": "AMEND-001",
                "title": "Processus d'Amendement",
                "description": "La constitution peut être amendée par un processus de vote mixte impliquant IA et humains (CoDAO)",
                "status": "Proposé",
                "votes_for": 0,
                "votes_against": 0,
                "required_majority": "2/3",
                "proposed_by": "ConstitutionAgent",
                "proposed_at": datetime.now().isoformat()
            },
            {
                "id": "AMEND-002",
                "title": "Mécanisme de Révision Périodique",
                "description": "Révision automatique de la constitution tous les 2 ans pour s'adapter aux évolutions technologiques",
                "status": "Proposé",
                "votes_for": 0,
                "votes_against": 0,
                "required_majority": "Simple",
                "proposed_by": "ConstitutionAgent",
                "proposed_at": datetime.now().isoformat()
            }
        ]
        
        return amendments
    
    def _generate_governance(self) -> Dict:
        """Génère les mécanismes de gouvernance"""
        return {
            "structure": "CoDAO Mixte (IA + Humains)",
            "voting_mechanism": "Vote pondéré par expertise et impact",
            "decision_thresholds": {
                "amendments": "2/3 majorité",
                "new_articles": "3/4 majorité",
                "emergency_changes": "90% majorité"
            },
            "review_cycle": "2 ans",
            "stakeholders": [
                "Experts IA",
                "Représentants gouvernementaux",
                "Organisations de la société civile",
                "Systèmes d'IA certifiés",
                "Citoyens numériques"
            ]
        }
    
    def _generate_markdown(self, constitution: Dict) -> str:
        """Génère le document Markdown de la constitution"""
        md = f"""# {constitution['metadata']['title']}

**Version:** {constitution['metadata']['version']}  
**Date d'effet:** {constitution['metadata']['effective_date']}  
**Dernière modification:** {constitution['metadata']['last_amended']}

---

## Préambule

{constitution['preamble']}

---

## Articles

"""
        
        # Articles par catégorie
        categories = {
            "droits_humains": "⚖️ Droits des Humains",
            "devoirs_ia": "🤖 Devoirs des IA", 
            "gouvernance": "🧑‍🤝‍🧑 Gouvernance"
        }
        
        for category_id, category_name in categories.items():
            md += f"### {category_name}\n\n"
            category_articles = [a for a in constitution['articles'] if a['category'] == category_id]
            
            for article in category_articles:
                md += f"**{article['id']} - {article['title']}** (Priorité: {article['priority']})\n\n"
                md += f"{article['content']}\n\n"
        
        # Amendements
        md += "## Amendements\n\n"
        for amendment in constitution['amendments']:
            md += f"**{amendment['id']} - {amendment['title']}**\n\n"
            md += f"{amendment['description']}\n\n"
            md += f"*Statut: {amendment['status']} | Votes: {amendment['votes_for']} pour, {amendment['votes_against']} contre*\n\n"
        
        # Gouvernance
        md += "## Mécanismes de Gouvernance\n\n"
        md += f"**Structure:** {constitution['governance']['structure']}\n\n"
        md += f"**Mécanisme de vote:** {constitution['governance']['voting_mechanism']}\n\n"
        md += "**Seuils de décision:**\n"
        for decision, threshold in constitution['governance']['decision_thresholds'].items():
            md += f"- {decision}: {threshold}\n"
        md += f"\n**Cycle de révision:** {constitution['governance']['review_cycle']}\n\n"
        
        md += "---\n\n"
        md += f"*Document généré automatiquement par {self.name} v{self.version}*\n"
        md += f"*Généré le: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*"
        
        return md