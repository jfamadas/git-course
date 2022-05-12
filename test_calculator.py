import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator.add(3, 6), 9)

    def test_substract(self):
        self.assertEqual(Calculator.subtract(3, 10), -7)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(2.5, 7), 17.5)

    def test_divide(self):
        self.assertEqual(Calculator.divide(10, 4), 2.5)

    def test_zerodiv(self):
        with self.assertRaises(ValueError):
            Calculator.divide(1, 0)

    def test_add_int_with_str(self):
        with self.assertRaises(TypeError):
            Calculator.add(1, "3")

    def test_sqrt(self):
        self.assertEqual(Calculator.sqrt(16), 4)

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            Calculator.sqrt(-1)


if __name__ == '__main__':
    unittest.main()
