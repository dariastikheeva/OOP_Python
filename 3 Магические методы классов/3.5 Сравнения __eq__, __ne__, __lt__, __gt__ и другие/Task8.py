class CentralBank(object):
    rates = {"rub": 72.5, "dollar": 1.0, "euro": 1.15}

    def __new__(cls, *args, **kwargs):
        return

    @classmethod
    def register(cls, money):
        money.cb = cls


class Money(object):
    currency = None

    def __init__(self, volume=0):
        self.__volume = volume
        self.__cb = None

    @property
    def cb(self):
        return self.__cb
    @cb.setter
    def cb(self, value):
        self.__cb = value

    @property
    def volume(self):
        return self.__volume
    @volume.setter
    def volume(self, value):
        self.__volume = value

    def get_volume(self, other):
        if other.cb is None:
            raise ValueError("Неизвестен курс валют.")

        v1 = self.volume / self.cb.rates[self.currency]
        v2 = other.volume / other.cb.rates[other.currency]
        return v1, v2

    def __eq__(self, other):
        v1, v2 = self.get_volume(other)

        return abs(v1 - v2) < 0.1

    def __gt__(self, other):
        v1, v2 = self.get_volume(other)

        return v1 > v2

    def __ge__(self, other):
        v1, v2 = self.get_volume(other)

        return v1 >= v2


class MoneyR(Money):
    currency = 'rub'


class MoneyD(Money):
    currency = 'dollar'


class MoneyE(Money):
    currency = 'euro'
