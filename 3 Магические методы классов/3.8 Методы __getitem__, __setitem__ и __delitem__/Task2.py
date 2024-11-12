class Record:
    def __init__(self, **kwargs):
        self.keys = []
        for k, v in kwargs.items():
            setattr(self, k, v)
            self.keys.append(k)

    def __getitem__(self, key):
        if key >= len(self.keys):
            raise IndexError('неверный индекс поля')
        else:
            return getattr(self, self.keys[key])
        
    def __setitem__(self, key, value):
        if key >= len(self.keys):
            raise IndexError('неверный индекс поля')
        else:
            return setattr(self, self.keys[key], value)
