import typing as tp
from task_1_csr import CSR_Matrix, to_csr, to_dense, enter_csr


def scalar_multiplicative(matrix: CSR_Matrix, scalar: int) -> CSR_Matrix:
    """
    Умножение матрицы в csr формате на скаляр
    :param matrix: Матрица в csr формате
    :param scalar: Скаляр, на который будем умножать
    :return: Матрица в csr формате в результате умножения на скаляр
    """
    if scalar == 0: #если умножаем на 0
        matrix.value = []
        matrix.rows = [1 for i in range(matrix.size_row + 1)]
        matrix.cols = []
    else:
        for i in range(len(matrix.value)):
            matrix.value[i] *= scalar
    return matrix

#сложение двух матриц
def csr_additive(a: CSR_Matrix, b: CSR_Matrix) -> tp.Optional[CSR_Matrix]:
    """
    Сложение двух матриц csr формата
    :param a: Первая матрица в csr формате
    :param b: Вторая матрица в csr формате
    :return: Результат в csr формате, если размеры матриц допускают сложение. Иначе None
    """
    if a.size_col == b.size_col and a.size_row == b.size_row: #проверка на соответствие размеров
        rows = [1, ]
        cols = []
        value = []
        for row in range(a.size_row):
            new_elems = 0 # количество != 0 элементов в строке после сложения
            m1 = a.cols[a.rows[row] - 1 : a.rows[row + 1] - 1] #список столбоцов, в которых есть значение != 0
            m2 = b.cols[b.rows[row] - 1 : b.rows[row + 1] -1]
            m1.append(float('inf'))
            m2.append(float('inf'))
            l1 = 0
            l2 = 0
            while l1 < len(m1) - 1 or l2 < len(m2) - 1: #пока не пройдем по всем элементам
                if m1[l1] == m2[l2]: #ненулевой элемент есть в каждой матрице
                    new_value = a.value[a.rows[row] - 1 + l1] + b.value[b.rows[row] - 1 + l2]
                    if new_value != 0:
                        value.append(new_value)
                        cols.append(m1[l1])
                        new_elems += 1
                    l1 += 1
                    l2 += 1
                elif m1[l1] < m2[l2]: #значит в матрице b на этой позиции 0
                    new_value = a.value[a.rows[row] - 1 + l1]
                    value.append(new_value)
                    cols.append(m1[l1])
                    new_elems += 1
                    l1 += 1
                else:#значит в матрице a на этой позиции 0
                    new_value = b.value[b.rows[row] - 1 + l2]
                    value.append(new_value)
                    cols.append(m2[l2])
                    new_elems += 1
                    l2 += 1
            rows.append(rows[row] + new_elems)
        res = CSR_Matrix(a.size_row, a.size_col, value, rows, cols)
        return res
    return None


def csr_multiplicative(a: CSR_Matrix, b_csr: CSR_Matrix) -> tp.Optional[CSR_Matrix]:
    """
    Умножение двух матриц в csr формата (a * b)
    :param a: Первая матрица в csr формате
    :param b_csr: Вторая матрица в csr формате
    :return: Результат в csr формате, если размеры матриц допускают умножение. Иначе None
    """
    if a.size_col == b_csr.size_row: #проверка на соответствие размеров
        res = [[0 for j in range(b_csr.size_col)] for i in range(a.size_row)] #матрица нужных размеров из нулей
        b = to_dense(b_csr) #перевод матрицы b в обычный формат
        for row in range(a.size_row):
            for j in range(a.rows[row] - 1, a.rows[row + 1] - 1): # проход по ненулевым значениям a
                col = a.cols[j]
                value = a.value[j]
                for k in range(b_csr.size_col):
                    res[row][k] += value * b[col][k]
        res_csr = to_csr(a.size_row, b_csr.size_col, res)
        return res_csr
    return None