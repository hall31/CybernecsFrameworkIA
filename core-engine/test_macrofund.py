#!/usr/bin/env python3
"""
Test script for MacroFundAgent and related endpoints
"""

import asyncio
import json
from datetime import datetime
from agents.macrofund_agent import MacroFundAgent
from agents.global_trader_contract import GlobalTraderContract

async def test_macrofund_agent():
    """Test the MacroFundAgent functionality"""
    print("🧪 Testing MacroFundAgent...")
    
    # Initialize agent
    agent = MacroFundAgent()
    
    # Test portfolio summary
    print("\n📊 Portfolio Summary:")
    summary = agent.get_portfolio_summary()
    print(json.dumps(summary, indent=2, default=str))
    
    # Test hedge status
    print("\n🛡️ Hedge Status:")
    hedge_status = agent.get_hedge_status()
    print(json.dumps(hedge_status, indent=2, default=str))
    
    # Test full execution
    print("\n🚀 Executing Macro Fund Analysis...")
    try:
        result = await agent.run()
        print("✅ Macro Fund execution successful!")
        print(f"📈 Portfolio Value: {result['portfolio_value']}")
        print(f"🔄 Arbitrages executed: {len(result['recent_arbitrages'])}")
        print(f"📊 Allocations: {result['allocations']}")
    except Exception as e:
        print(f"❌ Error during execution: {e}")

def test_global_trader():
    """Test the GlobalTraderContract functionality"""
    print("\n🧪 Testing GlobalTraderContract...")
    
    # Initialize contract
    trader = GlobalTraderContract()
    
    # Test buy operation
    print("\n📈 Testing BUY operation...")
    buy_result = trader.buy("BTC", 1000000)  # 1M €
    print(f"Buy result: {json.dumps(buy_result, indent=2, default=str)}")
    
    # Test sell operation
    print("\n📉 Testing SELL operation...")
    sell_result = trader.sell("BTC", 500000)  # 500k €
    print(f"Sell result: {json.dumps(sell_result, indent=2, default=str)}")
    
    # Test portfolio summary
    print("\n📊 Portfolio Summary:")
    portfolio = trader.get_portfolio_summary()
    print(json.dumps(portfolio, indent=2, default=str))
    
    # Test rebalancing
    print("\n⚖️ Testing Macro Rebalancing...")
    target_allocations = {
        "IA Startups": 0.35,
        "ETF IA": 0.20,
        "Crypto": 0.30,
        "Stocks": 0.10,
        "Commodities": 0.05
    }
    rebalance_result = trader.rebalance_macro(target_allocations, 50000000)
    print(f"Rebalance result: {json.dumps(rebalance_result, indent=2, default=str)}")

async def test_api_endpoints():
    """Test the API endpoints"""
    print("\n🧪 Testing API Endpoints...")
    
    import aiohttp
    
    async with aiohttp.ClientSession() as session:
        # Test GET /macrofund
        print("\n📡 Testing GET /macrofund...")
        try:
            async with session.get('http://localhost:8000/macrofund') as response:
                if response.status == 200:
                    data = await response.json()
                    print("✅ GET /macrofund successful!")
                    print(f"📊 Portfolio Value: {data['portfolio_value']}")
                    print(f"🔄 Arbitrages: {len(data['recent_arbitrages'])}")
                else:
                    print(f"❌ GET /macrofund failed with status {response.status}")
        except Exception as e:
            print(f"❌ Error testing GET /macrofund: {e}")
        
        # Test POST /macrofund/execute
        print("\n📡 Testing POST /macrofund/execute...")
        try:
            async with session.post('http://localhost:8000/macrofund/execute') as response:
                if response.status == 200:
                    data = await response.json()
                    print("✅ POST /macrofund/execute successful!")
                    print(f"📊 Result: {data['message']}")
                else:
                    print(f"❌ POST /macrofund/execute failed with status {response.status}")
        except Exception as e:
            print(f"❌ Error testing POST /macrofund/execute: {e}")

def main():
    """Main test function"""
    print("🚀 Starting MacroFund Tests...")
    print("=" * 50)
    
    # Test agents
    asyncio.run(test_macrofund_agent())
    test_global_trader()
    
    # Test API endpoints (only if server is running)
    print("\n" + "=" * 50)
    print("🌐 Testing API Endpoints (requires server to be running)...")
    try:
        asyncio.run(test_api_endpoints())
    except Exception as e:
        print(f"⚠️ API tests skipped (server not running): {e}")
    
    print("\n✅ All tests completed!")

if __name__ == "__main__":
    main()