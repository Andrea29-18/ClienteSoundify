class UserSingleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.data = {}
        return cls._instance
    
    def set_data(self, key, value):
        self.data[key] = value
    
    def get_data(self, key):
        return self.data.get(key)