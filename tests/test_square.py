import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):

    def test_area_basic(self):
        '''
        Проверяет вычисление площади квадрата при стандартной стороне.

        Параметры на вход:
        a = 4 (float) - сторона квадрата

        Ожидаемый результат:
        area = 4^2 = 16 (float)
        '''
        result = area(4)
        self.assertEqual(result, 16)


    def test_area_float(self):
        '''
        Проверяет корректность вычисления площади квадрата при вещественной стороне.

        Параметры на вход:
        a = 2.5 (float) - сторона квадрата

        Ожидаемый результат:
        area = 2.5^2 = 6.25 (float)
        '''
        result = area(2.5)
        self.assertAlmostEqual(result, 6.25)


    def test_area_zero_side(self):
        '''
        Проверяет вычисление площади квадрата при нулевой стороне.

        Параметры на вход:
        a = 0 (float) - сторона квадрата

        Ожидаемый результат:
        area = 0^2 = 0 (float)
        '''
        result = area(0)
        self.assertEqual(result, 0)


    def test_perimeter_basic(self):
        '''
        Проверяет вычисление периметра квадрата при стандартной стороне.

        Параметры на вход:
        a = 3 (float) - сторона квадрата

        Ожидаемый результат:
        perimeter = 4 * 3 = 12 (float)
        '''
        result = perimeter(3)
        self.assertEqual(result, 12)


    def test_perimeter_zero_side(self):
        '''
        Проверяет вычисление периметра квадрата при нулевой стороне.

        Параметры на вход:
        a = 0 (float) - сторона квадрата

        Ожидаемый результат:
        perimeter = 0 * 4 = 0 (float)
        '''
        result = perimeter(0)
        self.assertEqual(result, 0)
