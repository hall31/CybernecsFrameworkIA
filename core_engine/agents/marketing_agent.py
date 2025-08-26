import os
import json
from typing import Dict, List
from pathlib import Path

class MarketingAgent:
    def __init__(self):
        self.generated_dir = Path("generated")
        self.branding_dir = self.generated_dir / "branding"
        self.landing_dir = self.generated_dir / "landing-page"
        
        # Créer les dossiers s'ils n'existent pas
        self.branding_dir.mkdir(parents=True, exist_ok=True)
        self.landing_dir.mkdir(parents=True, exist_ok=True)
    
    def run(self, idea: str) -> Dict:
        """
        Génère tout le contenu marketing pour une idée de startup
        """
        print(f"🎯 MarketingAgent: Génération du contenu marketing pour '{idea}'")
        
        # 1. Générer le contenu marketing
        marketing_content = self._generate_marketing_content(idea)
        
        # 2. Générer le logo SVG
        logo_path = self._generate_logo_svg(idea)
        
        # 3. Créer la landing page HTML
        landing_path = self._create_landing_page(marketing_content, logo_path)
        
        # 4. Retourner le résultat
        result = {
            "headline": marketing_content["headline"],
            "tagline": marketing_content["tagline"],
            "features": marketing_content["features"],
            "pricing": marketing_content["pricing"],
            "logo": str(logo_path),
            "landing": str(landing_path)
        }
        
        print(f"✅ MarketingAgent: Contenu marketing généré avec succès")
        return result
    
    def _generate_marketing_content(self, idea: str) -> Dict:
        """
        Génère le contenu marketing (headline, tagline, features, pricing)
        """
        print(f"📝 Génération du contenu marketing...")
        
        # Headlines et taglines selon le type d'idée
        headlines = {
            "marketplace": "La plateforme qui révolutionne le commerce",
            "saas": "L'outil SaaS qui simplifie votre quotidien",
            "app": "L'application qui change la donne",
            "platform": "La plateforme nouvelle génération",
            "tool": "L'outil indispensable pour votre réussite"
        }
        
        taglines = {
            "marketplace": "Connectez, échangez, réussissez",
            "saas": "Simplicité et efficacité au service de votre business",
            "app": "Innovation et performance dans votre poche",
            "platform": "La puissance d'une plateforme, la simplicité d'une app",
            "tool": "Transformez vos idées en succès"
        }
        
        # Déterminer le type d'idée
        idea_type = "saas"  # Par défaut
        for key in headlines.keys():
            if key in idea.lower():
                idea_type = key
                break
        
        # Générer le contenu
        content = {
            "headline": headlines[idea_type],
            "tagline": taglines[idea_type],
            "features": [
                "Interface intuitive et moderne",
                "Performance et rapidité garanties",
                "Support client 24/7",
                "Intégrations multiples"
            ],
            "pricing": [
                {
                    "plan": "Starter",
                    "price": "€19/mois",
                    "desc": "Parfait pour démarrer",
                    "features": ["Fonctionnalités de base", "Support email", "1 utilisateur"]
                },
                {
                    "plan": "Pro",
                    "price": "€49/mois",
                    "desc": "Pour les équipes en croissance",
                    "features": ["Toutes les fonctionnalités", "Support prioritaire", "5 utilisateurs", "Analytics avancés"]
                },
                {
                    "plan": "Enterprise",
                    "price": "Contactez-nous",
                    "desc": "Solutions sur mesure",
                    "features": ["Personnalisation complète", "Support dédié", "SLA garanti", "Intégrations sur mesure"]
                }
            ]
        }
        
        return content
    
    def _generate_logo_svg(self, idea: str) -> Path:
        """
        Génère un logo SVG simple pour la startup
        """
        print(f"🎨 Génération du logo SVG...")
        
        # Créer un logo SVG simple avec le nom de la startup
        startup_name = idea.split()[0].title()  # Premier mot de l'idée
        
        svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#3B82F6;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#1E40AF;stop-opacity:1" />
    </linearGradient>
  </defs>
  
  <!-- Cercle de fond -->
  <circle cx="100" cy="100" r="90" fill="url(#grad1)" />
  
  <!-- Texte du logo -->
  <text x="100" y="120" font-family="Arial, sans-serif" font-size="24" font-weight="bold" 
        text-anchor="middle" fill="white">{startup_name}</text>
  
  <!-- Icône simple -->
  <path d="M80 70 L120 70 L120 110 L80 110 Z" fill="white" opacity="0.8"/>
  <circle cx="100" cy="90" r="8" fill="white" opacity="0.6"/>
