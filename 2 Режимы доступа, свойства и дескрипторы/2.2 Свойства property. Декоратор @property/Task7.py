class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = x if self.check_coord(x) else 0
        self.__y = y if self.check_coord(y) else 0

    @classmethod
    def check_coord(cls, n):
        return type(n) in (int, float) and cls.MIN_COORD <= n <= cls.MAX_COORD

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if self.check_coord(x):
            self.__x = x

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        if self.check_coord(y):
            self.__y = y

    @staticmethod
    def norm2(vector):
        return vector.x ** 2 + vector.y ** 2
