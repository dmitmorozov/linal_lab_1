import unittest
from task_3_det import det_triangle, det_minor, determinant, inverse_matrix
from random import randrange
import numpy as np

class TestTask3(unittest.TestCase):

    def setUp(self):
        self.square_matrix = [
            [1, 2, 3, 0],
            [6, 8, 3, 1],
            [80, 3, 3, 4],
            [2, 11, 4, 5]
        ]
        self.non_square_matrix = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        self.zero_det_matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [0, 0, 0]
        ]
        self.big_matrix = [[randrange(100) for j in range(100)] for i in range(100)]

    def test_minor_square(self): #определитель квадратной матрицы
        det = determinant(self.square_matrix, 'minor')
        self.assertEqual(det, -5514)
        inverse = inverse_matrix(det)
        self.assertEqual(inverse, 'да')

    def test_minor_non_square(self): #определитель не квадратной матрицы
        det = determinant(self.non_square_matrix, 'minor')
        self.assertEqual(det, None)
        inverse = inverse_matrix(det)
        self.assertEqual(inverse, 'нет')

    def test_minor_zero_det(self): #определитель равен 0
        det = determinant(self.zero_det_matrix, 'minor')
        self.assertEqual(det, 0)
        inverse = inverse_matrix(det)
        self.assertEqual(inverse, 'нет')

    def test_triangle_square(self): #определеитель большой матрицы
        det = determinant(self.square_matrix, 'triangle')
        expected_det = np.linalg.det(np.array(self.square_matrix))
        inaccuracy = abs(1 - det / expected_det)
        self.assertEqual(inaccuracy <= 0.00000000001, True)

    def test_triangle_zero_det(self):
        det = determinant(self.zero_det_matrix, 'triangle')
        self.assertEqual(det, 0)

    def test_bif_size_matrix(self):
        det = determinant(self.big_matrix, 'triangle')
        expected_det = np.linalg.det(np.array(self.big_matrix))
        inaccuracy = abs(1 - det / expected_det)
        t = det - expected_det
        print("%2f" % t)
        self.assertEqual(inaccuracy <= 0.00000000001, True)



if __name__ == '__main__':
    unittest.main()