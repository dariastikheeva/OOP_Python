# здесь объявляйте классы CellException, CellIntegerException, CellFloatException, CellStringException
class CellException(Exception):
    pass


class CellIntegerException(CellException):
    pass


class CellFloatException(CellException):
    pass


class CellStringException(CellException):
    pass

# здесь объявляйте классы CellInteger, CellFloat, CellString
class CellInteger:
    def __init__(self, min_value, max_value):
        self.__value = None
        self._min_value = min_value
        self._max_value = max_value

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value):
        self.__value = value

    def __setattr__(self, key, value):
        if key == 'value':
            if value is not None and (
                value < self._min_value or value > self._max_value
            ):
                raise CellIntegerException('значение выходит за допустимый диапазон')
        super().__setattr__(key, value)


class CellFloat:
    def __init__(self, min_value, max_value):
        self.__value = None
        self._min_value = min_value
        self._max_value = max_value

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value):
        self.__value = value

    def __setattr__(self, key, value):
        if key == 'value':
            if value is not None and (
                value < self._min_value or value > self._max_value
            ):
                raise CellFloatException('значение выходит за допустимый диапазон')
        super().__setattr__(key, value)


class CellString:
    def __init__(self, min_length, max_length):
        self.__value = None
        self._min_length = min_length
        self._max_length = max_length

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value):
        self.__value = value

    def __setattr__(self, key, value):
        if key == 'value':
            if value is not None and (
                len(value) < self._min_length or len(value) > self._max_length
            ):
                raise CellStringException('длина строки выходит за допустимый диапазон')
        super().__setattr__(key, value)

# здесь объявляйте класс TupleData
class TupleData:
    __types = (CellInteger, CellFloat, CellString)

    def __init__(self, *args):
        self._lst_data = [cell for cell in args if isinstance(cell, self.__types)]

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0 or key > (len(self._lst_data) - 1):
            raise IndexError
        self._lst_data[key].value = value

    def __getitem__(self, key):
        if not isinstance(key, int) or key < 0 or key > (len(self._lst_data) - 1):
            raise IndexError
        return self._lst_data[key].value

    def __iter__(self):
        self.ind = 0
        return self

    def __next__(self):
        if self.ind < len(self._lst_data):
            self.ind += 1
            return self[self.ind - 1]
        else:
            raise StopIteration

    def __len__(self):
        return len(self._lst_data)

# эти строчки в программе не менять!
ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")
    