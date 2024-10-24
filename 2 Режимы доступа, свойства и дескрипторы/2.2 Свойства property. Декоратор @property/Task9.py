from math import sqrt, pow

class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class PathLines:
    def __init__(self, *args):
        self.__path = [*args]

    def get_path(self):
        return self.__path
    
    def get_length(self):
        s = 0
        lst = [LineTo(0, 0)] + self.get_path()

        for i in range(len(lst)):
            if i > 0:
                s += sqrt(pow(lst[i].x - lst[i - 1].x, 2) + pow(lst[i].y - lst[i - 1].y, 2))
        return s
    
    def add_line(self, line):
        self.get_path().append(line)
    
p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length()
print(dist)
