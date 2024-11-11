class FileAcceptor:
    def __init__(self, *args):
        self.lst = [*args]

    def __call__(self, filename):
        return any(filename.endswith(i) for i in self.lst)
    
    def __add__(self, ac):
        return FileAcceptor(tuple(set(self.lst + ac.lst)))
