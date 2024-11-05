from math import sqrt, pow

class RadiusVector:
    def __init__(self, *args):
        if len(args) == 1:
            self.__coords = [0 for _ in range(args[0])]
        else:
            self.__coords = list(args)

    def set_coords(self, *args):
        for i in range(len(args if len(args) < len(self.__coords) else self.__coords)):
            self.__coords[i] = args[i]

    def get_coords(self):
        return tuple(self.__coords)
    
    def __len__(self):
        return len(self.__coords)
    
    def __abs__(self):
        return sqrt(sum((pow(i, 2)) for i in self.__coords))
