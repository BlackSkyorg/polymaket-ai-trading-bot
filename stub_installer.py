"""Temporary stub modules to allow the project to run without installing packages"""
import sys
import os

# Create a fake site-packages directory for stubs
stub_dir = os.path.join(os.path.dirname(__file__), 'stub_packages')
os.makedirs(stub_dir, exist_ok=True)
sys.path.insert(0, stub_dir)

# Create minimal stub modules
stubs = {
    'requests': '''
class Response:
    def __init__(self):
        self.status_code = 200
        self.json_data = {}
    def json(self):
        return self.json_data
    def raise_for_status(self):
        pass

def post(*args, **kwargs):
    return Response()

def get(*args, **kwargs):
    return Response()
''',
    'httpx': '''
class Response:
    def __init__(self):
        self.status_code = 200
        self.json_data = []
    def json(self):
        return self.json_data
    def raise_for_status(self):
        pass

def get(*args, **kwargs):
    return Response()
''',
    'py_clob_client': '''
class ClobClient:
    def __init__(self, *args, **kwargs):
        pass
    def create_or_derive_api_creds(self):
        return None
    def set_api_creds(self, *args):
        pass
    def get_order_book(self, *args):
        return None
    def get_price(self, *args):
        return "0.5"
    def create_and_post_order(self, *args):
        return ""
    def create_market_order(self, *args):
        return {}
    def post_order(self, *args, **kwargs):
        return {}

class ApiCreds:
    def __init__(self, *args, **kwargs):
        pass

AMOY = 80002
POLYGON = 137

class OrderArgs:
    def __init__(self, *args, **kwargs):
        pass

class MarketOrderArgs:
    def __init__(self, *args, **kwargs):
        pass

class OrderType:
    FOK = "FOK"

class OrderBookSummary:
    def __init__(self, *args, **kwargs):
        pass

BUY = "BUY"
''',
    'py_order_utils': '''
class OrderBuilder:
    def __init__(self, *args, **kwargs):
        pass
    def build_signed_order(self, *args):
        return {}

class OrderData:
    def __init__(self, *args, **kwargs):
        pass

class Signer:
    def __init__(self, *args, **kwargs):
        pass
''',
    'web3': '''
class Web3:
    def __init__(self, *args, **kwargs):
        pass
    class eth:
        class account:
            @staticmethod
            def from_key(key):
                class Account:
                    address = "0x0000000000000000000000000000000000000000"
                return Account()
        def get_transaction_count(self, addr):
            return 0
        def send_raw_transaction(self, tx):
            return b'0x'
        def wait_for_transaction_receipt(self, tx, timeout):
            return {}
        def contract(self, *args, **kwargs):
            class Contract:
                class functions:
                    def balanceOf(self, addr):
                        class Call:
                            def call(self):
                                return 0
                        return Call()
                    def approve(self, addr, amount):
                        class Build:
                            def build_transaction(self, *args):
                                return {}
                        return Build()
                    def setApprovalForAll(self, addr, approved):
                        class Build:
                            def build_transaction(self, *args):
                                return {}
                        return Build()
            return Contract()
    class middleware:
        class onion:
            def inject(self, *args, **kwargs):
                pass
    class HTTPProvider:
        pass

def geth_poa_middleware(*args, **kwargs):
    pass

try:
    from web3.middleware import ExtraDataToPOAMiddleware as geth_poa_middleware
except:
    pass
''',
    'dotenv': '''
def load_dotenv(*args, **kwargs):
    pass
''',
}

# Write stub modules
for module_name, code in stubs.items():
    module_file = os.path.join(stub_dir, f'{module_name}.py')
    with open(module_file, 'w') as f:
        f.write(code)
    # Also create __init__.py if needed
    init_file = os.path.join(stub_dir, module_name, '__init__.py')
    os.makedirs(os.path.dirname(init_file), exist_ok=True)
    with open(init_file, 'w') as f:
        f.write(code)

print(f"Created stub modules in {stub_dir}")
print("Note: These are minimal stubs - full functionality will not work")
