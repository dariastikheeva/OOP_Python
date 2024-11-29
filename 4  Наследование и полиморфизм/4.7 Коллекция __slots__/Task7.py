class Note:
    __names = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')
    __ton = (-1, 0, 1)
    
    def __init__(self, name, ton=0):
        self._name = name
        self._ton = ton
    
    def __setattr__(self, key, value):
        if key == '_name' and value not in self.__names:
            raise ValueError('недопустимое значение аргумента')
        if key == '_ton' and value not in self.__ton:
            raise ValueError('недопустимое значение аргумента')
        super().__setattr__(key, value)

class Notes:
    __slots__ = ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si')
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        self._do = Note('до')
        self._re = Note('ре')
        self._mi = Note('ми')
        self._fa = Note('фа')
        self._solt = Note('соль')
        self._la = Note('ля')
        self._si = Note('си')

    def __getitem__(self, key):
        if not isinstance(key, int) or key < 0 or key > 6:
            raise IndexError('недопустимый индекс')
        return getattr(self, self.__slots__[key])

notes = Notes()
