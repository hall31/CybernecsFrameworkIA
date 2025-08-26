import os
import logging
from typing import Dict, Any
from datetime import datetime

class LegalAgent:
    """Agent spécialisé dans la génération de documents légaux"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.legal_dir = "generated/legal"
        
        # Créer le répertoire s'il n'existe pas
        os.makedirs(self.legal_dir, exist_ok=True)
    
    def run(self, idea: str) -> Dict[str, Any]:
        """
        Génère tous les documents légaux nécessaires
        
        Args:
            idea (str): Description de l'idée de startup
            
        Returns:
            Dict contenant la liste des fichiers générés
        """
        try:
            # Log de l'événement
            self.logger.info(f"LegalAgent: Documents légaux générés pour l'idée: {idea}")
            
            # Génération des documents
            generated_files = []
            
            # CGU
            cgu_content = self._generate_cgu(idea)
            cgu_file = os.path.join(self.legal_dir, "cgu.md")
            with open(cgu_file, 'w', encoding='utf-8') as f:
                f.write(cgu_content)
            generated_files.append("cgu.md")
            
            # CGV
            cgv_content = self._generate_cgv(idea)
            cgv_file = os.path.join(self.legal_dir, "cgv.md")
            with open(cgv_file, 'w', encoding='utf-8') as f:
                f.write(cgv_content)
            generated_files.append("cgv.md")
            
            # Politique de confidentialité
            privacy_content = self._generate_privacy(idea)
            privacy_file = os.path.join(self.legal_dir, "privacy.md")
            with open(privacy_file, 'w', encoding='utf-8') as f:
                f.write(privacy_content)
            generated_files.append("privacy.md")
            
            # Mentions légales
            mentions_content = self._generate_mentions(idea)
            mentions_file = os.path.join(self.legal_dir, "mentions.md")
            with open(mentions_file, 'w', encoding='utf-8') as f:
                f.write(mentions_content)
            generated_files.append("mentions.md")
            
            return {
                "generated_files": generated_files,
                "legal_dir": self.legal_dir,
                "generated_at": datetime.now().isoformat(),
                "status": "success"
            }
            
        except Exception as e:
            self.logger.error(f"Erreur dans LegalAgent: {str(e)}")
            return {
                "error": f"Erreur lors de la génération des documents légaux: {str(e)}",
                "generated_files": [],
                "status": "error"
            }
    
    def _generate_cgu(self, idea: str) -> str:
        """Génère les Conditions Générales d'Utilisation"""
        return f"""# Conditions Générales d'Utilisation

## Article 1 - Objet

Les présentes CGU régissent l'utilisation du service {idea} proposé par [Nom de la Société].

## Article 2 - Définitions

- **Service** : L'application {idea} accessible via internet
- **Utilisateur** : Toute personne utilisant le Service
- **Compte** : L'ensemble des informations fournies par l'Utilisateur

## Article 3 - Acceptation des conditions

L'utilisation du Service implique l'acceptation pleine et entière des présentes CGU.

## Article 4 - Inscription et compte

L'Utilisateur doit créer un compte pour accéder aux fonctionnalités du Service.

## Article 5 - Utilisation du service

L'Utilisateur s'engage à utiliser le Service conformément à sa destination.

## Article 6 - Responsabilité

[Nom de la Société] ne saurait être tenue responsable des dommages indirects.

## Article 7 - Droit applicable

Les présentes CGU sont soumises au droit français.

*Généré automatiquement le {datetime.now().strftime('%d/%m/%Y')}*
"""

    def _generate_cgv(self, idea: str) -> str:
        """Génère les Conditions Générales de Vente"""
        return f"""# Conditions Générales de Vente

## Article 1 - Objet

Les présentes CGV s'appliquent à la vente de services proposés par {idea}.

## Article 2 - Prix

Les prix sont exprimés en euros et hors taxes. La TVA applicable est de 20%.

## Article 3 - Commande

La commande est ferme dès réception de la confirmation par email.

## Article 4 - Paiement

Le paiement s'effectue par carte bancaire ou virement bancaire.

## Article 5 - Livraison

La prestation est livrée dans les délais indiqués lors de la commande.

## Article 6 - Rétractation

Droit de rétractation de 14 jours à compter de la commande.

## Article 7 - Garantie

Garantie légale de conformité et de vices cachés.

*Généré automatiquement le {datetime.now().strftime('%d/%m/%Y')}*
"""

    def _generate_privacy(self, idea: str) -> str:
        """Génère la Politique de Confidentialité"""
        return f"""# Politique de Confidentialité

## Collecte des données

{idea} collecte les données suivantes :
- Informations d'identification
- Données de connexion
- Données d'utilisation

## Utilisation des données

Les données collectées sont utilisées pour :
- Fournir le service
- Améliorer l'expérience utilisateur
- Communiquer avec l'utilisateur

## Partage des données

Aucune donnée personnelle n'est vendue à des tiers.

## Sécurité

Mise en place de mesures de sécurité appropriées.

## Droits de l'utilisateur

Droit d'accès, de rectification et de suppression des données.

## Cookies

Utilisation de cookies pour améliorer le service.

*Généré automatiquement le {datetime.now().strftime('%d/%m/%Y')}*
"""

    def _generate_mentions(self, idea: str) -> str:
        """Génère les Mentions Légales"""
        return f"""# Mentions Légales

## Éditeur

**Raison sociale** : [Nom de la Société]  
**Forme juridique** : SAS  
**Capital social** : [Montant] €  
**Siège social** : [Adresse]  
**SIRET** : [Numéro SIRET]  
**TVA intracommunautaire** : [Numéro TVA]

## Directeur de publication

[Nom du directeur de publication]

## Hébergement

**Hébergeur** : [Nom de l'hébergeur]  
**Adresse** : [Adresse de l'hébergeur]

## Contact

**Email** : contact@{idea.lower().replace(' ', '')}.com  
**Téléphone** : [Numéro de téléphone]

## Propriété intellectuelle

L'ensemble du contenu de {idea} est protégé par le droit d'auteur.

*Généré automatiquement le {datetime.now().strftime('%d/%m/%Y')}*
"""