import unittest
from exponentiation_func import exponentiation

class ExponentiationTest(unittest.TestCase):

    def test_exponentiation_with_positive_base_and_exponent(self):
        self.assertEqual(exponentiation(2, 2), 4)
        self.assertEqual(exponentiation(5, 3), 125)
        self.assertEqual(exponentiation(2, 3), 8)

    def test_exponentiation_with_negative_base_and_exponent(self):

        self.assertEqual(exponentiation(-2, 3), -8)
        self.assertEqual(exponentiation(-2, -3), -0.125)


    def test_exponentiation_with_base_as_zero(self):
        self.assertEqual(exponentiation(0, 1), 0)
        self.assertEqual(exponentiation(0, 100), 0)

    def test_exponentiation_with_exponent_as_zero(self):
        self.assertEqual(exponentiation(1, 0), 1)
        self.assertEqual(exponentiation(5, 0), 1)
        self.assertEqual(exponentiation(9, 0), 1)

    def test_exponentiation_with_base_as_zero_and_negative_exponent(self):
        with self.assertRaises(ZeroDivisionError):
            exponentiation(0, -3)



