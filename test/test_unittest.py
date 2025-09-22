# test/test_unittest.py
import unittest
from src.currency_converter import (
    convert, add_rate, set_rates, get_rate, list_currencies, reset_rates
)

class TestCurrencyConverter(unittest.TestCase):
    def setUp(self):
        reset_rates()

    def test_usd_to_eur(self):
        self.assertEqual(convert(100, "USD", "EUR"), 92.00)

    def test_eur_to_inr(self):
        self.assertEqual(convert(100, "EUR", "INR"), 9130.43)

    def test_same_currency(self):
        self.assertEqual(convert(50, "INR", "INR"), 50.00)

    def test_negative_amount_allowed(self):
        self.assertEqual(convert(-10, "USD", "EUR"), -9.20)

    def test_unknown_currency_src(self):
        with self.assertRaisesRegex(ValueError, "Unknown currency: ABC"):
            convert(10, "ABC", "USD")

    def test_unknown_currency_dst(self):
        with self.assertRaisesRegex(ValueError, "Unknown currency: ABC"):
            convert(10, "USD", "ABC")

    def test_add_rate_and_convert(self):
        add_rate("AED", 3.67)
        self.assertEqual(convert(100, "AED", "USD"), 27.25)

    def test_set_rates_custom_table(self):
        set_rates({"USD": 1.0, "EUR": 1.0, "INR": 100.0})
        self.assertEqual(convert(1, "USD", "INR"), 100.00)
        self.assertEqual(get_rate("EUR"), 1.0)

    def test_list_currencies_has_usd(self):
        self.assertIn("USD", list_currencies())

if __name__ == "__main__":
    unittest.main()
