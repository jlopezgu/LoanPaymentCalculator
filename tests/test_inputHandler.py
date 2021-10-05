import pytest
import sys

from calculator.inputHandler import InputHandler


def test_parse_data():
    data = ['amount:12000', 'interest:0.01', 'downpayment:0', 'term:12']
    sys.stdin = data
    inputHandler = InputHandler()
    inputHandler.read_data()
    inputHandler.parse_data()
    assert inputHandler.term == 12
    assert inputHandler.amount == 12000
    assert inputHandler.interest == 0.01/100
    assert inputHandler.down_payment == 0


def test_missing_term():
    data = ['amount:12000', 'interest:0.01', 'downpayment:0']
    sys.stdin = data
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        inputHandler = InputHandler()
        inputHandler.read_data()
        inputHandler.parse_data()
    assert pytest_wrapped_e.type == SystemExit


def test_missing_amount():
    data = ['interest:0.01', 'downpayment:0', 'term:12']
    sys.stdin = data
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        inputHandler = InputHandler()
        inputHandler.read_data()
        inputHandler.parse_data()
    assert pytest_wrapped_e.type == SystemExit


def test_missing_interest():
    data = ['amount:12000', 'downpayment:0', 'term:12']
    sys.stdin = data
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        inputHandler = InputHandler()
        inputHandler.read_data()
        inputHandler.parse_data()
    assert pytest_wrapped_e.type == SystemExit
