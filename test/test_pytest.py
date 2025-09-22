# test/test_pytest.py
import pytest
from src.currency_converter import (
    convert, add_rate, set_rates, get_rate, list_currencies, reset_rates
)

@pytest.fixture(autouse=True)
def fresh_rates():
    # Reset table before every test
    reset_rates()

def test_usd_to_eur():
    assert convert(100, "USD", "EUR") == 92.00

def test_eur_to_inr():
    # 100 / 0.92 * 84 = 9130.434... -> 9130.43
    assert convert(100, "EUR", "INR") == 9130.43

def test_same_currency_rounds():
    assert convert(50, "INR", "INR") == 50.00

def test_negative_amount_allowed():
    assert convert(-10, "USD", "EUR") == -9.20

def test_unknown_currency_src():
    with pytest.raises(ValueError, match="Unknown currency: ABC"):
        convert(10, "ABC", "USD")

def test_unknown_currency_dst():
    with pytest.raises(ValueError, match="Unknown currency: ABC"):
        convert(10, "USD", "ABC")

def test_add_rate_and_convert():
    add_rate("AED", 3.67)
    # 100 AED -> USD = 100 / 3.67 = 27.248... -> 27.25
    assert convert(100, "AED", "USD") == 27.25

def test_set_rates_custom_table():
    set_rates({"USD": 1.0, "EUR": 1.0, "INR": 100.0})
    assert convert(1, "USD", "INR") == 100.00
    assert get_rate("EUR") == 1.0

def test_list_currencies_has_usd():
    assert "USD" in list_currencies()
