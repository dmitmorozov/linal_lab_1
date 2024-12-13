import unittest
import typing as tp
from task_1_csr import CSR_Matrix, to_csr


class TestTask1(unittest.TestCase):


    def setUp(self):
        self.csr_square = CSR_Matrix(3, 3,[1, 2, 3],[1, 2, 3, 4],[0, 1, 2])

        self.csr_non_square = CSR_Matrix(2, 3,[1, 2],[1, 2, 2],[0, 1])

    def test_to_CSR(self): #тест перевода в CSR формат
        matrix = [[1, 0, 0],
                  [0, 2, 0],
                  [0, 0, 3]]
        csr_matrix = to_csr(3, 3, matrix)
        self.assertEqual(self.csr_square.size_row, csr_matrix.size_row)
        self.assertEqual(self.csr_square.size_col, csr_matrix.size_col)
        self.assertEqual(self.csr_square.value, csr_matrix.value)
        self.assertEqual(self.csr_square.rows, csr_matrix.rows)
        self.assertEqual(self.csr_square.cols, csr_matrix.cols)

    def test_trace_square(self): #след квадратной матрицы
        trace = self.csr_square.trace()
        self.assertEqual(trace, 6)

    def test_trace_non_square(self): #след не квадратной матрицы
        trace = self.csr_non_square.trace()
        self.assertEqual(trace, None)

    def test_get_elem(self): #получение ненулевого элемента
        elem = self.csr_square.get_elem(2, 2)
        self.assertEqual(elem, 2)

    def test_get_elem_zero(self): #получение нулевого элемента
        elem = self.csr_square.get_elem(1, 2)
        self.assertEqual(elem, 0)

    def test_get_wrong_elem(self): #некорректные индексы элемента
        elem = self.csr_square.get_elem(10, 1)
        self.assertEqual(elem, None)



if __name__ == '__main__':
    unittest.main()