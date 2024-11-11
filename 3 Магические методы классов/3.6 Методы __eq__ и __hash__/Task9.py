s_inp = input()  # эту строку (переменную s_inp) в программе не менять
lst_dims = []

class Dimensions:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __hash__(self):
        return hash((self.a, self.b, self.c))
    
    def __setattr__(self, name, value):
        if isinstance(value, str):
            value = float(value) if '.' in value else int(value)
        if value <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        else:
            object.__setattr__(self, name, value)

for s in s_inp.split(';'):
    s = s.split()
    for i in s:
        if '.' in i:
            i = float(i)
        else:
            i = int(i)
    dim = Dimensions(s[0], s[1], s[2])
    lst_dims.append(dim)

lst_dims = sorted(lst_dims, key=hash)
