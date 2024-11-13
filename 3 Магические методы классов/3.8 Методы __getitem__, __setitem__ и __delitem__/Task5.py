class IntegerValue:
    @classmethod
    def checked(cls, value):
        if type(value) != int:
            raise ValueError('возможны только целочисленные значения')

    def __set_name__(self, owner, name):
        self.name = '_' + f'{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.checked(value)
        setattr(instance, self.name, value)

class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value

class TableValues:
    def __init__(self, rows, cols, cell):
        if not cell:
            raise ValueError('параметр cell не указан')
        else:
            self.cells = [[cell() for _ in range(rows)] for _ in range(cols)]

    def __getitem__(self, indx):
        i, j = indx
        return self.cells[i][j].value
    
    def __setitem__(self, indx, value):
        i, j = indx
        self.cells[i][j].value = value
