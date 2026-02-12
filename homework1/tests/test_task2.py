#Testing and verifying output for task2.py
import pytest
from task2 import int_mult, float_add, string_concat, boolean_truth

#Test cases
def test_int():
    assert int_mult() == 6

def test_float():
    assert float_add() == 12.33

def test_string():
    assert string_concat() == "HelloWorld!"

def test_boolean():
    assert boolean_truth() == True