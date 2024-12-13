import typing as tp

def det_minor(matrix: tp.List[tp.List[int]]) -> int:
    """
    :param matrix: Матрица, для которой надо найти определитель
    :return: Определитель заданной матрицы
    """
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])

    det = 0
    for i in range(n):
        minor = [matrix[j][:i] + matrix[j][i+1:]for j in range(1, n)]
        A = ((-1)**i) * matrix[0][i] * det_minor(minor)
        det += A
    return det


def det_triangle(matrix: tp.List[tp.List[int]], i, n, sgn) -> int:
    """
    Вычисление поределителя с помощью приведения матрицы к треугольному виду, путём элементарных преобразований
    :param matrix: Матрица, для которой надо найти определитель
    :param i: Индекс текущего элемента на главной диагонали
    :param n: Размер матрицы
    :param sqn: Знак определителя
    :return: Определитель заданной матрицы
    """
    if i < n - 1:
        if matrix[i][i] != 0:
            for j in range(i + 1, n):
                c = matrix[j][i] / matrix[i][i]
                for k in range(i, n):
                    matrix[j][k] -= matrix[i][k] * c
            return det_triangle(matrix, i + 1, n, sgn)
        else:
            for j in range(i + 1, n):
                if matrix[j][i] != 0:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    return det_triangle(matrix, i, n, sgn * (-1))
            else:
                return 0
    det = 1
    for l in range(n):
        det *= matrix[l][l]
    return det


def inverse_matrix(det: int) -> str:
    """
    Существует ли обратная матрица
    :param det: Определитель заданной матрицы
    :return: Если существует обратная матрица: да, иначе: нет
    """
    return ['нет', 'да'][det != 0 and det != None]


def determinant(matrix = [], method: str = 'minor') -> tp.Optional[int]:
    """
    Вычисление определителя введённой матрицы
    :param matrix:  Матрица, для которой надо найти определитель. Если matrix == [], матрица вводится с клавиатуры
    :param method:  Метод нахождения определителя. minor - метод разложения по строке, triangle - нахождение через треугольную матрицу
    :return: Определитель введённой матрицы, если её размер nxn. Иначе None
    """
    is_square = True
    if not matrix:
        n = int(input())
        for i in range(n):
            row = [int(j) for j in input().split()]
            if len(row) == n:
                matrix.append(row)
            else:
                is_square = False
    else:
        size = len(matrix)
        for i in range(size):
            if len(matrix[i]) != size:
                is_square = False
    if is_square:
        if method == 'minor':
            det = det_minor(matrix)
            print(det)
            print(inverse_matrix(det))
            return det
        elif method == 'triangle':
            det = det_triangle(matrix, 0, len(matrix), 1)
            print(det)
            print(inverse_matrix(det))
            return det
