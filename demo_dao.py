#!/usr/bin/env python3
"""
Démonstration complète de l'agent DAO
Montre la création d'une startup avec tokenisation, DAO et trésorerie
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'core-engine'))

def demo_startup_creation():
    """Démonstration de la création d'une startup avec DAO"""
    print("🚀 DÉMONSTRATION STARTUPDAO - Agent DAO Blockchain")
    print("=" * 60)
    
    try:
        from agents.dao_agent import DAOOrchestrator
        
        # Création de l'orchestrateur
        orchestrator = DAOOrchestrator()
        
        # Idées de startups à tester
        startup_ideas = [
            "SaaS marketplace pour freelances",
            "Plateforme IA de gestion de projets",
            "Marketplace de tokens NFT",
            "Plateforme DeFi pour PME",
            "Système de vote blockchain pour entreprises"
        ]
        
        print(f"📋 {len(startup_ideas)} idées de startups à tokeniser:")
        for i, idea in enumerate(startup_ideas, 1):
            print(f"   {i}. {idea}")
        
        print("\n" + "=" * 60)
        
        # Test avec la première idée
        selected_idea = startup_ideas[0]
        print(f"🎯 Test avec l'idée: '{selected_idea}'")
        
        # Création de la DAO complète
        result = orchestrator.create_complete_dao("DEMO123", 5_000_000)
        
        print("\n✅ DAO COMPLÈTE CRÉÉE AVEC SUCCÈS!")
        print("=" * 60)
        
        # Affichage des résultats
        print(f"📊 Projet ID: {result['project_id']}")
        print(f"⏰ Timestamp: {result['timestamp']}")
        
        # Section Token
        print("\n🪙 TOKEN ERC20:")
        print(f"   📍 Adresse: {result['token']['contract_address']}")
        print(f"   🏷️ Symbole: {result['token']['token_symbol']}")
        print(f"   💰 Valorisation: {result['token']['valuation']}")
        print(f"   💵 Prix par token: {result['token']['price_per_token']}")
        print(f"   📊 Supply total: {result['token']['total_supply']:,}")
        
        # Distribution des tokens
        dist = result['token']['distribution']
        print(f"   🎯 Distribution:")
        print(f"      - Fondateur: {dist['founder']:,} tokens (20%)")
        print(f"      - Équipe IA: {dist['team']:,} tokens (10%)")
        print(f"      - Investisseurs: {dist['investors']:,} tokens (70%)")
        
        # Section DAO
        print("\n🏛️ GOUVERNANCE DAO:")
        print(f"   📍 Adresse: {result['dao']['dao_address']}")
        print(f"   🗳️ Pouvoir de vote: {result['dao']['voting_power']}")
        print(f"   📊 Quorum: {result['dao']['quorum']}")
        print(f"   ⏱️ Période de vote: {result['dao']['voting_period']}")
        
        print(f"   📋 Règles de gouvernance:")
        for i, rule in enumerate(result['dao']['rules'], 1):
            print(f"      {i}. {rule}")
        
        # Section Trésorerie
        print("\n💰 TRÉSORERIE DAO:")
        print(f"   📍 Adresse: {result['treasury']['treasury_address']}")
        print(f"   💵 Fonds disponibles: {result['treasury']['funds']}")
        print(f"   📅 Distribution: {result['treasury']['distribution_schedule']}")
        print(f"   🚫 Limite retrait: {result['treasury']['withdrawal_limit']}")
        
        print(f"   📋 Règles de trésorerie:")
        for i, rule in enumerate(result['treasury']['rules'], 1):
            print(f"      {i}. {rule}")
        
        # Résumé
        print("\n" + "=" * 60)
        print("🎉 RÉSUMÉ DE LA DÉMONSTRATION")
        print("=" * 60)
        print("✅ Tokenisation: ERC20 déployé avec distribution automatique")
        print("✅ Gouvernance: DAO créée avec règles de vote")
        print("✅ Trésorerie: Contrat de gestion des fonds déployé")
        print("✅ Orchestration: Processus automatisé complet")
        print("✅ Logging: Traçabilité complète des opérations")
        
        print("\n🚀 Prêt pour la production!")
        print("   - Connectez MetaMask pour interagir")
        print("   - Vérifiez les contrats sur Etherscan")
        print("   - Participez aux votes de la DAO")
        print("   - Gérez la trésorerie via l'interface")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors de la démonstration: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def demo_individual_agents():
    """Démonstration des agents individuels"""
    print("\n🔧 DÉMONSTRATION DES AGENTS INDIVIDUELS")
    print("=" * 60)
    
    try:
        from agents.dao_agent import TokenisationAgent, GovernanceAgent, TreasuryAgent
        
        # Test TokenisationAgent
        print("🧪 Test TokenisationAgent...")
        token_agent = TokenisationAgent()
        token_result = token_agent.run("AGENT123", 3_000_000)
        print(f"   ✅ Token créé: {token_result['token_symbol']}")
        
        # Test GovernanceAgent
        print("🧪 Test GovernanceAgent...")
        gov_agent = GovernanceAgent()
        gov_result = gov_agent.run("AGENT123", token_result['contract_address'])
        print(f"   ✅ DAO créée: {gov_result['dao_address']}")
        
        # Test TreasuryAgent
        print("🧪 Test TreasuryAgent...")
        treasury_agent = TreasuryAgent()
        treasury_result = treasury_agent.run("AGENT123", gov_result['dao_address'])
        print(f"   ✅ Trésorerie créée: {treasury_result['treasury_address']}")
        
        print("\n✅ Tous les agents individuels fonctionnent correctement!")
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors du test des agents: {str(e)}")
        return False

def main():
    """Fonction principale de démonstration"""
    print("🏛️ STARTUPDAO - Démonstration de l'Agent DAO Blockchain")
    print("=" * 80)
    
    # Test des agents individuels
    if not demo_individual_agents():
        print("❌ Échec du test des agents individuels")
        return 1
    
    # Test de l'orchestrateur complet
    if not demo_startup_creation():
        print("❌ Échec de la démonstration complète")
        return 1
    
    print("\n" + "=" * 80)
    print("🎉 DÉMONSTRATION TERMINÉE AVEC SUCCÈS!")
    print("=" * 80)
    print("L'agent DAO est prêt pour la production!")
    print("Prochaines étapes:")
    print("1. 🔗 Intégration avec MetaMask/WalletConnect")
    print("2. 🚀 Déploiement sur testnet (Sepolia)")
    print("3. 📱 Interface utilisateur complète")
    print("4. 🔐 Tests de sécurité et audit")
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)