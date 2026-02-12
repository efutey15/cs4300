#Testing and verifying output for task1.py
import pytest
from task1 import say_hello

#Test case
def test_result(capsys):
    say_hello()
    captured = capsys.readouterr() #Captures stdout
    assert captured.out == "Hello, World!\n" #Asserts that expected output == captured output