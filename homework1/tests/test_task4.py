#Testing and verifying output for task4.py
import pytest
from task4 import calculate_discount

#Test Cases for calculate_discount(price, discount)
def test_int_int():
    assert calculate_discount(10, 40) == 6.00

def test_int_float():
    assert calculate_discount(10, 0.5) == 5.00

def test_float_int():
    assert calculate_discount(10.00, 60) == 4.00

def test_float_float():
    assert calculate_discount(10.00, 0.3) == 7.00