#!/usr/bin/env python3
"""
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
