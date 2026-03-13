class BaseModel:
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def dict(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
    
    def json(self):
        import json
        return json.dumps(self.dict())
