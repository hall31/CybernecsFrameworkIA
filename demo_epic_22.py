#!/usr/bin/env python3
"""
🚀 Démonstration EPIC 22: Constitution IA Globale

Ce script démontre le fonctionnement complet de l'épic 22,
incluant la génération de la constitution et l'affichage des résultats.
"""

import json
import sys
import os

# Ajouter le chemin du core-engine
sys.path.append(os.path.join(os.path.dirname(__file__), 'core-engine'))

def demo_constitution_agent():
    """Démonstration de l'agent Constitution"""
    print("🏛️ EPIC 22: Constitution IA Globale")
    print("=" * 50)
    
    try:
        # Importer et tester l'agent
        from agents.constitution_agent import ConstitutionAgent
        
        print("✅ Import de l'agent Constitution réussi")
        
        # Créer l'agent
        agent = ConstitutionAgent()
        print("✅ Agent Constitution initialisé")
        
        # Générer la constitution
        print("\n🔄 Génération de la constitution...")
        result = agent.run()
        
        # Afficher le résumé
        print("\n📊 Résumé de la Constitution:")
        print(f"   • Version: {result['summary']['version']}")
        print(f"   • Articles: {result['summary']['total_articles']}")
        print(f"   • Amendements: {result['summary']['total_amendments']}")
        
        # Afficher les articles par catégorie
        print("\n📋 Articles de la Constitution:")
        categories = {
            "droits_humains": "⚖️ Droits des Humains",
            "devoirs_ia": "🤖 Devoirs des IA",
            "gouvernance": "🧑‍🤝‍🧑 Gouvernance"
        }
        
        for category_id, category_name in categories.items():
            print(f"\n{category_name}:")
            category_articles = [a for a in result['constitution']['articles'] if a['category'] == category_id]
            
            for article in category_articles:
                priority_emoji = "🔴" if article['priority'] == "Critique" else "🟠" if article['priority'] == "Élevée" else "🔵"
                print(f"   {priority_emoji} {article['id']}: {article['title']} ({article['priority']})")
        
        # Afficher les amendements
        print("\n✏️ Amendements Proposés:")
        for amendment in result['constitution']['amendments']:
            print(f"   📝 {amendment['id']}: {amendment['title']}")
            print(f"      Majorité requise: {amendment['required_majority']}")
            print(f"      Statut: {amendment['status']}")
        
        # Afficher la gouvernance
        print("\n🏛️ Mécanismes de Gouvernance:")
        governance = result['constitution']['governance']
        print(f"   • Structure: {governance['structure']}")
        print(f"   • Mécanisme de vote: {governance['voting_mechanism']}")
        print(f"   • Cycle de révision: {governance['review_cycle']}")
        
        # Sauvegarder la constitution
        output_file = "constitution_generated.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        
        print(f"\n💾 Constitution sauvegardée dans: {output_file}")
        
        # Afficher un extrait du Markdown
        print("\n📝 Extrait du document Markdown:")
        markdown_lines = result['markdown'].split('\n')
        for i, line in enumerate(markdown_lines[:10]):
            print(f"   {line}")
        if len(markdown_lines) > 10:
            print("   ...")
        
        print("\n🎉 Démonstration terminée avec succès!")
        return True
        
    except ImportError as e:
        print(f"❌ Erreur d'import: {e}")
        print("   Assurez-vous d'être dans le bon répertoire et que l'agent est installé")
        return False
        
    except Exception as e:
        print(f"❌ Erreur lors de la démonstration: {e}")
        import traceback
        traceback.print_exc()
        return False

def demo_dashboard_setup():
    """Démonstration de la configuration du dashboard"""
    print("\n" + "=" * 50)
    print("🖥️ Configuration du Dashboard React")
    print("=" * 50)
    
    dashboard_dir = "dashboard"
    if os.path.exists(dashboard_dir):
        print(f"✅ Répertoire dashboard trouvé: {dashboard_dir}")
        
        # Vérifier les composants
        components = [
            "src/components/ConstitutionPage.jsx",
            "src/components/Sidebar.jsx",
            "src/App.jsx"
        ]
        
        for component in components:
            component_path = os.path.join(dashboard_dir, component)
            if os.path.exists(component_path):
                print(f"✅ Composant trouvé: {component}")
            else:
                print(f"❌ Composant manquant: {component}")
        
        # Vérifier les données
        data_file = os.path.join(dashboard_dir, "src/data/constitution.json")
        if os.path.exists(data_file):
            print(f"✅ Données de constitution trouvées: {data_file}")
        else:
            print(f"❌ Données de constitution manquantes: {data_file}")
        
        print("\n🚀 Pour démarrer le dashboard:")
        print(f"   cd {dashboard_dir}")
        print("   npm install")
        print("   npm run dev")
        
    else:
        print(f"❌ Répertoire dashboard non trouvé: {dashboard_dir}")

def main():
    """Fonction principale de démonstration"""
    print("🌟 Démonstration EPIC 22: Constitution IA Globale")
    print("=" * 60)
    
    # Test de l'agent Constitution
    success = demo_constitution_agent()
    
    if success:
        # Configuration du dashboard
        demo_dashboard_setup()
        
        print("\n" + "=" * 60)
        print("🎯 Prochaines étapes:")
        print("1. Démarrer le serveur backend: cd core-engine && python main.py")
        print("2. Démarrer le dashboard: cd dashboard && npm run dev")
        print("3. Ouvrir http://localhost:5173 dans votre navigateur")
        print("4. Naviguer vers la page Constitution")
        print("=" * 60)
    else:
        print("\n❌ La démonstration a échoué. Vérifiez la configuration.")

if __name__ == "__main__":
    main()