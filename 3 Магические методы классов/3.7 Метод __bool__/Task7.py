class Ellipse:
    def __init__(self, *args):
        if args:
            self.x1, self.y1, self.x2, self.y2 = args

    def __bool__(self):
        return hasattr(self, 'x1') and hasattr(self, 'y1') and hasattr(self, 'x2') and hasattr(self, 'y2')
    
    def get_coords(self):
        if bool(self):
            return (self.x1, self.y1, self.x2, self.y2)
        else:
            raise AttributeError('нет координат для извлечения')
        
lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8)]

for el in lst_geom:
    if bool(el):
        el.get_coords()
