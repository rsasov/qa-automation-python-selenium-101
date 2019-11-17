import unittest

import calculator


class CalculatorTestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(0, -2), -2)
        self.assertEqual(calculator.add(10, -2), 8)
        self.assertEqual(calculator.add(10, 12), 22)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(1, 2), -1)
        self.assertEqual(calculator.subtract(10, 2), 8)
        self.assertEqual(calculator.subtract(-10, 2), -12)
        self.assertEqual(calculator.subtract(-10, -6), -4)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(5, 3), 15)
        self.assertEqual(calculator.multiply(6, 8), 48)
        self.assertEqual(calculator.multiply(-1, 2), -2)
        self.assertEqual(calculator.multiply(-7, -3), 21)

    def test_divide(self):
        self.assertEqual(calculator.divide(5, 4), 1.25)
        self.assertEqual(calculator.divide(12, 2), 6)
        self.assertEqual(calculator.divide(-18, 2), -9)
        self.assertEqual(calculator.divide(-20, -2), 10)


if __name__ == '__main__':
    unittest.main()