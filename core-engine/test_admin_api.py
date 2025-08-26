#!/usr/bin/env python3
"""
Tests pour l'API Admin FastAPI
Ce script teste les principales fonctionnalités de l'API
"""

import requests
import json
import time

# Configuration
BASE_URL = "http://localhost:8000"
HEADERS = {"Content-Type": "application/json"}

def test_health():
    """Test du endpoint de santé"""
    print("🏥 Test du endpoint de santé...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Santé OK - Agents: {data['agents_count']}, Épics: {data['epics_count']}")
            return True
        else:
            print(f"❌ Erreur santé: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Erreur connexion: {e}")
        return False

def test_agents():
    """Test des endpoints des agents"""
    print("\n🤖 Test des endpoints des agents...")
    
    # Liste des agents
    try:
        response = requests.get(f"{BASE_URL}/agents")
        if response.status_code == 200:
            agents = response.json()
            print(f"✅ Liste des agents récupérée: {len(agents)} agents")
            
            # Test d'un agent spécifique
            if agents:
                first_agent = agents[0]['name']
                response = requests.get(f"{BASE_URL}/agents/{first_agent}")
                if response.status_code == 200:
                    print(f"✅ Agent {first_agent} récupéré")
                else:
                    print(f"❌ Erreur récupération agent {first_agent}")
        else:
            print(f"❌ Erreur liste agents: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Erreur agents: {e}")
        return False
    
    return True

def test_epics():
    """Test des endpoints des épics"""
    print("\n📋 Test des endpoints des épics...")
    
    try:
        response = requests.get(f"{BASE_URL}/epics")
        if response.status_code == 200:
            epics = response.json()
            print(f"✅ Liste des épics récupérée: {len(epics)} épics")
            
            # Test d'une épic spécifique
            if epics:
                first_epic = epics[0]['id']
                response = requests.get(f"{BASE_URL}/epics/{first_epic}")
                if response.status_code == 200:
                    print(f"✅ Épic {first_epic} récupérée")
                else:
                    print(f"❌ Erreur récupération épic {first_epic}")
        else:
            print(f"❌ Erreur liste épics: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Erreur épics: {e}")
        return False
    
    return True

def test_toggle_agent():
    """Test du toggle d'un agent"""
    print("\n🔄 Test du toggle d'un agent...")
    
    try:
        # Récupérer la liste des agents
        response = requests.get(f"{BASE_URL}/agents")
        if response.status_code != 200:
            print("❌ Impossible de récupérer la liste des agents")
            return False
        
        agents = response.json()
        if not agents:
            print("❌ Aucun agent disponible")
            return False
        
        # Prendre le premier agent
        test_agent = agents[0]['name']
        initial_state = agents[0]['enabled']
        
        print(f"🔄 Test du toggle de l'agent {test_agent} (état initial: {initial_state})")
        
        # Toggle l'agent
        response = requests.post(f"{BASE_URL}/agents/{test_agent}/toggle")
        if response.status_code == 200:
            data = response.json()
            new_state = data['enabled']
            print(f"✅ Agent {test_agent} togglé: {initial_state} -> {new_state}")
            
            # Remettre dans l'état initial
            if new_state != initial_state:
                response = requests.post(f"{BASE_URL}/agents/{test_agent}/toggle")
                if response.status_code == 200:
                    print(f"✅ Agent {test_agent} remis dans l'état initial")
                else:
                    print(f"⚠️ Impossible de remettre l'agent dans l'état initial")
            
            return True
        else:
            print(f"❌ Erreur toggle agent: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Erreur toggle agent: {e}")
        return False

def test_system_status():
    """Test du statut système"""
    print("\n📊 Test du statut système...")
    
    try:
        response = requests.get(f"{BASE_URL}/status")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Statut système récupéré:")
            print(f"   - Agents: {data['agents']['active']}/{data['agents']['total']} actifs")
            print(f"   - Épics: {data['epics']['idle']} idle, {data['epics']['running']} running, {data['epics']['done']} done")
            return True
        else:
            print(f"❌ Erreur statut système: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Erreur statut système: {e}")
        return False

def main():
    """Fonction principale de test"""
    print("🧪 Tests de l'API Admin FastAPI")
    print("=" * 50)
    
    # Vérifier que l'API est accessible
    if not test_health():
        print("\n❌ L'API n'est pas accessible. Assurez-vous qu'elle est démarrée sur le port 8000.")
        print("💡 Lancez: python run_admin_api.py")
        return
    
    # Tests des fonctionnalités
    tests = [
        test_agents,
        test_epics,
        test_toggle_agent,
        test_system_status
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ Test {test.__name__} a échoué avec une exception: {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 Résultats: {passed}/{total} tests réussis")
    
    if passed == total:
        print("🎉 Tous les tests sont passés ! L'API fonctionne parfaitement.")
    else:
        print("⚠️ Certains tests ont échoué. Vérifiez les logs de l'API.")

if __name__ == "__main__":
    main()