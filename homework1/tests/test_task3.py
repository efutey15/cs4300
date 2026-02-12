#Testing and verifying output for task 3
import pytest
from task3 import check_sign, ten_prime, sum_to_hundred

#Test cases
def test_check_sign():
    assert check_sign() == "Positive"

def test_ten_prime(capsys):
    ten_prime()
    captured = capsys.readouterr() #Captures stdout
    assert captured.out == "2\n3\n5\n7\n11\n13\n17\n19\n23\n29\n"

def test_sum_to_hundred():
    assert sum_to_hundred() == 5050