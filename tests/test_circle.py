import unittest
from circle import area, perimeter
import math


class CircleTestCase(unittest.TestCase):

    def test_area_basic(self):
        '''
        Проверяет вычисление площади круга при стандартном значении радиуса.

        Параметры на вход:
        r = 5 (float) - радиус окружности

        Ожидаемый результат:
        area = π * 5^2 (float)
        '''
        result = area(5)
        self.assertAlmostEqual(result, math.pi * 25)


    def test_area_zero_radius(self):
        '''
        Проверяет вычисление площади круга при нулевом радиусе.

        Параметры на вход:
        r = 0 (float) - радиус окружности

        Ожидаемый результат:
        area = π * 0^2 = 0 (float), так как площадь круга с R = 0 равна нулю
        '''
        result = area(0)
        self.assertEqual(result, 0)


    def test_perimeter_basic(self):
        '''
        Проверяет вычисление длины окружности при стандартном значении радиуса.

        Параметры на вход:
        r = 3 (float) - радиус окружности

        Ожидаемый результат:
        perimeter = 2 * π * 3 = 6π (float)
        '''
        result = perimeter(3)
        self.assertAlmostEqual(result, 2 * math.pi * 3)


    def test_perimeter_zero_radius(self):
        '''
        Проверяет вычисление длины окружности при нулевом радиусе.

        Параметры на вход:
        r = 0 (float) - радиус окружности

        Ожидаемый результат:
        perimeter = 2 * π * 0 = 0 (float)
        '''
        result = perimeter(0)
        self.assertEqual(result, 0)
