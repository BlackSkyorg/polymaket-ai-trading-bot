class Web3:
    def __init__(self, *args, **kwargs):
        self.eth = self.Eth()
        self.middleware_onion = self.MiddlewareOnion()
    
    class Eth:
        def __init__(self):
            self.account = self.Account()
        
        def get_transaction_count(self, addr):
            return 0
        
        def send_raw_transaction(self, tx):
            return b'0x'
        
        def wait_for_transaction_receipt(self, tx, timeout):
            return {}
        
        def contract(self, *args, **kwargs):
            return self.Contract()
        
        class Account:
            @staticmethod
            def from_key(key):
                class Account:
                    address = "0x0000000000000000000000000000000000000000"
                return Account()
        
        class Contract:
            class Functions:
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
            def __init__(self):
                self.functions = self.Functions()
    
    class MiddlewareOnion:
        def inject(self, *args, **kwargs):
            pass
    
    class HTTPProvider:
        def __init__(self, *args, **kwargs):
            pass

def HTTPProvider(*args, **kwargs):
    return Web3.HTTPProvider(*args, **kwargs)
