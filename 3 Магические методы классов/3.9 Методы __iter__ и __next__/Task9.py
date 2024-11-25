class Cell:
    def __init__(self, data):
        self.__data = data

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data):
        self.__data = data

class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.table = [[Cell(0) for _ in range(self.cols)] for _ in range(self.rows)]

    def check_indices(self, i, j):
        if not (isinstance(i, int) and isinstance(j, int)) or not(0 <= i < self.rows and 0 <= j <= self.cols):
            raise IndexError('неверный индекс')
        else:
            return True

    def __getitem__(self, indx):
        r, c = indx[0], indx[1]
        self.check_indices(r, c)
        return self.table[r][c].data
    
    def __setitem__(self, key, value):
        r, c = key[0], key[1]
        self.check_indices(r, c)
        if not isinstance(value, self.type_data):
            raise TypeError('неверный тип присваиваемых данных')
        else:
            self.table[r][c].data = value

    def __iter__(self):
        for row in self.table:
            yield [i.data for i in row]
            