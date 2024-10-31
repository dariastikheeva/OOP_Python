class LengthValidator:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwds):
        return self.min_length <= len(args[0]) <= self.max_length
    
class CharsValidator:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, *args, **kwds):
        return all(i in self.chars for i in args[0])
