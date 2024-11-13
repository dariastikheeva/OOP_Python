class Track:
    def __init__(self, start_x, start_y):
        self.points = []

    def add_point(self, x, y, speed):
        self.points.append([(x, y), speed])

    def __getitem__(self, indx):
        if not (type(indx) == int and 0 <= indx < len(self.points)):
            raise IndexError('некорректный индекс')
        else:
            return self.points[indx]
        
    def __setitem__(self, key, value):
        if not (type(key) == int and 0 <= key <= len(self.points)):
            raise IndexError('некорректный индекс')
        else:
            self.points[key][-1] = value
