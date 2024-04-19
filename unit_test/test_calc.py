import unittest
import traceback


def get_function_name():
    return traceback.extract_stack(None, 2)[0][2]


import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        print(f'\t{get_function_name()}')

        self.assertEqual(calc.add(10, 5), 10 + 5)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        print(f'\t{get_function_name()}')

        self.assertEqual(calc.subtract(10, 5), 10 - 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        print(f'\t{get_function_name()}')

        self.assertEqual(calc.multiply(10, 5), 10 * 5)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        print(f'\t{get_function_name()}')
        self.assertEqual(calc.divide(10, 5), 10 / 5)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 5 / 2)

        with self.assertRaises(ValueError):
            calc.divide(10, 0)


print(f'Testing calc.py\n')
if __name__ == '__main__':
    unittest.main()
