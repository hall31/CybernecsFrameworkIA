import os
import json
from typing import Dict, Any, Optional
from agents.base_agent import BaseAgent

class AdsAgent(BaseAgent):
    """Agent pour la gestion des campagnes publicitaires et acquisition clients"""
    
    def __init__(self):
        super().__init__()
        self.linkedin_client_id = os.getenv('LINKEDIN_CLIENT_ID')
        self.linkedin_client_secret = os.getenv('LINKEDIN_CLIENT_SECRET')
        self.linkedin_access_token = os.getenv('LINKEDIN_ACCESS_TOKEN')
        
        self.google_ads_client_id = os.getenv('GOOGLE_ADS_CLIENT_ID')
        self.google_ads_client_secret = os.getenv('GOOGLE_ADS_CLIENT_SECRET')
        self.google_ads_developer_token = os.getenv('GOOGLE_ADS_DEVELOPER_TOKEN')
        self.google_ads_refresh_token = os.getenv('GOOGLE_ADS_REFRESH_TOKEN')
    
    def run(self, idea: str, growth: Dict[str, Any]) -> Dict[str, Any]:
        """Lance une campagne publicitaire automatique"""
        try:
            self.log_event("AdsAgent", "Démarrage de la campagne publicitaire", {"idea": idea, "growth": growth})
            
            # 1. Analyser l'idée et la stratégie de croissance
            campaign_strategy = self._analyze_campaign_strategy(idea, growth)
            
            # 2. Choisir la plateforme la plus appropriée
            platform_choice = self._choose_advertising_platform(idea, growth)
            
            # 3. Créer la campagne sur la plateforme choisie
            if platform_choice == "linkedin":
                campaign_result = self._create_linkedin_campaign(idea, campaign_strategy)
            elif platform_choice == "google":
                campaign_result = self._create_google_ads_campaign(idea, campaign_strategy)
            else:
                # Fallback sur LinkedIn par défaut
                campaign_result = self._create_linkedin_campaign(idea, campaign_strategy)
            
            result = {
                "ads_platform": platform_choice,
                "campaign_id": campaign_result.get("campaign_id", "camp_auto_" + str(hash(idea))[:8]),
                "status": campaign_result.get("status", "active"),
                "strategy": campaign_strategy,
                "budget": campaign_result.get("budget", "50€/jour"),
                "targeting": campaign_result.get("targeting", {}),
                "cta": campaign_result.get("cta", "Démarrer gratuitement")
            }
            
            self.log_event("AdsAgent", "Campagne publicitaire lancée", result)
            return result
            
        except Exception as e:
            return self.handle_error(e, f"Lancement de campagne pour l'idée: {idea}")
    
    def _analyze_campaign_strategy(self, idea: str, growth: Dict[str, Any]) -> Dict[str, Any]:
        """Analyse l'idée et la stratégie de croissance pour définir la campagne"""
        strategy = {
            "target_audience": [],
            "key_messages": [],
            "cta": "Démarrer gratuitement",
            "budget_recommendation": "50€/jour",
            "duration": "30 jours"
        }
        
        # Analyser le type d'idée pour définir l'audience cible
        if "marketplace" in idea.lower():
            strategy["target_audience"] = [
                "Entrepreneurs B2B",
                "Directeurs Marketing",
                "Chefs de produit"
            ]
            strategy["key_messages"] = [
                "Connectez acheteurs et vendeurs",
                "Croissance rapide de votre business",
                "Plateforme clé en main"
            ]
            strategy["cta"] = "Lancer votre marketplace"
            
        elif "ai" in idea.lower() or "intelligence" in idea.lower():
            strategy["target_audience"] = [
                "Data Scientists",
                "Chefs de projet IT",
                "Directeurs Innovation"
            ]
            strategy["key_messages"] = [
                "Automatisez vos processus",
                "IA accessible à tous",
                "Gain de productivité immédiat"
            ]
            strategy["cta"] = "Tester l'IA gratuitement"
            
        elif "analytics" in idea.lower() or "data" in idea.lower():
            strategy["target_audience"] = [
                "Analystes de données",
                "Directeurs Marketing",
                "Chefs de produit"
            ]
            strategy["key_messages"] = [
                "Prenez des décisions éclairées",
                "Analytics en temps réel",
                "ROI mesurable"
            ]
            strategy["cta"] = "Voir la démo"
            
        else:
            # Stratégie générique pour SaaS
            strategy["target_audience"] = [
                "Professionnels B2B",
                "Petites et moyennes entreprises",
                "Startups en croissance"
            ]
            strategy["key_messages"] = [
                "Solution SaaS complète",
                "Démarrage en 5 minutes",
                "Support expert inclus"
            ]
            strategy["cta"] = "Commencer l'essai gratuit"
        
        # Adapter selon la stratégie de croissance
        if growth.get("channel") == "content_marketing":
            strategy["budget_recommendation"] = "30€/jour"
            strategy["duration"] = "45 jours"
        elif growth.get("channel") == "paid_ads":
            strategy["budget_recommendation"] = "100€/jour"
            strategy["duration"] = "21 jours"
        elif growth.get("channel") == "social_media":
            strategy["budget_recommendation"] = "40€/jour"
            strategy["duration"] = "30 jours"
        
        return strategy
    
    def _choose_advertising_platform(self, idea: str, growth: Dict[str, Any]) -> str:
        """Choisit la plateforme publicitaire la plus appropriée"""
        # Logique de sélection basée sur l'idée et la stratégie
        if "b2b" in idea.lower() or "enterprise" in idea.lower():
            return "linkedin"  # LinkedIn pour B2B
        elif "mobile" in idea.lower() or "app" in idea.lower():
            return "google"     # Google Ads pour mobile
        elif "local" in idea.lower() or "geolocalisation" in idea.lower():
            return "google"     # Google Ads pour local
        else:
            # Par défaut, LinkedIn pour SaaS B2B
            return "linkedin"
    
    def _create_linkedin_campaign(self, idea: str, strategy: Dict[str, Any]) -> Dict[str, Any]:
        """Crée une campagne LinkedIn Ads"""
        try:
            # Simulation de création de campagne LinkedIn
            # En production, utiliser l'API LinkedIn Ads officielle
            
            campaign_data = {
                "campaign_id": f"camp_linkedin_{str(hash(idea))[:8]}",
                "status": "active",
                "budget": strategy["budget_recommendation"],
                "targeting": {
                    "locations": ["France", "Belgique", "Suisse"],
                    "industries": ["Technology", "Marketing", "Business Services"],
                    "job_titles": strategy["target_audience"],
                    "company_size": ["1-10", "11-50", "51-200"]
                },
                "ad_creative": {
                    "headline": f"🚀 {idea[:50]}...",
                    "description": strategy["key_messages"][0] if strategy["key_messages"] else "Solution SaaS innovante",
                    "cta": strategy["cta"],
                    "image_url": "https://via.placeholder.com/1200x627/3B82F6/FFFFFF?text=Startup+SaaS"
                }
            }
            
            self.log_event("AdsAgent", "Campagne LinkedIn créée", campaign_data)
            return campaign_data
            
        except Exception as e:
            self.logger.error(f"Erreur lors de la création de la campagne LinkedIn: {e}")
            return {
                "campaign_id": "error",
                "status": "error",
                "error": str(e)
            }
    
    def _create_google_ads_campaign(self, idea: str, strategy: Dict[str, Any]) -> Dict[str, Any]:
        """Crée une campagne Google Ads"""
        try:
            # Simulation de création de campagne Google Ads
            # En production, utiliser l'API Google Ads officielle
            
            campaign_data = {
                "campaign_id": f"camp_google_{str(hash(idea))[:8]}",
                "status": "active",
                "budget": strategy["budget_recommendation"],
                "targeting": {
                    "keywords": self._generate_keywords(idea),
                    "locations": ["France"],
                    "languages": ["French"],
                    "audiences": ["In-market", "Affinity"]
                },
                "ad_creative": {
                    "headline1": f"🚀 {idea[:30]}...",
                    "headline2": strategy["key_messages"][0][:30] if strategy["key_messages"] else "Solution SaaS innovante",
                    "headline3": strategy["cta"],
                    "description": strategy["key_messages"][1] if len(strategy["key_messages"]) > 1 else "Démarrez en 5 minutes",
                    "final_url": "https://yourdomain.com"
                }
            }
            
            self.log_event("AdsAgent", "Campagne Google Ads créée", campaign_data)
            return campaign_data
            
        except Exception as e:
            self.logger.error(f"Erreur lors de la création de la campagne Google Ads: {e}")
            return {
                "campaign_id": "error",
                "status": "error",
                "error": str(e)
            }
    
    def _generate_keywords(self, idea: str) -> list:
        """Génère des mots-clés pertinents pour Google Ads"""
        base_keywords = [
            "saas",
            "startup",
            "outil",
            "plateforme",
            "solution"
        ]
        
        idea_keywords = idea.lower().split()
        idea_keywords = [word for word in idea_keywords if len(word) > 3]
        
        # Combiner les mots-clés de base avec ceux de l'idée
        all_keywords = base_keywords + idea_keywords[:5]
        
        # Ajouter des variations
        variations = []
        for keyword in all_keywords:
            variations.extend([
                keyword,
                f"{keyword} gratuit",
                f"{keyword} essai",
                f"meilleur {keyword}",
                f"{keyword} 2024"
            ])
        
        return variations[:20]  # Limiter à 20 mots-clés
    
    def get_campaign_status(self, campaign_id: str) -> Dict[str, Any]:
        """Récupère le statut d'une campagne"""
        try:
            # Simulation de récupération du statut
            # En production, appeler l'API de la plateforme
            return {
                "campaign_id": campaign_id,
                "status": "active",
                "impressions": 1250,
                "clicks": 45,
                "ctr": "3.6%",
                "spend": "€125.50",
                "conversions": 3
            }
        except Exception as e:
            return self.handle_error(e, f"Récupération du statut pour campaign_id: {campaign_id}")
    
    def pause_campaign(self, campaign_id: str) -> Dict[str, Any]:
        """Met en pause une campagne"""
        try:
            # Simulation de pause de campagne
            return {
                "campaign_id": campaign_id,
                "status": "paused",
                "action": "paused",
                "timestamp": "2024-01-15T10:30:00Z"
            }
        except Exception as e:
            return self.handle_error(e, f"Pause de campagne pour campaign_id: {campaign_id}")
    
    def update_campaign_budget(self, campaign_id: str, new_budget: str) -> Dict[str, Any]:
        """Met à jour le budget d'une campagne"""
        try:
            return {
                "campaign_id": campaign_id,
                "old_budget": "50€/jour",
                "new_budget": new_budget,
                "status": "updated",
                "timestamp": "2024-01-15T10:30:00Z"
            }
        except Exception as e:
            return self.handle_error(e, f"Mise à jour du budget pour campaign_id: {campaign_id}")