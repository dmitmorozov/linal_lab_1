import typing as tp


class CSR_Matrix:
    def __init__(self, size_row, size_col, value, rows, cols):
        """
        :param size_row: Количество строк матрицы
        :param size_col: Количество столбцов матрицы
        :param value: Ненулевые элемента матрицы
        :param rows: rows[i + 1] - rows[i] - количество ненулевых элементов в i-ой строке
        :param cols: Номера столбцов, соответствующие ненулевым значениям
        """
        self.size_row = size_row
        self.size_col = size_col
        self.value = value
        self.rows = rows
        self.cols = cols

    #вычисление следа матрциы
    def trace(self) -> tp.Optional[int]:
        """
        Вычисление следа матрицы
        :return: След матрицы, если она квадратная. Иначе None
        """
        if self.size_col == self.size_row: #является ли матрица квадратной
            res = 0
            for i in range(self.size_col): #проход по каждой стркое
                res += self.get_elem(i + 1, i + 1)
            return res
        return None

    #получение эл-та из i-ой строки, j-го столбца
    def get_elem(self, i: int, j: int) -> tp.Optional[int]:
        """
        Получение элемента матрицы
        :param i: Номер строки элемента (индексация с единицы)
        :param j: Номер столбца элемента (индексация с единицы)
        :return: Элемент i-ой строки j-столбца матрицы, если индексы корректы. Иначе None
        """
        if i < 1 or i > self.size_row or j < 1 or j > self.size_col: #корректность индексов
            return None
        for k in range(self.rows[i - 1] - 1, self.rows[i] - 1):
            if self.cols[k] == j - 1:
                return self.value[k]
        return 0 #если на нашли эл-т, значит это 0


#перевод матрциы в csr формат
def to_csr(n: int, m: int, matrix: tp.List[tp.List[int]]) -> CSR_Matrix:
    """
    Перевод введённой матрицы в CSR формат
    :param n: Количество строк
    :param m: Количество столбцов
    :param matrix: матрица в плотном формате
    :return: Матрица в CSR формате
    """
    value = []
    rows = [1, ]
    cols = []
    for i in range(n):
        rows.append(rows[i])
        row = matrix[i]
        for j in range(m):
            if row[j] != 0:
                value.append(int(row[j]))
                cols.append(j)
                rows[i+1] += 1
    csr = CSR_Matrix(n, m, value, rows, cols)
    return csr

def to_dense(matrix: CSR_Matrix) -> tp.List[tp.List[int]]:
    """
    Перевод матрицы из CSR формата в плотный
    :param matrix: Матрица в CSR формате
    :return: Матрица в плотном формате
    """
    res = [[0 for j in range(matrix.size_col)] for i in range(matrix.size_row)]
    for row in range(matrix.size_row):
        for j in range(matrix.rows[row] - 1, matrix.rows[row+1] - 1):
            col = matrix.cols[j]
            value = matrix.value[j]
            res[row][col] = value
    return res



def enter_csr() -> CSR_Matrix:
    """
    Получение матрицы с клавиатуры и сохранение в CSR формате
    :return: Введённая матрица в CSR формате
    """
    n, m = map(int, input().split())
    matrix = [[int(j) for j in input().split()] for i in range(n)]
    matrix_csr = to_CSR(n, m, matrix)
    return matrix_csr