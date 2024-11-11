class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def __call__(self, matrix):
        self._validate_matrix(matrix)
        return self._max_pooling(matrix)

    def _validate_matrix(self, matrix):
        if not matrix or not all(isinstance(row, list) for row in matrix):
            raise ValueError("Неверный формат для первого параметра matrix.")
        row_length = len(matrix[0])
        for row in matrix:
            if len(row) != row_length or any(not isinstance(el, (int, float)) for el in row):
                raise ValueError("Неверный формат для первого параметра matrix.")

    def _max_pooling(self, matrix):
        result = []
        row_step, col_step = self.step
        row_size, col_size = self.size
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        for i in range(0, num_rows - row_size + 1, row_step):
            new_row = []
            for j in range(0, num_cols - col_size + 1, col_step):
                window = [matrix[x][y] for x in range(i, i + row_size)
                          for y in range(j, j + col_size)]
                new_row.append(max(window))
            result.append(new_row)
        
        return result
