#!/usr/bin/env python3
"""
Script de test pour l'API REST de l'Epic 9
Teste la création de startup avec infrastructure complète
"""

import sys
import os
import json
import time

# Ajout du chemin des modules


from orchestrator.main import handle_create_startup_request
def test_create_startup_api():
    """Test de l'API de création de startup"""
    
    print("🧪 Test de l'API REST /create-startup")
    print("=" * 50)
    
    # Test 1: Création normale
    print("\n📝 Test 1: Création de startup normale")
    request_data = {
        "idea": "SaaS marketplace pour freelances"
    }
    
    print(f"Requête: {json.dumps(request_data, indent=2)}")
    
    try:
        result = handle_create_startup_request(request_data)
        print(f"✅ Réponse: {json.dumps(result, indent=2, ensure_ascii=False)}")
    except Exception as e:
        print(f"❌ Erreur: {e}")
    
    # Test 2: Idée vide
    print("\n📝 Test 2: Idée vide")
    request_data = {
        "idea": ""
    }
    
    print(f"Requête: {json.dumps(request_data, indent=2)}")
    
    try:
        result = handle_create_startup_request(request_data)
        print(f"✅ Réponse: {json.dumps(result, indent=2, ensure_ascii=False)}")
    except Exception as e:
        print(f"❌ Erreur: {e}")
    
    # Test 3: Idée manquante
    print("\n📝 Test 3: Idée manquante")
    request_data = {}
    
    print(f"Requête: {json.dumps(request_data, indent=2)}")
    
    try:
        result = handle_create_startup_request(request_data)
        print(f"✅ Réponse: {json.dumps(result, indent=2, ensure_ascii=False)}")
    except Exception as e:
        print(f"❌ Erreur: {e}")
    
    # Test 4: Idée avec caractères spéciaux
    print("\n📝 Test 4: Idée avec caractères spéciaux")
    request_data = {
        "idea": "🚀 Plateforme IA pour l'analyse de données 📊"
    }
    
    print(f"Requête: {json.dumps(request_data, indent=2)}")
    
    try:
        result = handle_create_startup_request(request_data)
        print(f"✅ Réponse: {json.dumps(result, indent=2, ensure_ascii=False)}")
    except Exception as e:
        print(f"❌ Erreur: {e}")
    
    # Test 5: Idée très longue
    print("\n📝 Test 5: Idée très longue")
    long_idea = "Une plateforme SaaS très sophistiquée et innovante qui révolutionne complètement le marché des applications métier en proposant une solution intégrée de gestion d'entreprise avec des fonctionnalités avancées d'intelligence artificielle, de machine learning, d'analyse prédictive, de reporting en temps réel, de workflow automation, de gestion des processus métier, d'intégration API, de sécurité renforcée, de conformité réglementaire, de scalabilité cloud-native, de monitoring avancé, et d'alerting intelligent pour les équipes DevOps et les administrateurs système"
    
    request_data = {
        "idea": long_idea
    }
    
    print(f"Requête: {json.dumps(request_data, indent=2)}")
    
    try:
        result = handle_create_startup_request(request_data)
        print(f"✅ Réponse: {json.dumps(result, indent=2, ensure_ascii=False)}")
    except Exception as e:
        print(f"❌ Erreur: {e}")


def test_performance():
    """Test de performance de l'API"""
    
    print("\n🚀 Test de performance")
    print("=" * 50)
    
    request_data = {
        "idea": "Test de performance"
    }
    
    # Test avec 5 requêtes consécutives
    times = []
    for i in range(5):
        start_time = time.time()
        try:
            result = handle_create_startup_request(request_data)
            end_time = time.time()
            duration = end_time - start_time
            times.append(duration)
            print(f"Requête {i+1}: {duration:.3f}s - {result.get('status', 'unknown')}")
        except Exception as e:
            print(f"Requête {i+1}: Erreur - {e}")
    
    if times:
        avg_time = sum(times) / len(times)
        min_time = min(times)
        max_time = max(times)
        
        print(f"\n📊 Statistiques de performance:")
        print(f"   Temps moyen: {avg_time:.3f}s")
        print(f"   Temps minimum: {min_time:.3f}s")
        print(f"   Temps maximum: {max_time:.3f}s")


