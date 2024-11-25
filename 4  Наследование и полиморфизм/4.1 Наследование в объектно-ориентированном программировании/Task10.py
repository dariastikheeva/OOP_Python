class Vector(object):
    def __init__(self, *args):
        self.coords = args

    def get_coords(self):
        return self.coords

    def __add__(self, other):
        self.__check_razm(other)
        out_coord = [v + other.coords[i] for i, v in enumerate(self.coords)]
        if isinstance(other, VectorInt):
            return VectorInt(*out_coord)
        return Vector(*out_coord)

    def __sub__(self, other):
        self.__check_razm(other)
        out_coord = [v - other.coords[i] for i, v in enumerate(self.coords)]
        if isinstance(other, VectorInt):
            return VectorInt(*out_coord)
        return Vector(*out_coord)

    def __check_razm(self, other):
        if len(self.coords) != len(other.coords):
            raise TypeError('размерности векторов не совпадают')
        return True


class VectorInt(Vector):
    def __setattr__(self, key, value):
        if key == "coords":
            for i in value:
                if not isinstance(i, int):
                    raise ValueError('координаты должны быть целыми числами')
        object.__setattr__(self, key, value)
