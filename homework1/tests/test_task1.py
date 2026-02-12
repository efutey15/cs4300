#Testing and verifying output for task1.py
import pytest

#Contents of task1
def say_hello():
    print("Hello, World!")

#Test case
def test_result(capsys):
    say_hello()
    captured = capsys.readouterr() #Captures stdout
    assert captured.out == "Hello, World!\n" #Asserts that expected output == captured output