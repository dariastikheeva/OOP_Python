class IterColumn:
    def __init__(self, lst, column):
        self.lst = lst
        self.column = column

    def __iter__(self):
        for row in range(len(self.lst)):
            yield self.lst[row][self.column]
            