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
        
        # 3. Créer la landing page React
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
                    "features": ["Personnalisation complète", "Support dédié", "Utilisateurs illimités", "API personnalisée"]
                }
            ]
        }
        
        return content
    
    def _generate_logo_svg(self, idea: str) -> str:
        """
        Génère un logo SVG minimal basé sur l'idée
        """
        print(f"🎨 Génération du logo SVG...")
        
        # Couleurs du logo
        primary_color = "#2563EB"
        secondary_color = "#1E40AF"
        
        # Créer un logo SVG simple et moderne
        svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <!-- Cercle de fond -->
  <circle cx="60" cy="60" r="55" fill="{primary_color}" opacity="0.1"/>
  
  <!-- Forme principale -->
  <path d="M30 40 L60 20 L90 40 L90 80 L60 100 L30 80 Z" 
        fill="{primary_color}" 
        stroke="{secondary_color}" 
        stroke-width="2"/>
  
  <!-- Élément central -->
  <circle cx="60" cy="60" r="15" fill="white"/>
  <circle cx="60" cy="60" r="8" fill="{primary_color}"/>
  
  <!-- Texte de l'idée -->
  <text x="60" y="115" 
        text-anchor="middle" 
        font-family="Arial, sans-serif" 
        font-size="8" 
        fill="{primary_color}" 
        font-weight="bold">
    {idea[:10].upper()}
  </text>
</svg>'''
        
        logo_path = self.branding_dir / "logo.svg"
        with open(logo_path, "w", encoding="utf-8") as f:
            f.write(svg_content)
        
        print(f"✅ Logo SVG généré: {logo_path}")
        return str(logo_path)
    
    def _create_landing_page(self, marketing_content: Dict, logo_path: str) -> str:
        """
        Crée une landing page React complète avec Tailwind CSS
        """
        print(f"🌐 Création de la landing page React...")
        
        # Créer le composant principal
        landing_page_jsx = self._generate_landing_page_jsx(marketing_content, logo_path)
        
        # Créer le fichier principal
        main_file = self.landing_dir / "LandingPage.jsx"
        with open(main_file, "w", encoding="utf-8") as f:
            f.write(landing_page_jsx)
        
        # Créer le fichier de styles Tailwind
        tailwind_file = self.landing_dir / "tailwind.config.js"
        with open(tailwind_file, "w", encoding="utf-8") as f:
            f.write(self._generate_tailwind_config())
        
        # Créer le fichier package.json
        package_file = self.landing_dir / "package.json"
        with open(package_file, "w", encoding="utf-8") as f:
            f.write(self._generate_package_json())
        
        # Créer le fichier README
        readme_file = self.landing_dir / "README.md"
        with open(readme_file, "w", encoding="utf-8") as f:
            f.write(self._generate_readme())
        
        print(f"✅ Landing page React créée: {self.landing_dir}")
        return str(self.landing_dir)
    
    def _generate_landing_page_jsx(self, marketing_content: Dict, logo_path: str) -> str:
        """
        Génère le composant React principal de la landing page
        """
        return f'''import React from 'react';

