class Cell(object):
    def __init__(self, value=0):
        self.value = value
        self.is_free = True

    def __bool__(self):
        return self.is_free


class TicTacToe(object):
    def __init__(self):
        self.pole = tuple([tuple([Cell() for _ in range(3)]) for _ in range(3)])

    def check_index(self, indx):
        if (isinstance(indx, tuple) and isinstance(indx[0], int) and isinstance(indx[1], int)):
            r, c = indx[0], indx[1]
            if r < 0 or r > 2 or c < 0 or c > 2:
                raise IndexError('неверный индекс клетки')
            else:
                return True
        return True

    def check_cell(self, cell):
        if not cell:
            raise ValueError('клетка уже занята')
        else:
            return True

    def get_coords(self, coords):
        coords = []
        for coord in coords:
            if isinstance(coord, int):
                coords.append(coord)
            if isinstance(coord, slice):
                ind = coord.indices(3)
                coords.append(ind)
        return tuple(coords)

    def __getitem__(self, key):
        if self.check_index(key):
            coord = self.get_coords(key)
            r = coord[0]
            c = coord[1]
            if isinstance(r, int) and isinstance(c, int):
                return self.pole[r][c].value
            else:
                res = []
                if isinstance(r, tuple):
                    for row in range(r[0], r[1], r[2]):
                        res.append(self.pole[row][c].value)

                if isinstance(c, tuple):
                    for col in range(c[0], c[1], c[2]):
                        res.append(self.pole[r][col].value)

            return tuple(res)

    def __setitem__(self, key, value):
        if self.check_index(key):
            if self.check_cell(self.pole[key[0]][key[1]]):
                self.pole[key[0]][key[1]].value = value

    def clear(self):
        for row in self.pole:
            for cell in row:
                cell.value = 0
                cell.is_free = True

