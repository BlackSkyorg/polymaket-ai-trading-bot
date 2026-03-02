#!/usr/bin/env python3
"""
Main entry point to run the Polymarket AI Trading Agent
"""
import sys
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    """Main entry point"""
    try:
        from agents.polymarket.polymarket import Polymarket
        
        print("=" * 60)
        print("Polymarket AI Trading Agent")
        print("=" * 60)
        print()
        
        # Initialize Polymarket client
        print("Initializing Polymarket client...")
        polymarket = Polymarket()
        print("✓ Polymarket client initialized")
        print()
        
        # Test POL price API
        print("Testing POL price API...")
        try:
            pol_price = polymarket.get_pol_price()
            print(f"✓ POL Price: ${pol_price:.4f}")
        except Exception as e:
            print(f"⚠ POL Price API error: {e}")
        print()
        
        # Get USDC balance
        print("Checking USDC balance...")
        try:
            balance = polymarket.get_usdc_balance()
            print(f"✓ USDC Balance: ${balance:.2f}")
        except Exception as e:
            print(f"⚠ Balance check error: {e}")
        print()
        
        # Get markets
        print("Fetching markets...")
        try:
            markets = polymarket.get_all_markets()
            print(f"✓ Found {len(markets)} markets")
        except Exception as e:
            print(f"⚠ Markets fetch error: {e}")
        print()
        
        print("=" * 60)
        print("Project is running successfully!")
        print("=" * 60)
        print()
        print("To use the CLI, run:")
        print("  python -m scripts.python.cli --help")
        print()
        print("Available commands:")
        print("  - python -m scripts.python.cli get-all-markets")
        print("  - python -m scripts.python.cli get-all-events")
        print("  - python -m scripts.python.cli run-autonomous-trader")
        print()
        
        return 0
        
    except ImportError as e:
        print(f"✗ Import error: {e}")
        print("\nPlease install dependencies:")
        print("  pip install -e .")
        return 1
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
