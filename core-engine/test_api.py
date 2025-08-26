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