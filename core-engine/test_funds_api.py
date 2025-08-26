#!/usr/bin/env python3
"""
Test script for the Funds API endpoints
"""

import requests
import json
import time

BASE_URL = "http://localhost:8000"

def test_create_fund():
    """Test creating a new fund"""
    print("🧪 Testing fund creation...")
    
    # Test data
    fund_data = {
        "startups": ["STK001", "STK002", "STK003"]
    }
    
    try:
        response = requests.post(f"{BASE_URL}/funds", json=fund_data)
        
        if response.status_code == 200:
            fund = response.json()
            print(f"✅ Fund created successfully!")
            print(f"   Symbol: {fund['fund_symbol']}")
            print(f"   Address: {fund['fund_address']}")
            print(f"   NAV: {fund['nav']}")
            print(f"   Composition: {len(fund['composition'])} startups")
            return fund
        else:
            print(f"❌ Failed to create fund: {response.status_code}")
            print(f"   Response: {response.text}")
            return None
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection error. Make sure the server is running on localhost:8000")
        return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def test_get_all_funds():
    """Test getting all funds"""
    print("\n🧪 Testing get all funds...")
    
    try:
        response = requests.get(f"{BASE_URL}/funds")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Retrieved {data['total_count']} funds")
            print(f"   Active: {data['active_count']}")
            
            for fund in data['funds']:
                print(f"   - {fund['fund_symbol']}: {fund['nav']} ({len(fund['composition'])} startups)")
            
            return data['funds']
        else:
            print(f"❌ Failed to get funds: {response.status_code}")
            return []
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return []

def test_get_fund_by_symbol(symbol):
    """Test getting a specific fund by symbol"""
    print(f"\n🧪 Testing get fund by symbol: {symbol}")
    
    try:
        response = requests.get(f"{BASE_URL}/funds/{symbol}")
        
        if response.status_code == 200:
            fund = response.json()
            print(f"✅ Fund retrieved successfully!")
            print(f"   Symbol: {fund['fund_symbol']}")
            print(f"   NAV: {fund['nav']}")
            print(f"   Status: {fund['status']}")
            return fund
        else:
            print(f"❌ Failed to get fund: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def test_update_fund_nav(symbol, new_nav):
    """Test updating fund NAV"""
    print(f"\n🧪 Testing NAV update for {symbol} to {new_nav}")
    
    try:
        response = requests.put(f"{BASE_URL}/funds/{symbol}/nav?nav={new_nav}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ NAV updated successfully!")
            print(f"   Message: {data['message']}")
            return True
        else:
            print(f"❌ Failed to update NAV: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_invalid_requests():
    """Test invalid requests"""
    print("\n🧪 Testing invalid requests...")
    
    # Test creating fund with less than 2 startups
    print("   Testing fund creation with 1 startup...")
    try:
        response = requests.post(f"{BASE_URL}/funds", json={"startups": ["STK001"]})
        if response.status_code == 400:
            print("   ✅ Correctly rejected fund with 1 startup")
        else:
            print(f"   ❌ Should have been rejected: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test getting non-existent fund
    print("   Testing get non-existent fund...")
    try:
        response = requests.get(f"{BASE_URL}/funds/INVALID")
        if response.status_code == 404:
            print("   ✅ Correctly returned 404 for non-existent fund")
        else:
            print(f"   ❌ Should have returned 404: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")

def main():
    """Run all tests"""
    print("🚀 Starting Funds API Tests")
    print("=" * 50)
    
    # Test 1: Create a fund
    fund = test_create_fund()
    if not fund:
        print("❌ Cannot continue tests without creating a fund")
        return
    
    # Wait a bit
    time.sleep(1)
    
    # Test 2: Get all funds
    funds = test_get_all_funds()
    
    # Test 3: Get specific fund
    test_get_fund_by_symbol(fund['fund_symbol'])
    
    # Test 4: Update fund NAV
    test_update_fund_nav(fund['fund_symbol'], "105.50 €")
    
    # Test 5: Get updated fund
    test_get_fund_by_symbol(fund['fund_symbol'])
    
    # Test 6: Test invalid requests
    test_invalid_requests()
    
    print("\n" + "=" * 50)
    print("🎉 All tests completed!")
    
    if fund:
        print(f"\n📊 Created fund summary:")
        print(f"   Symbol: {fund['fund_symbol']}")
        print(f"   Address: {fund['fund_address']}")
        print(f"   NAV: {fund['nav']}")
        print(f"   Composition:")
        for item in fund['composition']:
            print(f"     - {item['token']}: {item['weight']}")

if __name__ == "__main__":
    main()