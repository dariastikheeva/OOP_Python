from random import randint

# здесь объявляйте классы
from random import choice

class Cell:
    def __init__(self):
        self.__number = 0
        self.__is_mine = False
        self.__is_open = False

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number):
        if type(number) == int and 0 <= number <= 8:
            self.__number = number
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def is_mine(self):
        return self.__is_mine
    @is_mine.setter
    def is_mine(self, is_mine):
        if type(is_mine) == bool:
            self.__is_mine = is_mine
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def is_open(self):
        return self.__is_open
    @is_open.setter
    def is_open(self, is_open):
        if type(is_open) == bool:
            self.__is_open = is_open
        else:
            raise ValueError("недопустимое значение атрибута")
        
    def __bool__(self):
        return not self.is_open
    
    def __add__(self, other):
        if isinstance(other, Cell):
            return self.is_mine + other.is_mine
        if isinstance(other, int):
            return self.is_mine + other

    def __radd__(self, other):
        if isinstance(other, Cell):
            return other.is_mine + self.is_mine
        if isinstance(other, int):
            return other + self.is_mine

class GamePole:
    __count = 0
    __instance = None

    def __init__(self, N, M, total_mines):
        self.row = N
        self.column = M
        self.total_mines = total_mines
        self.__pole_cells = [[Cell() for _ in range(self.column)] for _ in range(self.row)]
        self.init_pole()
        self.set_around_mines()

    def __new__(cls, *args, **kwargs):
        if cls.__count == 0:
            cls.__count += 1
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        for i in self.pole:
            for cell in i:
                mine = choice([True, False])
                if mine:
                    if self.total_mines > 0:
                        cell.is_mine = True
                        self.total_mines -= 1

    def set_around_mines(self):
        count = 0
        tmp_pole = [
            [0 for _ in range(len(self.pole) + 2)],
            *[[0] + row + [0] for row in self.pole],
            [0 for _ in range(len(self.pole) + 2)],
        ]
        for r in range(len(self.pole)):
            for c in range(len(self.pole[r])):
                if not self.pole[r][c].is_mine:
                    count_mine = sum(
                        tmp_pole[r][c : c + 3]
                        + tmp_pole[r + 1][c : c + 3]
                        + tmp_pole[r + 2][c : c + 3]
                    )
                    self.pole[r][c].number = count_mine

    def open_cell(self, i, j):
        if (i < 0 or i > self.row - 1) or (j < 0 or j > self.column - 1):
            raise IndexError("некорректные индексы i, j клетки игрового поля")
        else:
            self.pole[i][j].is_open = True

    def show_pole(self):
        for i in self.pole:
            for cell in i:
                if cell.is_open:
                    if cell.is_mine:
                        print('*', end=' ')
                    else:
                        print(str(cell.number), end=' ')
                else:
                    print('#', end=' ')
