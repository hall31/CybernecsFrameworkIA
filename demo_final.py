#!/usr/bin/env python3
"""
🎯 DÉMONSTRATION FINALE DU SYSTÈME D'AGENTS IA
==================================================
Ce script démontre toutes les fonctionnalités du système d'agents IA
qui crée automatiquement une startup complète avec backend Laravel et frontend React.
"""

import json
import time
from pathlib import Path
from main import StartupOrchestrator

def print_header():
    """Affiche l'en-tête de la démonstration"""
    print("🎯" + "="*58)
    print("🚀 SYSTÈME D'AGENTS IA POUR CRÉATION DE STARTUP")
    print("="*60)
    print("Ce système crée automatiquement une startup complète avec:")
    print("• Backend Laravel avec API REST complète")
    print("• Frontend React avec Tailwind CSS")
    print("• Infrastructure Docker avec Nginx")
    print("• Tests unitaires et configuration complète")
    print("="*60)

def demo_single_startup():
    """Démonstration d'une startup unique"""
    print("\n🚀 DÉMONSTRATION 1: CRÉATION D'UNE STARTUP")
    print("-" * 50)
    
    idea = "Plateforme de gestion de projets collaboratifs"
    print(f"💡 Idée: {idea}")
    
    orchestrator = StartupOrchestrator()
    start_time = time.time()
    
    result = orchestrator.create_startup(idea)
    end_time = time.time()
    
    print(f"⏱️  Temps d'exécution: {end_time - start_time:.2f} secondes")
    print(f"✅ Statut: {result['status']}")
    
    if result['status'] == 'success':
        print(f"🔧 Backend: {result['backend']['backend_type']}")
        print(f"🎨 Frontend: {result['frontend']['frontend_type']}")
        print(f"📁 Dossier: {result['generated_path']}")
        
        # Afficher les fonctionnalités
        print(f"\n🔧 Fonctionnalités Backend ({len(result['backend']['features'])}):")
        for feature in result['backend']['features']:
            print(f"   ✅ {feature}")
        
        print(f"\n🎨 Fonctionnalités Frontend ({len(result['frontend']['features'])}):")
        for feature in result['frontend']['features']:
            print(f"   ✅ {feature}")
        
        print(f"\n🌐 Endpoints API ({len(result['backend']['api_endpoints'])}):")
        for endpoint in result['backend']['api_endpoints']:
            print(f"   🔗 {endpoint}")
        
        return True
    else:
        print(f"❌ Erreur: {result.get('error', 'Erreur inconnue')}")
        return False

def demo_multiple_startups():
    """Démonstration de plusieurs startups"""
    print("\n🚀 DÉMONSTRATION 2: CRÉATION DE MULTIPLES STARTUPS")
    print("-" * 50)
    
    ideas = [
        "Marketplace de services freelance",
        "Plateforme de gestion d'événements",
        "SaaS de facturation et comptabilité",
        "Application de gestion d'inventaire"
    ]
    
    orchestrator = StartupOrchestrator()
    successful = 0
    
    for i, idea in enumerate(ideas, 1):
        print(f"\n{i}. Création de: {idea}")
        print("-" * 40)
        
        start_time = time.time()
        result = orchestrator.create_startup(idea)
        end_time = time.time()
        
        print(f"   ⏱️  Temps: {end_time - start_time:.2f}s")
        print(f"   ✅ Statut: {result['status']}")
        
        if result['status'] == 'success':
            successful += 1
            print(f"   🔧 Backend: {result['backend']['backend_type']}")
            print(f"   🎨 Frontend: {result['frontend']['frontend_type']}")
            print(f"   📁 Dossier: {result['generated_path']}")
        else:
            print(f"   ❌ Erreur: {result.get('error', 'Erreur inconnue')}")
    
    print(f"\n📊 RÉSULTAT: {successful}/{len(ideas)} startups créées avec succès")
    return successful == len(ideas)

def demo_custom_configuration():
    """Démonstration avec configuration personnalisée"""
    print("\n🚀 DÉMONSTRATION 3: CONFIGURATION PERSONNALISÉE")
    print("-" * 50)
    
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
    idea = "Plateforme de commerce électronique avancée"
    
    print(f"💡 Idée: {idea}")
    print("🔧 Stack personnalisée: Laravel 11 + Next.js 14 + PostgreSQL")
    
    start_time = time.time()
    result = orchestrator.create_startup(idea)
    end_time = time.time()
    
    print(f"⏱️  Temps d'exécution: {end_time - start_time:.2f} secondes")
    print(f"✅ Statut: {result['status']}")
    
    if result['status'] == 'success':
        print(f"🔧 Stack Backend: {result['stack']['backend']['framework']}")
        print(f"🎨 Stack Frontend: {result['stack']['frontend']['framework']}")
        print(f"🗄️ Base de données: {result['stack']['backend']['database']}")
        return True
    else:
        print(f"❌ Erreur: {result.get('error', 'Erreur inconnue')}")
        return False

