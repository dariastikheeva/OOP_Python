class WordString:
    def __init__(self, string=''):
        self.__string = string
        self.__words = self.string.split()

    @property
    def string(self):
        return self.__string
    @string.setter
    def string(self, string):
        self.__string = string
        self.__words = string.split()

    def __len__(self):
        return len(self.__words)
    
    def __call__(self, indx):
        return self.__words[indx]
