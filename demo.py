#!/usr/bin/env python3
"""
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