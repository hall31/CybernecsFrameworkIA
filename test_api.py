#!/usr/bin/env python3
"""
Script de test pour l'API Flask
"""

import requests
import json
import time

def test_api():
    """Teste l'API Flask"""
    base_url = "http://localhost:5000"
    
    print("🧪 Test de l'API Flask...")
    
    # Test de santé
    print("\n1. Test de l'endpoint /health...")
    try:
        response = requests.get(f"{base_url}/health", timeout=5)
        if response.status_code == 200:
            print("✅ Health check réussi:", response.json())
        else:
            print("❌ Health check échoué:", response.status_code)
            return
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur de connexion: {e}")
        return
    
    # Test de création de startup
    print("\n2. Test de l'endpoint /create-startup...")
    try:
        payload = {"idea": "SaaS e-commerce"}
        response = requests.post(
            f"{base_url}/create-startup",
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Startup créée avec succès!")
            print("📊 Roadmap:", json.dumps(result.get("roadmap", {}), indent=2, ensure_ascii=False))
            print("🔧 Stack technique:", json.dumps(result.get("technical_stack", {}), indent=2, ensure_ascii=False))
        else:
            print(f"❌ Erreur lors de la création: {response.status_code}")
            print("Réponse:", response.text)
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur de connexion: {e}")
    
    print("\n🎉 Test de l'API terminé!")

if __name__ == "__main__":
    test_api()