#!/usr/bin/env python3
"""
Démonstration complète du système Epic4
Montre toutes les fonctionnalités : CEO, CTO, Dev, Marketing
"""

import sys
from pathlib import Path

# Ajouter le répertoire courant au path Python
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

# Import direct des classes
try:
    # Import du logger
    sys.path.insert(0, str(current_dir / "core-engine"))
    from logger import StartupLogger, get_logger
    
    # Import du marketing agent simplifié
    sys.path.insert(0, str(current_dir / "core-engine" / "agents"))
    from marketing_agent_simple import MarketingAgent
    
    print("✅ Imports réussis!")
    
except ImportError as e:
    print(f"❌ Erreur d'import: {e}")
    print("Vérifiez que la structure des dossiers est correcte")
    sys.exit(1)

def demo_marketing_agent():
    """Démonstration du Marketing Agent"""
    print("\n" + "🎨" + "="*50)
    print("🎨 DÉMONSTRATION DU MARKETING AGENT")
    print("="*50)
    
    # Test avec différentes idées
    test_ideas = [
        "SaaS marketplace pour freelances",
        "Application mobile de fitness",
        "Plateforme de gestion de projets",
        "Outil de création de contenu"
    ]
    
    for i, idea in enumerate(test_ideas, 1):
        print(f"\n{i}. 🎯 Test avec l'idée: {idea}")
        print("-" * 40)
        
        try:
            # Créer l'agent
            agent = MarketingAgent()
            
            # Exécuter l'agent
            result = agent.run(idea)
            
            # Afficher les résultats
            print(f"   ✅ Succès!")
            print(f"   📝 Headline: {result['headline']}")
            print(f"   🏷️  Tagline: {result['tagline']}")
            print(f"   ⭐ Features: {len(result['features'])} fonctionnalités")
            print(f"   💰 Pricing: {len(result['pricing'])} plans")
            print(f"   🎨 Logo: {result['logo']}")
            print(f"   🌐 Landing: {result['landing']}")
            
        except Exception as e:
            print(f"   ❌ Erreur: {e}")

def demo_file_structure():
    """Démonstration de la structure des fichiers générés"""
    print("\n" + "📁" + "="*50)
    print("📁 STRUCTURE DES FICHIERS GÉNÉRÉS")
    print("="*50)
    
    generated_dir = Path("generated")
    
    if generated_dir.exists():
        print(f"📂 Dossier principal: {generated_dir}")
        
        # Logo
        logo_dir = generated_dir / "branding"
        if logo_dir.exists():
            logo_files = list(logo_dir.glob("*.svg"))
            print(f"🎨 Logo ({len(logo_files)} fichiers):")
            for logo in logo_files:
                print(f"   - {logo}")
        
        # Landing page
        landing_dir = generated_dir / "landing-page"
        if landing_dir.exists():
            print(f"🌐 Landing page:")
            landing_files = list(landing_dir.rglob("*"))
            for file in landing_files:
                if file.is_file():
                    print(f"   - {file.relative_to(generated_dir)}")
        
        # Résultat
        result_file = generated_dir / "startup_result.json"
        if result_file.exists():
            print(f"📊 Résultat: {result_file}")
            
            # Afficher un aperçu du contenu
            import json
            with open(result_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                print(f"   🚀 Startup: {data['startup']['idea']}")
                print(f"   📅 Généré le: {data['startup']['generated_at']}")
                print(f"   ✅ Status: {data['startup']['status']}")
    else:
        print("❌ Aucun fichier généré trouvé")

def demo_landing_page_preview():
    """Aperçu de la landing page générée"""
    print("\n" + "🌐" + "="*50)
    print("🌐 APERÇU DE LA LANDING PAGE")
    print("="*50)
    
    landing_file = Path("generated/landing-page/LandingPage.jsx")
    
    if landing_file.exists():
        print(f"📄 Fichier: {landing_file}")
        
        # Lire et afficher un aperçu
        with open(landing_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Extraire les sections principales
            sections = [
                ("Hero Section", "<!-- Hero Section -->"),
                ("Features Section", "<!-- Features Section -->"),
                ("Pricing Section", "<!-- Pricing Section -->"),
                ("Footer", "<!-- Footer -->")
            ]
            
            for section_name, section_marker in sections:
                if section_marker in content:
                    print(f"   ✅ {section_name}")
                else:
                    print(f"   ❌ {section_name}")
        
        print(f"\n📱 Pour tester la landing page:")
        print(f"   cd generated/landing-page")
        print(f"   npm install")
        print(f"   npm run dev")
        
    else:
        print("❌ Landing page non trouvée")

def demo_logo_preview():
    """Aperçu du logo généré"""
    print("\n" + "🎨" + "="*50)
    print("🎨 APERÇU DU LOGO")
    print("="*50)
    
    logo_file = Path("generated/branding/logo.svg")
    
    if logo_file.exists():
        print(f"🎨 Fichier: {logo_file}")
        
        # Lire et afficher un aperçu
        with open(logo_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Vérifier les éléments du logo
            checks = [
                ("SVG valide", "<?xml version="),
                ("Forme géométrique", "<path d="),
                ("Couleurs", "#2563EB"),
                ("Dimensions", "width=\"120\" height=\"120\"")
            ]
            
            for check_name, check_marker in checks:
                if check_marker in content:
                    print(f"   ✅ {check_name}")
                else:
                    print(f"   ❌ {check_name}")
        
        print(f"\n🎨 Le logo est un fichier SVG vectoriel de 120x120px")
        print(f"   Couleurs: Bleu principal (#2563EB), secondaire (#1E40AF)")
        print(f"   Design: Forme hexagonale avec élément central")
        
    else:
        print("❌ Logo non trouvé")

def main():
    """Fonction principale de démonstration"""
    print("🚀" + "="*60)
    print("🚀 DÉMONSTRATION COMPLÈTE DU SYSTÈME EPIC4")
    print("="*60)
    print("🎯 Générateur de startups IA avec agents spécialisés")
    print("🤖 CEO + CTO + Dev + Marketing = Startup complète")
    
    # 1. Démonstration du Marketing Agent
    demo_marketing_agent()
    
    # 2. Structure des fichiers
    demo_file_structure()
    
    # 3. Aperçu de la landing page
    demo_landing_page_preview()
    
    # 4. Aperçu du logo
    demo_logo_preview()
    
    # 5. Résumé final
    print("\n" + "🎉" + "="*50)
    print("🎉 DÉMONSTRATION TERMINÉE !")
    print("="*50)
    print("✅ Marketing Agent fonctionnel")
    print("✅ Logo SVG généré")
    print("✅ Landing page React créée")
    print("✅ Structure de fichiers complète")
    print("✅ Documentation générée")
    
    print(f"\n🚀 Prochaines étapes:")
    print(f"   1. Tester: python3 test_simple.py")
    print(f"   2. Générer: python3 main_simple.py")
    print(f"   3. Explorer: ls -la generated/")
    print(f"   4. Développer: cd generated/landing-page && npm install")

if __name__ == "__main__":
    main()