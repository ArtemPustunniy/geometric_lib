import unittest
import circle
import math


class TriangleTest(unittest.TestCase):
    """unit test, который проверяет правильность работы функции для вычисления площади круга на диапазоне
    радиусов от 0 до 100"""
    def test_area_mul(self):
        for r in range(0, 100):
            res = circle.area(r)
            self.assertEqual(res, math.pi * r * r)

    """unit test, который проверяет правильность работы функции для вычисления длины окружности на диапазоне
    радиусов от 0 до 100"""
    def test_perimeter_mul(self):
        for r in range(0, 100):
            res = circle.perimeter(r)
            self.assertEqual(res, 2 * math.pi * r)


if __name__ == '__main__':
    unittest.main()