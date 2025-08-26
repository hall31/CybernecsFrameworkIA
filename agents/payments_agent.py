import os
import stripe
from typing import Dict, Any, List
from agents.base_agent import BaseAgent

class PaymentsAgent(BaseAgent):
    """Agent pour la gestion des paiements et monétisation via Stripe"""
    
    def __init__(self):
        super().__init__()
        stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
        
        if not stripe.api_key:
            raise ValueError("Clé Stripe manquante dans les variables d'environnement")
    
    def run(self, idea: str) -> Dict[str, Any]:
        """Configure la monétisation pour l'idée de startup"""
        try:
            self.log_event("PaymentsAgent", "Démarrage de la configuration des paiements", {"idea": idea})
            
            # 1. Créer les plans de pricing selon l'idée
            plans = self._create_pricing_plans(idea)
            
            # 2. Créer les produits Stripe
            stripe_products = self._create_stripe_products(plans)
            
            # 3. Créer les prix Stripe
            stripe_prices = self._create_stripe_prices(stripe_products, plans)
            
            # 4. Créer une page de checkout
            checkout_session = self._create_checkout_session(stripe_prices)
            
            result = {
                "stripe_plans": stripe_prices,
                "checkout_url": checkout_session.url,
                "session_id": checkout_session.id,
                "status": "configured"
            }
            
            self.log_event("PaymentsAgent", "Plans Stripe configurés", result)
            return result
            
        except Exception as e:
            return self.handle_error(e, f"Configuration des paiements pour l'idée: {idea}")
    
    def _create_pricing_plans(self, idea: str) -> List[Dict[str, Any]]:
        """Crée des plans de pricing adaptés à l'idée"""
        # Plans par défaut adaptés au type de SaaS
        if "marketplace" in idea.lower():
            plans = [
                {
                    "name": "Starter",
                    "price": 29,
                    "currency": "eur",
                    "interval": "month",
                    "features": ["Jusqu'à 100 utilisateurs", "Support email", "Analytics de base"],
                    "description": "Parfait pour démarrer votre marketplace"
                },
                {
                    "name": "Pro",
                    "price": 79,
                    "currency": "eur",
                    "interval": "month",
                    "features": ["Utilisateurs illimités", "Support prioritaire", "Analytics avancés", "API access"],
                    "description": "Pour les marketplaces en croissance"
                },
                {
                    "name": "Enterprise",
                    "price": 199,
                    "currency": "eur",
                    "interval": "month",
                    "features": ["Tout du plan Pro", "Support dédié", "SLA garanti", "Intégrations personnalisées"],
                    "description": "Solution sur mesure pour grandes entreprises"
                }
            ]
        elif "ai" in idea.lower() or "intelligence" in idea.lower():
            plans = [
                {
                    "name": "Starter",
                    "price": 39,
                    "currency": "eur",
                    "interval": "month",
                    "features": ["100 requêtes IA/mois", "Modèles de base", "Support communautaire"],
                    "description": "Découvrez la puissance de l'IA"
                },
                {
                    "name": "Pro",
                    "price": 99,
                    "currency": "eur",
                    "interval": "month",
                    "features": ["1000 requêtes IA/mois", "Modèles avancés", "Support prioritaire", "API access"],
                    "description": "IA pour professionnels"
                },
                {
                    "name": "Enterprise",
                    "price": 299,
                    "currency": "eur",
                    "interval": "month",
                    "features": ["Requêtes illimitées", "Modèles personnalisés", "Support dédié", "Intégrations"],
                    "description": "IA sur mesure pour entreprises"
                }
            ]
        else:
            # Plans génériques pour SaaS
            plans = [
                {
                    "name": "Starter",
                    "price": 19,
                    "currency": "eur",
                    "interval": "month",
                    "features": ["Fonctionnalités de base", "Support email", "1 utilisateur"],
                    "description": "Parfait pour démarrer"
                },
                {
                    "name": "Pro",
                    "price": 49,
                    "currency": "eur",
                    "interval": "month",
                    "features": ["Toutes les fonctionnalités", "Support prioritaire", "5 utilisateurs", "API access"],
                    "description": "Pour les équipes en croissance"
                },
                {
                    "name": "Enterprise",
                    "price": 149,
                    "currency": "eur",
                    "interval": "month",
                    "features": ["Tout du plan Pro", "Support dédié", "Utilisateurs illimités", "Intégrations"],
                    "description": "Solution complète pour entreprises"
                }
            ]
        
        return plans
    
    def _create_stripe_products(self, plans: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Crée les produits Stripe"""
        stripe_products = []
        
        for plan in plans:
            try:
                product = stripe.Product.create(
                    name=plan["name"],
                    description=plan["description"],
                    metadata={
                        "plan_type": plan["name"].lower(),
                        "features": ",".join(plan["features"])
                    }
                )
                
                stripe_products.append({
                    "id": product.id,
                    "name": product.name,
                    "plan_data": plan
                })
                
            except Exception as e:
                self.logger.warning(f"Erreur lors de la création du produit {plan['name']}: {e}")
        
        return stripe_products
    
    def _create_stripe_prices(self, stripe_products: List[Dict[str, Any]], plans: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Crée les prix Stripe pour chaque produit"""
        stripe_prices = []
        
        for product in stripe_products:
            plan = product["plan_data"]
            
            try:
                price = stripe.Price.create(
                    product=product["id"],
                    unit_amount=int(plan["price"] * 100),  # Stripe utilise les centimes
                    currency=plan["currency"],
                    recurring={
                        "interval": plan["interval"]
                    },
                    metadata={
                        "plan_name": plan["name"],
                        "features": ",".join(plan["features"])
                    }
                )
                
                stripe_prices.append({
                    "price_id": price.id,
                    "product_id": product["id"],
                    "name": plan["name"],
                    "price": plan["price"],
                    "currency": plan["currency"],
                    "interval": plan["interval"],
                    "features": plan["features"],
                    "description": plan["description"]
                })
                
            except Exception as e:
                self.logger.warning(f"Erreur lors de la création du prix pour {plan['name']}: {e}")
        
        return stripe_prices
    
    def _create_checkout_session(self, stripe_prices: List[Dict[str, Any]]):
        """Crée une session de checkout Stripe"""
        try:
            # Utiliser le premier plan comme plan par défaut
            default_price = stripe_prices[0]["price_id"] if stripe_prices else None
            
            if not default_price:
                raise Exception("Aucun prix Stripe disponible")
            
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price': default_price,
                    'quantity': 1,
                }],
                mode='subscription',
                success_url='https://yourdomain.com/success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url='https://yourdomain.com/cancel',
                metadata={
                    "startup_type": "saas",
                    "created_by": "PaymentsAgent"
                }
            )
            
            return checkout_session
            
        except Exception as e:
            raise Exception(f"Erreur lors de la création de la session de checkout: {e}")
    
    def get_subscription_status(self, session_id: str) -> Dict[str, Any]:
        """Récupère le statut d'un abonnement"""
        try:
            session = stripe.checkout.Session.retrieve(session_id)
            return {
                "session_id": session.id,
                "payment_status": session.payment_status,
                "subscription_id": session.subscription,
                "customer_id": session.customer
            }
        except Exception as e:
            return self.handle_error(e, f"Récupération du statut pour session_id: {session_id}")