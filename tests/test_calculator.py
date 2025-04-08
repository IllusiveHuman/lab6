import unittest
from calculator_gui import calculate

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate("2+2"), "4")

    def test_subtraction(self):
        self.assertEqual(calculate("5-3"), "2")

    def test_multiplication(self):
        self.assertEqual(calculate("4*3"), "12")

    def test_division(self):
        self.assertEqual(calculate("8/2"), "4.0")

    def test_invalid_expression(self):
        self.assertEqual(calculate("5/0"), "Ошибка")

if __name__ == "__main__":
    unittest.main()
