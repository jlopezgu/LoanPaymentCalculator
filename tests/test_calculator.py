from calculator.calculator import Calculator
import pytest


def test_calculator():
    calculator = Calculator(amount=100000, interest=5.5/100, down_payment=20000, term=30)
    result = calculator.calculate()
    assert result == {'monthly payment': 454.23, 'total payment': 163522.8, 'total interest': 83522.8}


def test_no_interest():
    calculator = Calculator(amount=100000, interest=0.0 / 100, down_payment=20000, term=30)
    with pytest.raises(ZeroDivisionError) as pytest_wrapped_e:
        calculator.calculate()
    assert pytest_wrapped_e.type == ZeroDivisionError


def test_no_amount():
    calculator = Calculator(amount=0, interest=5.5 / 100, down_payment=0, term=5)
    result = calculator.calculate()
    assert result == {'monthly payment': 0.0, 'total interest': 0.0, 'total payment': 0.0}


def test_no_values():
    calculator = Calculator(amount=0, interest=0.0, down_payment=0, term=0)
    with pytest.raises(ZeroDivisionError) as pytest_wrapped_e:
        calculator.calculate()
    assert pytest_wrapped_e.type == ZeroDivisionError
