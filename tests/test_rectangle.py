import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):

    def test_area_basic(self):
        '''
        Проверяет вычисление площади прямоугольника при стандартных входных данных.

        Параметры на вход:
        a = 5 (float) — первая сторона прямоугольника
        b = 10 (float) — вторая сторона прямоугольника

        Ожидаемый результат:
        area = 5 * 10 = 50 (float)
        '''
        result = area(5, 10)
        self.assertEqual(result, 50)


    def test_area_zero_side(self):
        '''
        Проверяет вычисление площади при наличии нулевой длины стороны.

        Параметры на вход:
        a = 10 (float) — первая сторона прямоугольника
        b = 0 (float) — вторая сторона прямоугольника

        Ожидаемый результат:
        area = 10 * 0 = 0 (float) — площадь равна нулю, т.к. одна из сторон равна 0
        '''
        result = area(10, 0)
        self.assertEqual(result, 0)


    def test_perimeter_basic(self):
        '''
        Проверяет вычисление периметра прямоугольника при стандартных значениях.

        Параметры на вход:
        a = 2 (float)  — первая сторона прямоугольника
        b = 7 (float) — вторая сторона прямоугольника

        Ожидаемый результат:
        perimeter = 2 * (2 + 7) = 18 (float)
        '''
        result = perimeter(2, 7)
        self.assertEqual(result, 18)


    def test_perimeter_square_case(self):
        '''
        Проверяет вычисление периметра, когда прямоугольник является квадратом.

        Параметры на вход:
        a = 5 (float) — первая сторона прямоугольника
        b = 5 (float) — вторая сторона прямоугольника

        Ожидаемый результат:
        perimeter = 2 * (5 + 5) = 20 (float)
        '''
        result = perimeter(5, 5)
        self.assertEqual(result, 20)


    def test_perimeter_zero_side(self):
        '''
        Проверяет вычисление периметра при нулевых длинах сторон.

        Параметры на вход:
        a = 0 (float) — первая сторона прямоугольника
        b = 0 (float) — вторая сторона прямоугольника

        Ожидаемый результат:
        perimeter = 0 (float), так как P = 2 * (0 + 0)
        '''
        result = perimeter(0, 0)
        self.assertEqual(result, 0)
