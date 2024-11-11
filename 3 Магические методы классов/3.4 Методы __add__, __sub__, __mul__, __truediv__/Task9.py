class Box3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def __add__(self, box):
        return Box3D(self.width + box.width, self.height + box.height, self.depth + box.depth)
    
    def __mul__(self, n):
        return Box3D(self.width * n, self.height * n, self.depth * n)
    
    def __rmul__(self, n):
        return Box3D(self.width * n, self.height * n, self.depth * n)
    
    def __sub__(self, box):
        return Box3D(self.width - box.width, self.height - box.height, self.depth - box.depth)
    
    def __floordiv__(self, n):
        return Box3D(self.width // n, self.height // n, self.depth // n)
    
    def __mod__(self, n):
        return Box3D(self.width % n, self.height % n, self.depth % n)