def test_infrastructure_validation():
    """Test de validation de l'infrastructure"""
    
    print("\n🔍 Test de validation de l'infrastructure")
    print("=" * 50)
    
    request_data = {
        "idea": "Validation infrastructure"
    }
    
    try:
        result = handle_create_startup_request(request_data)
        
        # Vérification de la structure de réponse
        required_fields = ['project_id', 'idea', 'status', 'infra', 'monitoring', 'alerting', 'summary']
        missing_fields = [field for field in required_fields if field not in result]
        
        if missing_fields:
            print(f"❌ Champs manquants: {missing_fields}")
        else:
            print("✅ Structure de réponse valide")
        
        # Vérification de l'infrastructure
        infra = result.get('infra', {})
        if infra.get('cluster') and infra.get('url') and infra.get('scaling'):
            print("✅ Infrastructure valide")
        else:
            print("❌ Infrastructure invalide")
        
        # Vérification du monitoring
        monitoring = result.get('monitoring', {})
        if monitoring.get('grafana_url') and monitoring.get('dashboards'):
            print("✅ Monitoring valide")
        else:
            print("❌ Monitoring invalide")
        
        # Vérification des alertes
        alerting = result.get('alerting', {})
        if alerting.get('alerts') and alerting.get('channels'):
            print("✅ Alertes valides")
        else:
            print("❌ Alertes invalides")
        
        # Vérification du résumé
        summary = result.get('summary', {})
        if summary.get('cluster') and summary.get('url'):
            print("✅ Résumé valide")
        else:
            print("❌ Résumé invalide")
        
    except Exception as e:
        print(f"❌ Erreur lors de la validation: {e}")


def main():
    """Fonction principale de test"""
    
    print("🎯 Tests de l'API REST Epic 9 - Infrastructure DevOps")
    print("=" * 60)
    
    # Tests de base
    test_create_startup_api()
    
    # Tests de performance
    test_performance()
    
    # Tests de validation
    test_infrastructure_validation()
    
    print("\n🎉 Tests terminés!")
    print("=" * 60)


if __name__ == "__main__":
    main()
