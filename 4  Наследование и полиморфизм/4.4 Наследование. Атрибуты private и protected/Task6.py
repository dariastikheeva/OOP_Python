class Furniture(object):
    def __init__(self, name, weight):
        super(Furniture, self).__init__()
        self._name = name
        self._weight = weight

    @classmethod
    def __verify_name(cls, name):
        if not isinstance(name, str):
            raise TypeError('название должно быть строкой')

    @classmethod
    def __verify_weight(cls, weight):
        if weight <= 0:
            raise TypeError('вес должен быть положительным числом')

    def __setattr__(self, key, value):
        if key == "_name":
            self.__verify_name(value)
        if key == "_weight":
            self.__verify_weight(value)
        object.__setattr__(self, key, value)

    def get_attrs(self):
        return self.__dict__.values()


class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
        super(Closet, self).__init__(name, weight)
        self._tp = tp
        self._doors = doors


class Chair(Furniture):
    def __init__(self, name, weight, height):
        super(Chair, self).__init__(name, weight)
        self._height = height


class Table(Furniture):
    def __init__(self, name, weight, height, square):
        super(Table, self).__init__(name, weight)
        self._height = height
        self._square = square
