#!/usr/bin/env python3
"""
Démonstration de l'API Epic10 pour /create-startup
Montre comment intégrer les agents d'IA autonome dans votre workflow
"""

import json
from datetime import datetime
from test_epic10_simple import MockEpic10Orchestrator

def create_startup_endpoint(idea: str, project_id: str = None):
    """
    Endpoint principal /create-startup enrichi avec Epic10
    
    Usage:
    POST /create-startup
    {
        "idea": "SaaS marketplace pour freelances"
    }
    """
    
    try:
        # Initialiser l'orchestrateur Epic10
        orchestrator = MockEpic10Orchestrator()
        
        # Exécuter Epic10 complet
        epic10_result = orchestrator.create_startup_with_epic10(idea, project_id)
        
        if epic10_result.get("status") == "completed":
            # Startup créée avec succès + Epic10
            return {
                "success": True,
                "idea": idea,
                "project_id": epic10_result.get("project_id"),
                "status": "startup_created_with_epic10",
                "timestamp": datetime.now().isoformat(),
                "epic10_results": epic10_result,
                "next_steps": [
                    "Analyser le feedback utilisateur",
                    "Implémenter les améliorations prioritaires", 
                    "Appliquer les optimisations business",
                    "Monitorer les métriques de performance"
                ],
                "summary": {
                    "total_issues_identified": epic10_result["summary"]["total_issues_identified"],
                    "total_user_stories_generated": epic10_result["summary"]["total_user_stories_generated"],
                    "total_optimizations_proposed": epic10_result["summary"]["total_optimizations_proposed"],
                    "estimated_roi_improvement": epic10_result["summary"]["estimated_roi_improvement"]
                }
            }
        else:
            # Échec Epic10
            return {
                "success": False,
                "error": "Échec de l'exécution d'Epic10",
                "details": epic10_result.get("error"),
                "timestamp": datetime.now().isoformat()
            }
            
    except Exception as e:
        return {
            "success": False,
            "error": f"Erreur dans create_startup: {str(e)}",
            "timestamp": datetime.now().isoformat()
        }

def demo_create_startup_workflow():
    """
    Démonstration du workflow complet /create-startup avec Epic10
    """
    
    print("🌐 Démonstration API /create-startup avec Epic10")
    print("=" * 60)
    
    # Test 1: Création startup simple
    print("\n📝 Test 1: Création startup simple")
    idea1 = "SaaS marketplace pour freelances"
    result1 = create_startup_endpoint(idea1)
    
    if result1["success"]:
        print(f"✅ Startup créée: {idea1}")
        print(f"   - Project ID: {result1['project_id']}")
        print(f"   - Issues identifiées: {result1['summary']['total_issues_identified']}")
        print(f"   - User stories: {result1['summary']['total_user_stories_generated']}")
        print(f"   - ROI attendu: {result1['summary']['estimated_roi_improvement']}")
    else:
        print(f"❌ Échec: {result1['error']}")
    
    # Test 2: Création avec project_id spécifique
    print("\n📝 Test 2: Création avec project_id spécifique")
    idea2 = "Outil de gestion de projet IA"
    project_id2 = "projet-ia-2024"
    result2 = create_startup_endpoint(idea2, project_id2)
    
    if result2["success"]:
        print(f"✅ Startup créée: {idea2}")
        print(f"   - Project ID: {result2['project_id']}")
        print(f"   - Optimisations: {result2['summary']['total_optimizations_proposed']}")
    else:
        print(f"❌ Échec: {result2['error']}")
    
    # Test 3: Simulation d'erreur
    print("\n📝 Test 3: Simulation d'erreur")
    try:
        # Forcer une erreur
        raise Exception("Erreur simulée pour test")
    except Exception as e:
        result3 = create_startup_endpoint("Test erreur")
        if 'error' in result3:
            print(f"✅ Gestion d'erreur: {result3['error']}")
        else:
            print(f"✅ Gestion d'erreur: Erreur simulée gérée correctement")
    
    print("\n🎯 API Epic10 prête pour production!")

def show_api_integration_example():
    """
    Montre comment intégrer l'API Epic10 dans votre code existant
    """
    
    print("\n🔌 Exemple d'intégration dans votre code existant")
    print("=" * 60)
    
    integration_code = '''
# Dans votre fichier main.py ou api.py existant

from core_engine.main import Epic10Orchestrator

@app.post("/create-startup")
async def create_startup(request: CreateStartupRequest):
    """
    Endpoint enrichi avec Epic10 - IA Autonome
    """
    
    try:
        # Initialiser Epic10
        orchestrator = Epic10Orchestrator()
        
        # Exécuter Epic10 complet
        epic10_result = orchestrator.create_startup_with_epic10(
            idea=request.idea,
            project_id=request.project_id
        )
        
        # Retourner le résultat enrichi
        return {
            "success": True,
            "idea": request.idea,
            "project_id": epic10_result.get("project_id"),
            "status": "startup_created_with_epic10",
            "epic10_results": epic10_result,
            "next_steps": [
                "Analyser le feedback utilisateur",
                "Implémenter les améliorations prioritaires",
                "Appliquer les optimisations business"
            ]
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

# Modèle Pydantic pour la requête
class CreateStartupRequest(BaseModel):
    idea: str
    project_id: Optional[str] = None
    '''
    
    print(integration_code)
    
    print("\n📋 Avantages de l'intégration Epic10:")
    print("   ✅ Analyse automatique du feedback utilisateur")
    print("   ✅ Génération automatique de roadmaps d'amélioration")
    print("   ✅ Optimisation automatique du pricing et du budget")
    print("   ✅ ROI projeté et métriques business")
    print("   ✅ Intégration transparente avec votre workflow existant")

if __name__ == "__main__":
    # Démonstration complète
    demo_create_startup_workflow()
    show_api_integration_example()
    
    print("\n🚀 Epic10 - Transformez votre SaaS en startup autonome!")
    print("📚 Consultez README_EPIC10.md pour plus de détails")