def demo_file_structure():
    """Démonstration de la structure des fichiers générés"""
    print("\n🚀 DÉMONSTRATION 4: STRUCTURE DES FICHIERS GÉNÉRÉS")
    print("-" * 50)
    
    generated_path = Path("generated")
    if not generated_path.exists():
        print("❌ Aucun dossier 'generated' trouvé. Créez d'abord une startup.")
        return False
    
    print("📁 Structure du dossier 'generated':")
    
    def print_tree(path, prefix="", is_last=True):
        """Affiche l'arborescence des fichiers"""
        if path.is_file():
            print(f"{prefix}{'└── ' if is_last else '├── '}{path.name}")
        elif path.is_dir():
            print(f"{prefix}{'└── ' if is_last else '├── '}{path.name}/")
            items = list(path.iterdir())
            for i, item in enumerate(items):
                print_tree(item, prefix + ("    " if is_last else "│   "), i == len(items) - 1)
    
    print_tree(generated_path)
    
    # Compter les fichiers
    file_count = sum(1 for _ in generated_path.rglob("*") if _.is_file())
    dir_count = sum(1 for _ in generated_path.rglob("*") if _.is_file())
    
    print(f"\n📊 Statistiques:")
    print(f"   📁 Dossiers: {dir_count}")
    print(f"   📄 Fichiers: {file_count}")
    
    return True

def demo_docker_setup():
    """Démonstration de la configuration Docker"""
    print("\n🚀 DÉMONSTRATION 5: CONFIGURATION DOCKER")
    print("-" * 50)
    
    docker_file = Path("generated/docker-compose.yml")
    if not docker_file.exists():
        print("❌ Fichier docker-compose.yml non trouvé")
        return False
    
    print("🐳 Services Docker configurés:")
    
    with open(docker_file, 'r') as f:
        content = f.read()
    
    services = [
        "backend", "frontend", "nginx", "mysql", "redis"
    ]
    
    for service in services:
        if service in content:
            print(f"   ✅ {service}")
        else:
            print(f"   ❌ {service}")
    
    print(f"\n🌐 Ports exposés:")
    ports = [
        ("Frontend React", "3000"),
        ("Backend API", "8000"),
        ("Nginx", "80"),
        ("MySQL", "3306"),
        ("Redis", "6379")
    ]
    
    for service, port in ports:
        if port in content:
            print(f"   🔗 {service}: {port}")
        else:
            print(f"   ❌ {service}: {port}")
    
    print(f"\n📋 Pour démarrer:")
    print(f"   cd generated")
    print(f"   docker-compose up -d")
    
    return True

def main():
    """Fonction principale de démonstration"""
    print_header()
    
    try:
        # Démonstrations
        demo1_success = demo_single_startup()
        demo2_success = demo_multiple_startups()
        demo3_success = demo_custom_configuration()
        demo4_success = demo_file_structure()
        demo5_success = demo_docker_setup()
        
        # Résumé final
        print("\n" + "="*60)
        print("📊 RÉSUMÉ DES DÉMONSTRATIONS")
        print("="*60)
        
        demos = [
            ("Création d'une startup", demo1_success),
            ("Création de multiples startups", demo2_success),
            ("Configuration personnalisée", demo3_success),
            ("Structure des fichiers", demo4_success),
            ("Configuration Docker", demo5_success)
        ]
        
        successful_demos = 0
        for name, success in demos:
            status = "✅" if success else "❌"
            print(f"{status} {name}")
            if success:
                successful_demos += 1
        
        print(f"\n🎯 RÉSULTAT FINAL: {successful_demos}/{len(demos)} démonstrations réussies")
        
        if successful_demos == len(demos):
            print("\n🎉 TOUTES LES DÉMONSTRATIONS ONT RÉUSSI!")
            print("🚀 Le système d'agents IA fonctionne parfaitement!")
        else:
            print(f"\n⚠️  {len(demos) - successful_demos} démonstration(s) ont échoué")
        
        print("\n📚 Prochaines étapes:")
        print("   1. Explorez le dossier 'generated/'")
        print("   2. Lancez 'docker-compose up -d' dans le dossier généré")
        print("   3. Accédez à http://localhost pour voir le frontend")
        print("   4. Testez l'API sur http://localhost/api")
        print("   5. Consultez README_AGENTS.md pour plus d'informations")
        
        return successful_demos == len(demos)
        
    except Exception as e:
        print(f"\n❌ Erreur lors de la démonstration: {str(e)}")
        print("Vérifiez que tous les agents sont correctement configurés")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)