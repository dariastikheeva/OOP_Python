class Cell(object):
    def __init__(self, value):
        self.value = value


class SparseTable(object):
    def __init__(self):
        super(SparseTable, self).__init__()
        self.rows = 0
        self.cols = 0
        self.cells = {}

    def get_value_row_col(self, coords, mode='rows'):
        res_value = 0
        if mode == 'rows':
            lst_rows = [item[0] for item in coords]
            res_value = max(lst_rows)
        if mode == 'cols':
            lst_cols = [item[1] for item in coords]
            res_value = max(lst_cols)
        return res_value

    def add_data(self, row, col, data):
        coord = (row, col)
        self.cells[coord] = data
        self.reindex()

    def remove_data(self, row, col):
        coord = (row, col)
        if coord not in self.cells:
            raise IndexError('ячейка с указанными индексами не существует')
        else:
            self.cells.pop(coord)
        self.reindex()

    def reindex(self):
        keys = self.cells.keys()
        self.rows = self.get_value_row_col(keys, mode='rows') + 1
        self.cols = self.get_value_row_col(keys, mode='cols') + 1

    def __getitem__(self, key):
        if key not in self.cells:
            raise ValueError('данные по указанным индексам отсутствуют')
        else:
            return self.cells[key].value

    def __setitem__(self, key, value):
        if key not in self.cells:
            self.add_data(key[0], key[1], Cell(value))
        else:
            self.cells[key].value = value
