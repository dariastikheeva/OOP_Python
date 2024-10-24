class FloatValue:
    @classmethod
    def check_value(cls, value):
        if not isinstance(value, float):
            raise TypeError("Присваивать можно только вещественный тип данных.")
    
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)
 
    def __set__(self, instance, value):
        self.check_value(value)
        setattr(instance, self.name, value)

class Cell:
    value = FloatValue()

    def __init__(self, value):
        self.value = value

class TableSheet:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.cells = [[Cell(0.0) for _ in range(M)] for _ in range(N)]

table = TableSheet(5, 3)
n = 0
for i in table.cells:
    for j in i:
        n += 1
        j.value = float(n)
