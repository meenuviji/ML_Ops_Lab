# test/test_unittest.py
import unittest
from src.calculator import fun1, fun2, fun3, fun4, fun5, fun6

class TestCalculator(unittest.TestCase):
    def test_fun1(self):
        self.assertEqual(fun1(2, 3), 5)

    def test_fun2(self):
        self.assertEqual(fun2(5, 3), 2)

    def test_fun3(self):
        self.assertEqual(fun3(4, 3), 12)

    def test_fun4(self):
        self.assertEqual(fun4(2, 3, 4), 9)

    # --- NEW: fun5 (division) ---
    def test_fun5_basic(self):
        self.assertEqual(fun5(10, 2), 5)

    def test_fun5_float(self):
        self.assertEqual(fun5(7, 2), 3.5)

    def test_fun5_zerodivision(self):
        with self.assertRaises(ValueError):
            fun5(1, 0)

    # --- NEW: fun6 (power) ---
    def test_fun6_power(self):
        self.assertEqual(fun6(2, 5), 32)

    def test_fun6_float_power(self):
        self.assertEqual(fun6(4, 0.5), 2)

    def test_type_validation(self):
        with self.assertRaises(ValueError):
            fun6("a", 2)
        with self.assertRaises(ValueError):
            fun5(10, "b")

if __name__ == "__main__":
    unittest.main()
