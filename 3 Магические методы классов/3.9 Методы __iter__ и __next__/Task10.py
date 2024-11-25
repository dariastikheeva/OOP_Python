class Matrix(object):
    def __init__(self, *args):
        if len(args) == 3:
            self.rows = args[0]
            self.cols = args[1]
            self.fill_value = args[2]
            self.lst_matrix = [
                [self.fill_value for _ in range(self.cols)] for _ in range(self.rows)
            ]
        if len(args) == 1:
            self.lst_matrix = args[0]
            self.rows = len(self.lst_matrix)
            self.cols = len(self.lst_matrix[0])

    def __setattr__(self, key, value):
        if (key == 'rows' or key == 'cols') and (not isinstance(value, int)):
            raise TypeError(
                'аргументы rows, cols - целые числа; fill_value - произвольное число'
            )
        if (key == 'fill_value') and (not isinstance(value, (int, float))):
            raise TypeError(
                'аргументы rows, cols - целые числа; fill_value - произвольное число'
            )
        if key == 'lst_matrix' and isinstance(value, list):
            self.check_list(value)
        object.__setattr__(self, key, value)

    def check_list(self, lst):
        if isinstance(lst, list):
            length = len(lst[0])
            for row in lst:
                if len(row) != length:
                    raise TypeError(
                        'список должен быть прямоугольным, состоящим из чисел'
                    )
                for i in row:
                    if not isinstance(i, (int, float)):
                        raise TypeError(
                            'список должен быть прямоугольным, состоящим из чисел'
                        )

    def check_value(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('значения матрицы должны быть числами')
        return True

    def check_index(self, indx):
        r, c = indx[0], indx[1]
        if not isinstance(r, int) or not isinstance(c, int):
            raise IndexError('недопустимые значения индексов')
        if (
            r < 0
            or r >= self.rows
            or c < 0
            or c >= self.cols
            or not isinstance(c, int)
            or not isinstance(r, int)
        ):
            raise IndexError('недопустимые значения индексов')
        return True

    def __getitem__(self, key):
        if self.check_index(key):
            return self.lst_matrix[key[0]][key[1]]

    def __setitem__(self, key, value):
        if self.check_index(key) and self.check_value(value):
            self.lst_matrix[key[0]][key[1]] = value

    def check_dim(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            return True
        else:
            raise ValueError('операции возможны только с матрицами равных размеров')

    def __add__(self, other):
        if isinstance(other, Matrix) and self.check_dim(other):
            out_lst = [
                [val + other[r, c] for c, val in enumerate(row)]
                for r, row in enumerate(self.lst_matrix)
            ]
        if isinstance(other, int):
            out_lst = [[val + other for val in row] for row in self.lst_matrix]
        return Matrix(out_lst)

    def __sub__(self, other):
        if isinstance(other, Matrix) and self.check_dim(other):
            out_lst = [
                [val - other[r, c] for c, val in enumerate(row)]
                for r, row in enumerate(self.lst_matrix)
            ]
        if isinstance(other, int):
            out_lst = [[val - other for val in row] for row in self.lst_matrix]
        return Matrix(out_lst)