=======
Script de test simple pour vérifier l'API Epic6 Core Engine
"""

import asyncio
import aiohttp
import json
from datetime import datetime

API_BASE_URL = "http://localhost:8000/api/v1"

async def test_health_check():
    """Test du health check"""
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(f"{API_BASE_URL.replace('/api/v1', '')}/health") as response:
                if response.status == 200:
                    data = await response.json()
                    print(f"✅ Health check: {data}")
                    return True
                else:
                    print(f"❌ Health check failed: {response.status}")
                    return False
        except Exception as e:
            print(f"❌ Health check error: {e}")
            return False

async def test_create_startup():
    """Test de création d'un projet startup"""
    project_data = {
        "idea": "SaaS marketplace pour freelances",
        "roadmap": {
            "phase1": "MVP - Fonctionnalités de base",
            "phase2": "Beta - Tests utilisateurs",
            "phase3": "Production - Lancement officiel"
        },
        "stack": {
            "frontend": "React + TypeScript",
            "backend": "FastAPI + PostgreSQL",
            "deployment": "Docker + AWS"
        }
    }
    
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(
                f"{API_BASE_URL}/create-startup",
                json=project_data
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    print(f"✅ Startup créée: {data['idea']}")
                    print(f"   ID: {data['id']}")
                    return data['id']
                else:
                    print(f"❌ Création startup failed: {response.status}")
                    error_text = await response.text()
                    print(f"   Error: {error_text}")
                    return None
        except Exception as e:
            print(f"❌ Création startup error: {e}")
            return None

async def test_get_projects():
    """Test de récupération de la liste des projets"""
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(f"{API_BASE_URL}/projects") as response:
                if response.status == 200:
                    data = await response.json()
                    print(f"✅ Projets récupérés: {len(data)} projet(s)")
                    for project in data:
                        print(f"   - {project['idea']} (ID: {project['id']})")
                    return True
                else:
                    print(f"❌ Récupération projets failed: {response.status}")
                    return False
        except Exception as e:
            print(f"❌ Récupération projets error: {e}")
            return False

async def test_get_project_details(project_id):
    """Test de récupération des détails d'un projet"""
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(f"{API_BASE_URL}/projects/{project_id}") as response:
                if response.status == 200:
                    data = await response.json()
                    print(f"✅ Détails projet récupérés: {data['idea']}")
                    print(f"   Roadmap: {len(data.get('roadmap', {}))} phases")
                    print(f"   Stack: {len(data.get('stack', {}))} technologies")
                    return True
                else:
                    print(f"❌ Récupération détails failed: {response.status}")
                    return False
        except Exception as e:
            print(f"❌ Récupération détails error: {e}")
            return False

async def test_download_project(project_id):
    """Test de téléchargement d'un projet"""
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(f"{API_BASE_URL}/projects/{project_id}/download") as response:
                if response.status == 200:
                    content_type = response.headers.get('content-type', '')
                    if 'application/zip' in content_type:
                        print(f"✅ Téléchargement projet réussi")
                        print(f"   Content-Type: {content_type}")
                        return True
                    else:
                        print(f"⚠️ Téléchargement réussi mais mauvais type: {content_type}")
                        return False
                else:
                    print(f"❌ Téléchargement failed: {response.status}")
                    return False
        except Exception as e:
            print(f"❌ Téléchargement error: {e}")
            return False

async def run_all_tests():
    """Exécuter tous les tests"""
    print("🚀 Démarrage des tests de l'API Epic6 Core Engine")
    print("=" * 60)
    
    # Test 1: Health check
    print("\n1️⃣ Test du health check...")
    if not await test_health_check():
        print("❌ L'application n'est pas accessible. Arrêt des tests.")
        return
    
    # Test 2: Création d'un projet
    print("\n2️⃣ Test de création d'un projet startup...")
    project_id = await test_create_startup()
    if not project_id:
        print("❌ Impossible de créer un projet. Arrêt des tests.")
        return
    
    # Test 3: Récupération de la liste des projets
    print("\n3️⃣ Test de récupération de la liste des projets...")
    await test_get_projects()
    
    # Test 4: Récupération des détails du projet
    print("\n4️⃣ Test de récupération des détails du projet...")
    await test_get_project_details(project_id)
    
    # Test 5: Téléchargement du projet
    print("\n5️⃣ Test de téléchargement du projet...")
    await test_download_project(project_id)
    
    print("\n" + "=" * 60)
    print("✅ Tous les tests sont terminés!")
    print(f"🌐 API disponible sur: {API_BASE_URL}")
    print(f"📚 Documentation: {API_BASE_URL.replace('/api/v1', '')}/docs")

if __name__ == "__main__":
    try:
        asyncio.run(run_all_tests())
    except KeyboardInterrupt:
        print("\n\n⏹️ Tests interrompus par l'utilisateur")
    except Exception as e:
        print(f"\n\n💥 Erreur lors de l'exécution des tests: {e}")
Script de test pour l'API FastAPI
"""

import requests
import json
import time
import sys

def test_api():
    """Test de l'API FastAPI"""
    
    base_url = "http://localhost:8000"
    
    print("🧪 Test de l'API Core Engine")
    print("=" * 50)
    
    # Test 1: Endpoint racine
    print("\n1️⃣  Test de l'endpoint racine /")
    try:
        response = requests.get(f"{base_url}/")
        if response.status_code == 200:
            print(f"✅ GET / - Status: {response.status_code}")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ GET / - Status: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Impossible de se connecter à l'API. Assurez-vous qu'elle est en cours d'exécution.")
        print("   Lancez: python main.py ou docker-compose up")
        return False
    
    # Test 2: Endpoint de création de startup
    print("\n2️⃣  Test de l'endpoint POST /create-startup")
    
    test_ideas = [
        "SaaS marketplace for freelancers",
        "AI-powered productivity tool",
        "Sustainable food delivery platform"
    ]
    
    for i, idea in enumerate(test_ideas, 1):
        print(f"\n   Test {i}: {idea}")
        
        payload = {"idea": idea}
        
        try:
            response = requests.post(
                f"{base_url}/create-startup",
                json=payload,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                print(f"   ✅ Status: {response.status_code}")
                
                data = response.json()
                roadmap = data.get("roadmap", {})
                
                print(f"   📋 Startup: {roadmap.get('startup_idea', 'N/A')}")
                print(f"   🎯 Epics: {len(roadmap.get('epics', []))}")
                print(f"   ⏱️  Timeline phases: {len(roadmap.get('timeline', {}))}")
                print(f"   📊 Metrics: {len(roadmap.get('success_metrics', []))}")
                
            else:
                print(f"   ❌ Status: {response.status_code}")
                print(f"   Error: {response.text}")
                return False
                
        except Exception as e:
            print(f"   ❌ Erreur: {str(e)}")
            return False
    
    print("\n" + "=" * 50)
    print("🎉 Tous les tests sont passés avec succès !")
    return True

def test_curl_commands():
    """Affiche les commandes curl pour tester l'API"""
    
    print("\n📡 Commandes curl pour tester l'API:")
    print("=" * 50)
    
    print("\n1. Test de santé:")
    print("   curl http://localhost:8000/")
    
    print("\n2. Création de startup:")
    print('   curl -X POST "http://localhost:8000/create-startup" \\')
    print('        -H "Content-Type: application/json" \\')
    print('        -d \'{"idea": "SaaS marketplace"}\'')
    
    print("\n3. Test avec une autre idée:")
    print('   curl -X POST "http://localhost:8000/create-startup" \\')
    print('        -H "Content-Type: application/json" \\')
    print('        -d \'{"idea": "AI productivity tool"}\'')

if __name__ == "__main__":
    print("🚀 Core Engine - Test de l'API")
    print("Assurez-vous que l'API est en cours d'exécution sur http://localhost:8000")
    print()
    
    # Test de l'API
    if test_api():
        test_curl_commands()
    else:
        print("\n❌ Certains tests ont échoué.")
        sys.exit(1)
