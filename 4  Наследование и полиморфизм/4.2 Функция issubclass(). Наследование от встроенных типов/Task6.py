class Tuple(tuple):
    def __add__(self, other):
        if hasattr(other, '__iter__'):
            return Tuple(tuple(self) + tuple(other))
