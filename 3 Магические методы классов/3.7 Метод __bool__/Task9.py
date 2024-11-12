class Vector(object):
    def __init__(self, *args):
        self.coords = args
        self.dimension = len(self.coords)

    def check_dimension(self, other):
        if isinstance(other, Vector):
            return True if self.dimension == other.dimension else False

    def __add__(self, other):
        if isinstance(other, Vector):
            if not self.check_dimension(other):
                raise ArithmeticError("размерности векторов не совпадают")
            coord = [self.coords[i] + other.coords[i] for i in range(len(self.coords))]
        else:
            coord = [self.coords[i] + other for i in range(len(self.coords))]
        return Vector(*coord)

    def __mul__(self, other):
        if isinstance(other, Vector):
            if not self.check_dimension(other):
                raise ArithmeticError("размерности векторов не совпадают")
            coord = [self.coords[i] * other.coords[i] for i in range(len(self.coords))]
        else:
            coord = [self.coords[i] * other for i in range(len(self.coords))]
        return Vector(*coord)

    def __sub__(self, other):
        if isinstance(other, Vector):
            if not self.check_dimension(other):
                raise ArithmeticError("размерности векторов не совпадают")
            coord = [self.coords[i] - other.coords[i] for i in range(len(self.coords))]
        else:
            coord = [self.coords[i] - other for i in range(len(self.coords))]
        return Vector(*coord)

    def __iadd__(self, other):
        if isinstance(other, Vector):
            self.coords = [
                self.coords[i] + other.coords[i] for i in range(len(self.coords))
            ]
        else:
            self.coords = [self.coords[i] + other for i in range(len(self.coords))]

        return self

    def __isub__(self, other):
        if isinstance(other, Vector):
            self.coords = [
                self.coords[i] - other.coords[i] for i in range(len(self.coords))
            ]
        else:
            self.coords = [self.coords[i] - other for i in range(len(self.coords))]
            
        return self

    def __eq__(self, other):
        for i, v in enumerate(self.coords):
            if v != other.coords[i]:
                return False
        return True

    def __ne__(self, other):
        for i, v in enumerate(self.coords):
            if v != other.coords[i]:
                return True
        return False
