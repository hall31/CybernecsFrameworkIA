#!/usr/bin/env python3
"""
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