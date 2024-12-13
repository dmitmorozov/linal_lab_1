import unittest
from task_1_csr import CSR_Matrix
from task_2_operations import csr_additive, csr_multiplicative, scalar_multiplicative


class TestTask2(unittest.TestCase):

    def setUp(self):
        self.matrix_a = CSR_Matrix(2, 3, [1, 2, 3], [1, 3, 4], [0, 1, 2])
        self.matrix_b = CSR_Matrix(2, 3, [4, 5, 6], [1, 2, 4], [0, 1, 2])
        self.matrix_c = CSR_Matrix(3, 2, [7, 8, 9], [1, 3, 4, 4], [0, 1, 0])


    def test_correct_additive(self): #корректное сложение
        expected_matrix = CSR_Matrix(2, 3, [5, 2, 5, 9], [1, 3, 5], [0, 1, 1, 2])
        res = csr_additive(self.matrix_a, self.matrix_b)
        self.assertEqual(expected_matrix.size_row, res.size_row)
        self.assertEqual(expected_matrix.size_col, res.size_col)
        self.assertEqual(expected_matrix.value, res.value)
        self.assertEqual(expected_matrix.rows, res.rows)
        self.assertEqual(expected_matrix.cols, res.cols)

    def test_incorrect_additive(self): #некорректное сложение
        res = csr_additive(self.matrix_a, self.matrix_c)
        self.assertEqual(res, None)

    def test_scalar_multiplicative(self): #умножение на ненулевой скаляр
        res = scalar_multiplicative(self.matrix_a, 4).value
        expected = [4, 8, 12]
        self.assertEqual(res,expected)

    def test_multiplicative_to_zero(self): #умножение на 0
        res = scalar_multiplicative(self.matrix_a, 0).value
        self.assertEqual(res, [])

    def test_correct_multiplicative(self): #корректное умножение
        expected_matrix = CSR_Matrix(2, 2, [25, 8], [1, 3, 3], [0, 1])
        res = csr_multiplicative(self.matrix_a, self.matrix_c)
        self.assertEqual(expected_matrix.size_row, res.size_row)
        self.assertEqual(expected_matrix.size_col, res.size_col)
        self.assertEqual(expected_matrix.value, res.value)
        self.assertEqual(expected_matrix.rows, res.rows)
        self.assertEqual(expected_matrix.cols, res.cols)

    def test_incorrect_multiplicative(self): #некорректное умножение
        res = csr_multiplicative(self.matrix_a, self.matrix_b)
        self.assertEqual(res, None)




if __name__ == '__main__':
    unittest.main()