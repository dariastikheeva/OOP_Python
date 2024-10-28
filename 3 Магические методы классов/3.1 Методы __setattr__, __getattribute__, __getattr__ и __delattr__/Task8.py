class Circle:
    def __init__(self, x, y, radius):
        self.__x = x
        self.__y = y
        self.__radius = radius

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, radius):
        self.__radius = radius
    
    def __setattr__(self, key, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Неверный тип присваиваемых данных.")
        if key == 'radius' and value <= 0:
            return
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False
