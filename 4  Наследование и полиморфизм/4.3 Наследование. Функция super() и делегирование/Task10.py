class ItemAttrs:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.items = [self.x, self.y]

    def __getitem__(self, key):
        return self.items[key]
    
    def __setitem__(self, key, value):
        self.items[key] = value

class Point(ItemAttrs):
    pass
