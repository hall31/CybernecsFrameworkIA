#!/usr/bin/env python3
"""
Test script for PlanetaryAgent
Tests the global governance AI system
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.planetary_agent import PlanetaryAgent
from utils.logger import log_event

def test_planetary_agent():
    """Test the PlanetaryAgent functionality"""
    print("🧪 Testing PlanetaryAgent...")
    
    try:
        # Initialize the agent
        print("1. Initializing PlanetaryAgent...")
        agent = PlanetaryAgent()
        print(f"✅ Agent initialized: {agent.name}")
        
        # Test basic functionality
        print("\n2. Testing basic functionality...")
        print(f"   - Sovereign funds count: {len(agent.sovereign_funds)}")
        print(f"   - Global DAO members: {len(agent.global_dao.members)}")
        print(f"   - Active proposals: {len(agent.global_dao.get_active_proposals())}")
        
        # Test planetary analysis
        print("\n3. Testing planetary analysis...")
        result = agent.run()
        
        print(f"   - Active sovereign funds: {result['active_sovereign_funds']}")
        print(f"   - Total countries: {result['summary']['total_countries']}")
        print(f"   - Total zones: {result['summary']['total_zones']}")
        print(f"   - Global population: {result['summary']['global_population']}")
        print(f"   - Total GDP: {result['summary']['total_gdp']}")
        
        # Test governance plan
        print("\n4. Testing governance plan...")
        governance_plan = result['governance_plan']
        print(f"   - Planet value: {governance_plan['planet_value']}")
        print(f"   - Allocations: {governance_plan['allocations']}")
        print(f"   - Global goals count: {len(governance_plan['global_goals'])}")
        
        # Test DAO functionality
        print("\n5. Testing DAO functionality...")
        dao_state = result['global_dao_state']
        print(f"   - Total members: {dao_state['total_members']}")
        print(f"   - Total voting power: {dao_state['total_voting_power']:.2f}")
        print(f"   - Active proposals: {dao_state['active_proposals']}")
        
        # Test voting system
        print("\n6. Testing voting system...")
        if dao_state['proposals']:
            first_proposal = dao_state['proposals'][0]
            print(f"   - Testing vote on proposal: {first_proposal['id']}")
            
            # Test voting
            success = agent.global_dao.vote(first_proposal['id'], "France", "for")
            print(f"   - Vote recorded: {success}")
            
            # Check updated votes
            updated_proposal = next(p for p in dao_state['proposals'] if p['id'] == first_proposal['id'])
            print(f"   - Votes for: {updated_proposal['votes_for']:.2f}")
        
        # Test status retrieval
        print("\n7. Testing status retrieval...")
        status = agent.get_planetary_status()
        print(f"   - Planet value: {status['planet_value']}")
        print(f"   - Active funds: {status['active_funds_count']}")
        print(f"   - DAO members: {status['dao_members_count']}")
        
        print("\n✅ All tests passed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed with error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def test_sovereign_funds():
    """Test SovereignFundAgent functionality"""
    print("\n🧪 Testing SovereignFundAgent...")
    
    try:
        from agents.planetary_agent import SovereignFundAgent
        
        # Create a test fund
        fund = SovereignFundAgent("TestCountry", "TestZone")
        print(f"✅ Fund created: {fund.country} in {fund.zone}")
        
        # Test status
        status = fund.get_status()
        print(f"   - Status: {status['status']}")
        print(f"   - Energy: {status['resources']['energy']:.2f} TWh")
        print(f"   - Water: {status['resources']['water']:.2f} km³")
        print(f"   - Health: {status['resources']['health']:.3f}")
        print(f"   - Agriculture: {status['resources']['agriculture']:.3f}")
        print(f"   - Population: {status['resources']['population']:.1f}M")
        print(f"   - GDP: {status['resources']['gdp']:.2f} trillion €")
        
        print("✅ SovereignFundAgent tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ SovereignFundAgent test failed: {str(e)}")
        return False

def test_global_dao():
    """Test GlobalDAO functionality"""
    print("\n🧪 Testing GlobalDAO...")
    
    try:
        from agents.planetary_agent import GlobalDAO
        
        # Create DAO
        dao = GlobalDAO()
        print("✅ GlobalDAO created")
        
        # Add members
        dao.add_member("TestCountry1", 100)
        dao.add_member("TestCountry2", 200)
        print(f"   - Members added: {len(dao.members)}")
        
        # Create proposal
        proposal_id = dao.create_proposal("Test Proposal", "Test description", "Test Category")
        print(f"   - Proposal created: {proposal_id}")
        
        # Test voting
        dao.vote(proposal_id, "TestCountry1", "for")
        dao.vote(proposal_id, "TestCountry2", "against")
        print("   - Votes recorded")
        
        # Check results
        proposal = next(p for p in dao.proposals if p['id'] == proposal_id)
        print(f"   - Votes for: {proposal['votes_for']}")
        print(f"   - Votes against: {proposal['votes_against']}")
        
        # Get DAO state
        state = dao.get_dao_state()
        print(f"   - Total voting power: {state['total_voting_power']}")
        print(f"   - Active proposals: {state['active_proposals']}")
        
        print("✅ GlobalDAO tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ GlobalDAO test failed: {str(e)}")
        return False

if __name__ == "__main__":
    print("🚀 Starting PlanetaryAgent Test Suite")
    print("=" * 50)
    
    # Run all tests
    tests = [
        test_sovereign_funds,
        test_global_dao,
        test_planetary_agent
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! PlanetaryAgent is working correctly.")
        sys.exit(0)
    else:
        print("❌ Some tests failed. Please check the errors above.")
        sys.exit(1)