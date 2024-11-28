class StringDigit(str):
    def __new__(cls, s):
        if not s.isdigit():
            raise ValueError('в строке должны быть только цифры')
        return super().__new__(cls, s)

    def __add__(self, other):
        return StringDigit(str(self) + other)

    def __radd__(self, other):
        return StringDigit(other + str(self))
