# здесь объявляйте класс
class TupleLimit(tuple):
    def __new__(cls, __iterable, max_length):
        if len(__iterable) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')
        return super().__new__(cls, __iterable)

    def __str__(self):
        return ' '.join(map(str, self))

    def __repr__(self):
        return ' '.join(map(str, self))



digits = list(map(float, input().split()))  # эту строчку не менять (коллекцию digits также не менять)

# здесь создавайте объект класса
try:
    tl = TupleLimit(digits, 5)
    print(tl)
except Exception as e:
    print(e)
    