</svg>'''
        
        logo_path = self.branding_dir / f"{startup_name.lower()}_logo.svg"
        logo_path.write_text(svg_content)
        
        print(f"✅ Logo généré: {logo_path}")
        return logo_path
    
    def _create_landing_page(self, marketing_content: Dict, logo_path: Path) -> Path:
        """
        Crée une landing page HTML simple
        """
        print(f"🌐 Création de la landing page...")
        
        # Créer le contenu HTML
        html_content = self._generate_html_content(marketing_content, logo_path)
        
        # Sauvegarder la landing page
        landing_path = self.landing_dir / "index.html"
        landing_path.write_text(html_content)
        
        print(f"✅ Landing page créée: {landing_path}")
        return landing_path
    
    def _generate_html_content(self, marketing_content: Dict, logo_path: Path) -> str:
        """
        Génère le contenu HTML de la landing page
        """
        features_html = ""
        for feature in marketing_content["features"]:
            features_html += f'<li class="feature-item">✅ {feature}</li>'
        
        pricing_html = ""
        for plan in marketing_content["pricing"]:
            features_list = ""
            for feature in plan["features"]:
                features_list += f'<li>✅ {feature}</li>'
            
            pricing_html += f'''
            <div class="pricing-card">
                <h3>{plan["plan"]}</h3>
                <div class="price">{plan["price"]}</div>
                <p class="description">{plan["desc"]}</p>
                <ul class="features">
                    {features_list}
                </ul>
                <button class="cta-button">Choisir ce plan</button>
            </div>
            '''
        
        html_content = f'''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{marketing_content["headline"]}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-align: center;
            padding: 4rem 2rem;
        }}
        
        .logo {{
            width: 80px;
            height: 80px;
            margin: 0 auto 2rem;
            filter: brightness(0) invert(1);
        }}
        
        .hero h1 {{
            font-size: 3rem;
            margin-bottom: 1rem;
        }}
        
        .hero p {{
            font-size: 1.5rem;
            opacity: 0.9;
        }}
        
        .features {{
            padding: 4rem 2rem;
            background: #f8f9fa;
        }}
        
        .features h2 {{
            text-align: center;
            margin-bottom: 3rem;
            font-size: 2.5rem;
            color: #333;
        }}
        
        .features-list {{
            max-width: 800px;
            margin: 0 auto;
            list-style: none;
        }}
        
        .feature-item {{
            background: white;
            padding: 1.5rem;
            margin-bottom: 1rem;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            font-size: 1.1rem;
        }}
        
        .pricing {{
            padding: 4rem 2rem;
            background: white;
        }}
        
        .pricing h2 {{
            text-align: center;
            margin-bottom: 3rem;
            font-size: 2.5rem;
            color: #333;
        }}
        
        .pricing-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        .pricing-card {{
            background: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            text-align: center;
            border: 2px solid #f0f0f0;
            transition: transform 0.3s ease;
        }}
        
        .pricing-card:hover {{
            transform: translateY(-5px);
        }}
        
        .pricing-card h3 {{
            font-size: 1.5rem;
            margin-bottom: 1rem;
            color: #333;
        }}
        
        .price {{
            font-size: 2.5rem;
            font-weight: bold;
            color: #667eea;
            margin-bottom: 1rem;
        }}
        
        .description {{
            color: #666;
            margin-bottom: 2rem;
        }}
        
        .features {{
            list-style: none;
            margin-bottom: 2rem;
            text-align: left;
        }}
        
        .features li {{
            padding: 0.5rem 0;
            border-bottom: 1px solid #f0f0f0;
        }}
        
        .cta-button {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 1rem 2rem;
            border-radius: 25px;
            font-size: 1.1rem;
            cursor: pointer;
            transition: transform 0.3s ease;
        }}
        
        .cta-button:hover {{
            transform: scale(1.05);
        }}
        
        .footer {{
            background: #333;
            color: white;
            text-align: center;
            padding: 2rem;
        }}
        
        @media (max-width: 768px) {{
            .hero h1 {{
                font-size: 2rem;
            }}
            
            .hero p {{
                font-size: 1.2rem;
            }}
            
            .pricing-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <header class="header">
        <img src="{logo_path}" alt="Logo" class="logo">
        <div class="hero">
            <h1>{marketing_content["headline"]}</h1>
            <p>{marketing_content["tagline"]}</p>
        </div>
    </header>
    
    <section class="features">
        <h2>Fonctionnalités principales</h2>
        <ul class="features-list">
            {features_html}
        </ul>
    </section>
    
    <section class="pricing">
        <h2>Nos tarifs</h2>
        <div class="pricing-grid">
            {pricing_html}
        </div>
    </section>
    
    <footer class="footer">
        <p>&copy; 2024 {marketing_content["headline"]}. Tous droits réservés.</p>
    </footer>
</body>
</html>'''
        
        return html_content