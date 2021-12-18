import unittest
from functions_for_testing import *
import math
import numpy as np
import time


# тесты для проверки корректности функций поиска минимума, максимума, сложения и умножения
class TestCalc(unittest.TestCase):
    with open('test_input.txt', 'w', encoding='utf-8') as file:
        print(*np.random.randint(-100, 100, 20), file=file)  # генерируем файл с рандомными значениями

    def setUp(self):
        self.calculator = read_file('test_input.txt')

    def test_min(self):
        self.assertEqual(minim(self.calculator), min(self.calculator))

    def test_max(self):
        self.assertEqual(maxim(self.calculator), max(self.calculator))

    def test_sum(self):
        self.assertEqual(summa(self.calculator), sum(self.calculator))

    def test_compose(self):
        self.assertEqual(compose(self.calculator), math.prod(self.calculator))


class TestTime(unittest.TestCase):  # тесты для проверки скорости работы программы при увеличении размера входного файла
    def test_time(self):  # нагрузочное тестирование
        with open('test_time_input.txt', 'w', encoding='utf-8') as file:
            for i in range(10000, 100000, 5000):
                with self.subTest(i=i):
                    print(*np.random.randint(-100, 100, i), file=file)
                    start = time.time()
                    main('test_time_input.txt')
                    end = time.time()
                    self.assertTrue(end-start < 1)  # ограничение по времени 0.1 секунда


class AnyTest(unittest.TestCase):  # на оценку 4 - тестируем ошибку при неверном формате данных в файле
    def test_error(self):
        with self.assertRaises(ValueError):
            read_file('test_error.txt')


if __name__ == "__main__":
    unittest.main()
