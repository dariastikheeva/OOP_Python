# здесь пишется программа
from random import choice

class Cell:
    def __init__(self, around_mines = 0, mine = False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False

class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = [[Cell() for _ in range(self.N)] for _ in range(self.N)]
        self.init()
        self.set_around_mines()

    def init(self):
        for i in self.pole:
            for cell in i:
                is_mine = choice([True, False])
                if is_mine:
                    if self.M > 0:
                        cell.mine = True
                        self.M -= 1

    def set_around_mines(self):
        for i in range(self.N):
            for j in range(self.N):
                self.pole[i][j].around_mines = sum([cell.mine for row in self.pole[max(0, i - 1):i + 2] for cell in row[max(0, j - 1):j + 2]])


    def show(self):
        for i in self.pole:
            for cell in i:
                if cell.fl_open:
                    if cell.mine:
                        print('*', end=' ')
                    else:
                        print(str(cell.around_mines), end=' ')
                else:
                    print('#', end=' ')
                    
pole_game = GamePole(10, 12)
