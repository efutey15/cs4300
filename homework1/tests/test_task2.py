#Testing and verifying output for task2.py
import pytest
from task2 import int_mult, float_add, string_concat, boolean_truth

#Test cases
def test_int():
    int1 = 2
    int2 = 3
    assert int_mult(int1, int2) == 6

def test_float():
    num1 = 5.55
    num2 = 6.78
    assert float_add(num1, num2) == 12.33

def test_string():
    str1 = "Hello"
    str2 = "World!"
    assert string_concat(str1, str2) == "HelloWorld!"

def test_boolean():
    color = "blue"
    assert boolean_truth(color) == True