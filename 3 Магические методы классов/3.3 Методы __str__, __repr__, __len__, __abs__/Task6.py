from math import sqrt, pow

class Complex:
    def __init__(self, real, img):
        self.__real = real
        self.__img = img

    @property
    def real(self):
        return self.__real
    @real.setter
    def real(self, real):
        if not isinstance(real, (int, float)):
            raise ValueError('Неверный тип данных.')
        self.__real = real

    @property
    def img(self):
        return self.__img
    @img.setter
    def img(self, img):
        if not isinstance(img, (int, float)):
            raise ValueError('Неверный тип данных.')
        self.__img = img

    def __abs__(self):
        return sqrt(pow(self.real, 2) + pow(self.img, 2))
    
cmp = Complex(real=7, img=8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
    