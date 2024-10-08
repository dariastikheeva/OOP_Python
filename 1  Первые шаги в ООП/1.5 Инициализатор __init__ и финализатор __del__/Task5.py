a, b, c = map(int, input().split()) # эту строчку не менять

class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if any(type(i) not in [float, int] for i in [self.a, self.b, self.c]) or any(i <= 0 for i in [self.a, self.b, self.c]):
            return 1
        elif (self.a + self.b < self.c) or (self.a + self.c < self.b) or (self.b + self.c < self.a):
            return 2
        else:
            return 3

tr = TriangleChecker(a, b, c)
print(tr.is_triangle())