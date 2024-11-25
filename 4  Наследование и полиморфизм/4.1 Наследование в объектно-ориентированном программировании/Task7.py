class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

class Game(Singleton):
    def __init__(self, name):
        super().__init__()
        if 'name' not in self.__dict__:
            self.name = name