const LandingPage = () => {{
  const {{ headline, tagline, features, pricing }} = {json.dumps(marketing_content, ensure_ascii=False, indent=2)};

  return (
    <div className="min-h-screen bg-white">
      <!-- Hero Section -->
      <section className="bg-gradient-to-br from-blue-50 to-white py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <div className="flex justify-center mb-8">
              <img 
                src="{logo_path}" 
                alt="Logo" 
                className="w-24 h-24"
              />
            </div>
            <h1 className="text-5xl font-bold text-gray-900 mb-6">
              {{headline}}
            </h1>
            <p className="text-xl text-gray-600 mb-8 max-w-3xl mx-auto">
              {{tagline}}
            </p>
            <button className="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-4 px-8 rounded-lg text-lg transition duration-300 transform hover:scale-105">
              Commencer maintenant
            </button>
          </div>
        </div>
      </section>

      <!-- Features Section -->
      <section className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">
              Pourquoi nous choisir ?
            </h2>
            <p className="text-lg text-gray-600">
              Découvrez ce qui nous rend uniques
            </p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            {{features.map((feature, index) => (
              <div key={{index}} className="bg-white p-6 rounded-xl shadow-lg hover:shadow-xl transition duration-300 border border-gray-100">
                <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mb-4 mx-auto">
                  <svg className="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                  </svg>
                </div>
                <h3 className="text-lg font-semibold text-gray-900 mb-2">
                  {{feature}}
                </h3>
                <p className="text-gray-600">
                  Une fonctionnalité exceptionnelle qui vous fera gagner du temps.
                </p>
              </div>
            ))}}
          </div>
        </div>
      </section>

      <!-- Pricing Section -->
      <section className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">
              Choisissez votre plan
            </h2>
            <p className="text-lg text-gray-600">
              Des options flexibles pour tous les besoins
            </p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {{pricing.map((plan, index) => (
              <div key={{index}} className={`bg-white rounded-xl shadow-lg p-8 ${{plan.plan === 'Pro' ? 'ring-2 ring-blue-500 transform scale-105' : ''}}`}}>
                <div className="text-center">
                  <h3 className="text-2xl font-bold text-gray-900 mb-2">
                    {{plan.plan}}
                  </h3>
                  <div className="text-4xl font-bold text-blue-600 mb-4">
                    {{plan.price}}
                  </div>
                  <p className="text-gray-600 mb-6">
                    {{plan.desc}}
                  </p>
                  
                  <ul className="text-left space-y-3 mb-8">
                    {{plan.features.map((feature, fIndex) => (
                      <li key={{fIndex}} className="flex items-center">
                        <svg className="w-5 h-5 text-green-500 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                        </svg>
                        {{feature}}
                      </li>
                    ))}}
                  </ul>
                  
                  <button className={`w-full py-3 px-6 rounded-lg font-semibold transition duration-300 ${{plan.plan === 'Pro' 
                    ? 'bg-blue-600 hover:bg-blue-700 text-white' 
                    : 'bg-gray-100 hover:bg-gray-200 text-gray-800'}}`}}>
                    {{plan.plan === 'Enterprise' ? 'Nous contacter' : 'Choisir ce plan'}}
                  </button>
                </div>
              </div>
            ))}}
          </div>
        </div>
      </section>

      <!-- Footer -->
      <footer className="bg-gray-900 text-white py-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <div className="flex justify-center mb-6">
              <img 
                src="{logo_path}" 
                alt="Logo" 
                className="w-16 h-16 filter brightness-0 invert"
              />
            </div>
            <p className="text-lg mb-4">
              Prêt à transformer votre business ?
            </p>
            <p className="text-gray-400 mb-6">
              Contactez-nous à contact@startup.com
            </p>
            <div className="border-t border-gray-800 pt-6">
              <p className="text-gray-400">
                © 2024 Startup. Tous droits réservés.
              </p>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}};

export default LandingPage;
'''
    
    def _generate_tailwind_config(self) -> str:
        """
        Génère la configuration Tailwind CSS
        """
        return '''module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
    "./**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        'inter': ['Inter', 'sans-serif'],
      },
      colors: {
        'accent': '#2563EB',
      }
    },
  },
  plugins: [],
}'''
    
    def _generate_package_json(self) -> str:
        """
        Génère le fichier package.json pour la landing page
        """
        return '''{
  "name": "startup-landing-page",
  "version": "1.0.0",
  "description": "Landing page marketing générée automatiquement",
  "main": "index.js",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.0.0",
    "autoprefixer": "^10.4.14",
    "postcss": "^8.4.24",
    "tailwindcss": "^3.3.2",
    "vite": "^4.3.9"
  }
}'''
    
    def _generate_readme(self) -> str:
        """
        Génère le fichier README pour la landing page
        """
        return '''# Landing Page Marketing

Cette landing page a été générée automatiquement par l'agent marketing.

## Installation

```bash
npm install
```

## Développement

```bash
npm run dev
```

## Build

```bash
npm run build
```

## Technologies utilisées

- React 18
- Tailwind CSS
- Vite

## Structure

- **Hero Section** : Logo, headline, tagline et CTA
- **Features Section** : Cartes des fonctionnalités
- **Pricing Section** : Plans tarifaires
- **Footer** : Contact et informations

## Personnalisation

Modifiez le composant `LandingPage.jsx` pour adapter le contenu à vos besoins.
'''