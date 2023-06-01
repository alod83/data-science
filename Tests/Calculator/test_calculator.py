import pytest
from calculator import *

def test_addition():
    result = add(2, 4)
    assert result == 6

    result = add(-1, 3)
    assert result == 2

    result = add(0, 0)
    assert result == 0

def test_addition():
    result = add(2, 3)
    assert result == 5

    result = add(-1, 5)
    assert result == 4

    result = add(0, 0)
    assert result == 0

def test_subtraction():
    result = subtract(5, 2)
    assert result == 3

    result = subtract(10, -3)
    assert result == 13

    result = subtract(0, 0)
    assert result == 0

def test_multiplication():
    result = multiply(2, 3)
    assert result == 6

    result = multiply(-4, 5)
    assert result == -20

    result = multiply(0, 100)
    assert result == 0

def test_division():
    result = divide(10, 2)
    assert result == 5

    result = divide(25, -5)
    assert result == -5

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
