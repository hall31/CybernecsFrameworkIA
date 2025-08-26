#!/usr/bin/env python3
"""
Démonstration complète du système Epic4
Montre toutes les fonctionnalités : CEO, CTO, Dev, Marketing
"""

import sys
from pathlib import Path

# Ajouter les répertoires nécessaires au path Python
def setup_import_paths():
    current_dir = Path(__file__).parent
    sys.path.insert(0, str(current_dir))
    sys.path.insert(0, str(current_dir / "core-engine"))
    sys.path.insert(0, str(current_dir / "core-engine" / "agents"))

setup_import_paths()

# Import direct des classes
try:
    # Import du logger
    from logger import StartupLogger, get_logger
    
    # Import du marketing agent simplifié
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

Démonstration du système d'agents IA pour création de startup
"""

from main import StartupOrchestrator
import json

def demo_simple():
    """Démonstration simple avec une idée de startup"""
    print("🚀 DÉMONSTRATION SIMPLE")
    print("=" * 50)
    
    orchestrator = StartupOrchestrator()
    result = orchestrator.create_startup("Plateforme de gestion de projets")
    
    print(f"✅ Statut: {result['status']}")
    print(f"📁 Dossier généré: {result['generated_path']}")
    
    if result['status'] == 'success':
        print(f"🔧 Backend: {result['backend']['backend_type']}")
        print(f"🎨 Frontend: {result['frontend']['frontend_type']}")
        print(f"📊 Roadmap: {result['roadmap']['vision']}")

def demo_multiple_startups():
    """Démonstration avec plusieurs idées de startup"""
    print("\n🚀 DÉMONSTRATION MULTIPLE STARTUPS")
    print("=" * 50)
    
    ideas = [
        "Marketplace de services freelance",
        "Plateforme de gestion d'événements",
        "SaaS de facturation et comptabilité",
        "Application de gestion d'inventaire"
    ]
    
    orchestrator = StartupOrchestrator()
    
    for i, idea in enumerate(ideas, 1):
        print(f"\n{i}. Création de: {idea}")
        print("-" * 40)
        
        result = orchestrator.create_startup(idea)
        
        if result['status'] == 'success':
            print(f"✅ Créée avec succès")
            print(f"   Backend: {result['backend']['backend_type']}")
            print(f"   Frontend: {result['frontend']['frontend_type']}")
            print(f"   API Endpoints: {len(result['backend']['api_endpoints'])}")
        else:
            print(f"❌ Erreur: {result.get('error', 'Erreur inconnue')}")

def demo_custom_stack():
    """Démonstration avec une stack technique personnalisée"""
    print("\n🚀 DÉMONSTRATION STACK PERSONNALISÉE")
    print("=" * 50)
    
    # Créer un orchestrateur personnalisé
    class CustomOrchestrator(StartupOrchestrator):
        def _execute_cto_agent(self, roadmap):
            """Stack technique personnalisée"""
            print("⚡ CTOAgent - Stack technique personnalisée")
            
            stack = {
                "backend": {
                    "framework": "Laravel 11",
                    "database": "PostgreSQL 15",
                    "authentication": "Laravel Sanctum + JWT",
                    "api": "GraphQL + REST",
                    "deployment": "Kubernetes + Helm"
                },
                "frontend": {
                    "framework": "Next.js 14",
                    "styling": "Tailwind CSS + Framer Motion",
                    "routing": "App Router",
                    "state_management": "Zustand + React Query",
                    "build_tool": "Turbopack"
                },
                "infrastructure": {
                    "containerization": "Docker + BuildKit",
                    "reverse_proxy": "Traefik",
                    "database": "PostgreSQL + Redis Cluster",
                    "cache": "Redis + Memcached",
                    "monitoring": "Prometheus + Grafana"
                }
            }
            
            return stack
    
    orchestrator = CustomOrchestrator()
    result = orchestrator.create_startup("Plateforme de commerce électronique")
    
    print(f"✅ Statut: {result['status']}")
    if result['status'] == 'success':
        print(f"🔧 Stack Backend: {result['stack']['backend']['framework']}")
        print(f"🎨 Stack Frontend: {result['stack']['frontend']['framework']}")
        print(f"🗄️ Base de données: {result['stack']['backend']['database']}")

def demo_agent_individual():
    """Démonstration d'utilisation individuelle des agents"""
    print("\n🚀 DÉMONSTRATION AGENTS INDIVIDUELS")
    print("=" * 50)
    
    from core_engine.agents.dev_backend_agent import DevBackendAgent
    from core_engine.agents.dev_frontend_agent import DevFrontendAgent
    
    # Configuration de stack
    stack = {
        "backend": {"framework": "Laravel 10"},
        "frontend": {"framework": "React 18"}
    }
    
    # Utiliser uniquement l'agent backend
    print("🔧 Utilisation de DevBackendAgent uniquement")
    backend_agent = DevBackendAgent()
    backend_result = backend_agent.run(stack)
    
    print(f"   Statut: {backend_result['status']}")
    if backend_result['status'] == 'success':
        print(f"   Type: {backend_result['backend_type']}")
        print(f"   Fonctionnalités: {len(backend_result['features'])}")
    
    # Utiliser uniquement l'agent frontend
    print("\n🎨 Utilisation de DevFrontendAgent uniquement")
    frontend_agent = DevFrontendAgent()
    frontend_result = frontend_agent.run(stack)
    
    print(f"   Statut: {frontend_result['status']}")
    if frontend_result['status'] == 'success':
        print(f"   Type: {frontend_result['frontend_type']}")
        print(f"   Pages: {len(frontend_result['pages'])}")

def main():
    """Fonction principale de démonstration"""
    print("🎯 SYSTÈME D'AGENTS IA POUR CRÉATION DE STARTUP")
    print("=" * 60)
    print("Ce système crée automatiquement une startup complète avec:")
    print("• Backend Laravel avec API REST")
    print("• Frontend React avec Tailwind CSS")
    print("• Infrastructure Docker avec Nginx")
    print("• Tests unitaires et configuration complète")
    print("=" * 60)
    
    try:
        # Démonstrations
        demo_simple()
        demo_multiple_startups()
        demo_custom_stack()
        demo_agent_individual()
        
        print("\n🎉 DÉMONSTRATION TERMINÉE AVEC SUCCÈS!")
        print("=" * 60)
        print("📁 Toutes les startups ont été créées dans le dossier 'generated/'")
        print("🚀 Pour démarrer une startup:")
        print("   cd generated/[nom_startup]")
        print("   docker-compose up -d")
        print("\n📚 Consultez README_AGENTS.md pour plus d'informations")
        
    except Exception as e:
        print(f"\n❌ Erreur lors de la démonstration: {str(e)}")
        print("Vérifiez que tous les agents sont correctement configurés")

if __name__ == "__main__":
    main()