class Digit(object):
    def __init__(self, value):
        super().__init__()
        self._value = value

    def __setattr__(self, key, value):
        if not isinstance(value, (int, float)):
            raise TypeError('значение не соответствует типу объекта')
        super().__setattr__(key, value)

class Integer(Digit):
    def __init__(self, value):
        if not isinstance(value, int):
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class Float(Digit):
    def __init__(self, value):
        if not isinstance(value, float):
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class Positive(Digit):
    def __init__(self, value):
        if value < 0:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class Negative(Digit):
    def __init__(self, value):
        if value >=0:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)

class PrimeNumber(Integer, Positive):
    def __init__(self, value):
        super().__init__(value)

class FloatPositive(Float, Positive):
    def __init__(self, value):
        super().__init__(value)
    
digits = [PrimeNumber(3), PrimeNumber(1), PrimeNumber(4), 
          FloatPositive(1.5), FloatPositive(9.2), FloatPositive(6.5), 
          FloatPositive(3.5), FloatPositive(8.9)]

lst_positive = [x for x in digits  if isinstance(x, Positive)]
lst_float = [x for x in digits if isinstance(x, Float)]
