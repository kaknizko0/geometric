import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):

    def test_perimeter_basic(self):
        '''
        Проверяет вычисление периметра треугольника при стандартных длинах сторон.

        Параметры на вход:
        a = 3 (float) - первая сторона треугольника 
        b = 4 (float) - вторая сторона треугольника
        c = 5 (float) - третья сторона треугольника

        Ожидаемый результат:
        perimeter = 3 + 4 + 5 = 12 (float)
        '''
        result = perimeter(3, 4, 5)
        self.assertEqual(result, 12)


    def test_perimeter_zero_side(self):
        '''
        Проверяет вычисление периметра треугольника при наличии нулевой стороны.

        Параметры на вход:
        a = 0 (float) - первая сторона треугольника 
        b = 0 (float) - вторая сторона треугольника
        c = 0 (float) - третья сторона треугольника

        Ожидаемый результат:
        perimeter = 0 + 0 + 0 = 0 (float)
        '''
        result = perimeter(0, 0, 0)
        self.assertEqual(result, 0)


    def test_area_basic(self):
        '''
        Проверяет вычисление площади треугольника при стандартных значениях.

        Параметры на вход:
        a = 10 (float) — основание
        h = 5  (float) — высота, проведенная к основанию

        Ожидаемый результат:
        area = 1/2 * 10 * 5 = 25 (float)
        '''
        result = area(10, 5)
        self.assertEqual(result, 25)


    def test_area_zero_height(self):
        '''
        Проверяет вычисление площади треугольника при нулевой высоте.

        Параметры на вход:
        a = 10 (float) — основание
        h = 0  (float) — высота, проведенная к основанию

        Ожидаемый результат:
        area = 1/2 * 10 * 0 = 0 (float)
        '''
        result = area(10, 0)
        self.assertEqual(result, 0)
