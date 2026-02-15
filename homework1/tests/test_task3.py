#Testing and verifying output for task3.py
import pytest
from task3 import check_sign, ten_prime, sum_to_hundred

#Test cases
#Positive number
def test_check_sign_pos():
    number = 6
    assert check_sign(number) == "Positive"

#Negative number
def test_check_sign_neg():
    number = -6
    assert check_sign(number) == "Negative"

#Positive number
def test_check_sign_zero():
    number = 0
    assert check_sign(number) == "Zero"

#First 10 expected prime numbers
def test_ten_prime(capsys):
    ten_prime()
    captured = capsys.readouterr() #Captures stdout
    assert captured.out == "2\n3\n5\n7\n11\n13\n17\n19\n23\n29\n"

#Expected sum of all numbers 1 to 100
def test_sum_to_hundred():
    assert sum_to_hundred() == 5050 #Sum of numbers 1 to 100