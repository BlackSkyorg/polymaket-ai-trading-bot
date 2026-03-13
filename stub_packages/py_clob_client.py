
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
