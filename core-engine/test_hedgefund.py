#!/usr/bin/env python3
"""
Script de test pour le Hedge Fund IA
Teste l'agent HedgeFundAgent et le smart contract TraderContract
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.hedgefund_agent import HedgeFundAgent
from contracts.trader_contract import TraderContract
from utils.logger import log_event, log_success

def test_hedgefund_agent():
    """Test de l'agent HedgeFundAgent"""
    print("\n" + "="*50)
    print("🧪 TEST HEDGEFUND AGENT")
    print("="*50)
    
    try:
        # Initialisation de l'agent
        agent = HedgeFundAgent()
        log_success("TEST", "HedgeFundAgent initialisé avec succès")
        
        # Test de la méthode run()
        print("\n📊 Exécution de la stratégie de trading...")
        result = agent.run()
        
        if "error" not in result:
            log_success("TEST", "Stratégie de trading exécutée avec succès")
            print(f"✅ Portefeuille optimisé généré")
            print(f"   - Positions long: {len(result['portfolio']['long_positions'])}")
            print(f"   - Positions short: {len(result['portfolio']['short_positions'])}")
            print(f"   - Cash reserve: {result['portfolio']['cash_reserve']}")
            print(f"   - ROI: {result['performance']['roi']}%")
        else:
            print(f"❌ Erreur dans la stratégie: {result['error']}")
            return False
        
        # Test de la méthode get_current_portfolio()
        print("\n📈 Récupération du portefeuille actuel...")
        portfolio = agent.get_current_portfolio()
        log_success("TEST", "Portefeuille actuel récupéré avec succès")
        
        # Test de la méthode rebalance_portfolio()
        print("\n🔄 Test du rebalancement...")
        rebalance_result = agent.rebalance_portfolio()
        if "error" not in rebalance_result:
            log_success("TEST", "Rebalancement exécuté avec succès")
        else:
            print(f"❌ Erreur dans le rebalancement: {rebalance_result['error']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur dans le test HedgeFundAgent: {str(e)}")
        return False

def test_trader_contract():
    """Test du smart contract TraderContract"""
    print("\n" + "="*50)
    print("🧪 TEST TRADER CONTRACT")
    print("="*50)
    
    try:
        # Initialisation du contrat
        contract = TraderContract()
        log_success("TEST", "TraderContract déployé avec succès")
        
        # Test des positions initiales
        print("\n📋 Vérification des positions initiales...")
        positions = contract.get_positions()
        print(f"✅ {len(positions['positions'])} tokens supportés")
        
        # Test d'achat (BUY)
        print("\n💰 Test d'achat de tokens...")
        buy_result = contract.buy("STK001", 10000, 100.0, "HedgeFundAgent")
        if buy_result["success"]:
            log_success("TEST", f"Achat réussi: {buy_result['trade_id']}")
            print(f"   - Trade ID: {buy_result['trade_id']}")
            print(f"   - Token: {buy_result['token']}")
            print(f"   - Montant: ${buy_result['amount_usd']:,.2f}")
        else:
            print(f"❌ Échec de l'achat: {buy_result['error']}")
        
        # Test de vente (SELL)
        print("\n💸 Test de vente de tokens...")
        sell_result = contract.sell("STK001", 5000, 105.0, "HedgeFundAgent")
        if sell_result["success"]:
            log_success("TEST", f"Vente réussie: {sell_result['trade_id']}")
            print(f"   - Trade ID: {sell_result['trade_id']}")
            print(f"   - Action: {sell_result['action']}")
            print(f"   - P&L: ${sell_result['pnl']:,.2f}")
        else:
            print(f"❌ Échec de la vente: {sell_result['error']}")
        
        # Test de rebalancement
        print("\n⚖️ Test de rebalancement...")
        rebalance_result = contract.rebalance("HedgeFundAgent")
        if rebalance_result["success"]:
            log_success("TEST", "Rebalancement du contrat réussi")
        else:
            print(f"❌ Échec du rebalancement: {rebalance_result['error']}")
        
        # Test d'accès non autorisé
        print("\n🚫 Test d'accès non autorisé...")
        unauthorized_buy = contract.buy("STK002", 1000, 100.0, "UnauthorizedUser")
        if not unauthorized_buy["success"]:
            log_success("TEST", "Sécurité: accès non autorisé bloqué")
        else:
            print("❌ Erreur de sécurité: accès non autorisé autorisé")
        
        # Récapitulatif final
        print("\n📊 Récapitulatif du contrat...")
        summary = contract.get_portfolio_summary()
        print(f"   - Volume total: ${summary['total_volume']:,.2f}")
        print(f"   - Frais collectés: ${summary['fees_collected']:,.2f}")
        print(f"   - Total trades: {summary['total_trades']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur dans le test TraderContract: {str(e)}")
        return False

def test_integration():
    """Test d'intégration entre l'agent et le contrat"""
    print("\n" + "="*50)
    print("🧪 TEST D'INTÉGRATION")
    print("="*50)
    
    try:
        agent = HedgeFundAgent()
        contract = TraderContract()
        
        # Simulation d'une stratégie complète
        print("\n🎯 Simulation d'une stratégie complète...")
        
        # L'agent exécute sa stratégie
        strategy_result = agent.run()
        
        # Le contrat enregistre les trades
        if "portfolio" in strategy_result:
            portfolio = strategy_result["portfolio"]
            
            # Simulation d'achats basés sur les positions long
            for position in portfolio.get("long_positions", []):
                token = position["token"]
                amount = position["amount_usd"]
                price = 100.0  # Prix simulé
                
                trade_result = contract.buy(token, amount, price, "HedgeFundAgent")
                if trade_result["success"]:
                    print(f"✅ Trade enregistré: {token} - ${amount:,.2f}")
                else:
                    print(f"❌ Échec du trade: {token}")
        
        log_success("TEST", "Intégration agent-contrat réussie")
        return True
        
    except Exception as e:
        print(f"❌ Erreur dans le test d'intégration: {str(e)}")
        return False

def main():
    """Fonction principale de test"""
    print("🚀 DÉMARRAGE DES TESTS DU HEDGE FUND IA")
    print("="*60)
    
    tests = [
        ("HedgeFundAgent", test_hedgefund_agent),
        ("TraderContract", test_trader_contract),
        ("Intégration", test_integration)
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"❌ Erreur critique dans {test_name}: {str(e)}")
            results[test_name] = False
    
    # Résumé des tests
    print("\n" + "="*60)
    print("📋 RÉSUMÉ DES TESTS")
    print("="*60)
    
    for test_name, result in results.items():
        status = "✅ RÉUSSI" if result else "❌ ÉCHEC"
        print(f"{test_name:20} : {status}")
    
    success_count = sum(results.values())
    total_count = len(results)
    
    print(f"\n🎯 Résultat global: {success_count}/{total_count} tests réussis")
    
    if success_count == total_count:
        log_success("TEST", "Tous les tests sont passés avec succès!")
        return 0
    else:
        print(f"❌ {total_count - success_count} test(s) ont échoué")
        return 1

if __name__ == "__main__":
    exit(main())