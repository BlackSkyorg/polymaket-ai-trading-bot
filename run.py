#!/usr/bin/env python3
"""
Main entry point to run the Polymarket AI Trading Agent
"""
import sys
import os

# Load environment variables FIRST, before adding stub path
from dotenv import load_dotenv
load_dotenv()

# Add stub packages path
stub_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'stub_packages')
if os.path.exists(stub_dir):
    sys.path.insert(0, stub_dir)

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
        print("[OK] Polymarket client initialized")
        print()
        
        print("----------------------->")
        try:
            pol_price = polymarket.get_pol_price()
            print(f"-------------------")
        except Exception as e:
            print(f"------------------")
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
        print(f"X Import error: {e}")
        print("\nPlease install dependencies:")
        print("  pip install -e .")
        return 1
    except Exception as e:
        print(f"X Error: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
