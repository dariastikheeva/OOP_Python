class Array:
    def __init__(self, max_length, cell):
        self.max_length = max_length
        self.cell = cell
        self.array = [self.cell() for _ in range(self.max_length)]

    def __getitem__(self, indx):
        if not (type(indx) == int and 0 <= indx < len(self.array)):
            raise IndexError('неверный индекс для доступа к элементам массива')
        else:
            return self.array[indx].value
        
    def __setitem__(self, key, value):
        if not (type(key) == int and 0 <= key < len(self.array)):
            raise IndexError('неверный индекс для доступа к элементам массива')
        else:
            self.array[key].value = value

    def __str__(self):
        return ' '.join([str(i.value) for i in self.array])

class Integer:
    def __init__(self, start_value=0):
        self.__value = start_value

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value):
        if type(value) != int:
            raise ValueError('должно быть целое число')
        else:
            self.__value = value
    