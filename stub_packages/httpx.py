
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
