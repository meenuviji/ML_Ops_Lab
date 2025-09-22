# test/test_pytest.py
import pytest
from src.calculator import fun1, fun2, fun3, fun4, fun5, fun6

def test_fun1():
    assert fun1(2, 3) == 5

def test_fun2():
    assert fun2(5, 3) == 2

def test_fun3():
    assert fun3(4, 3) == 12

def test_fun4():
    assert fun4(2, 3, 4) == 9

# --- NEW: fun5 (division) ---
def test_fun5_basic():
    assert fun5(10, 2) == 5

def test_fun5_float():
    assert fun5(7, 2) == 3.5

def test_fun5_zerodivision():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        fun5(1, 0)

# --- NEW: fun6 (power) ---
@pytest.mark.parametrize("x,y,expected", [
    (2, 5, 32),
    (3, 3, 27),
    (4, 0.5, 2),
])
def test_fun6_param(x, y, expected):
    assert fun6(x, y) == expected

def test_type_validation():
    with pytest.raises(ValueError):
        fun6("a", 2)
    with pytest.raises(ValueError):
        fun5(10, "b")
