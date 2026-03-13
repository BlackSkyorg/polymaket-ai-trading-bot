
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
    class constants:
        MAX_INT = "0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"

def geth_poa_middleware(*args, **kwargs):
    pass

try:
    from web3.middleware import ExtraDataToPOAMiddleware as geth_poa_middleware
except:
    pass
