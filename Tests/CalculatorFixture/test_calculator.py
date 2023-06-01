import pytest
from calculator import *

@pytest.fixture
def calculator():
    # Create an instance of the calculator
    calc = Calculator()
    return calc

def test_addition(calculator):
    result = calculator.add(2, 3)
    assert result == 5

def test_subtraction(calculator):
    result = calculator.subtract(5, 2)
    assert result == 3

def test_multiplication(calculator):
    result = calculator.multiply(4, 3)
    assert result == 12

def test_division(calculator):
    result = calculator.divide(10, 2)
    assert result == 5