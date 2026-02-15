#Testing and verifying output for task6.py
import pytest
from task6 import count_words

#Test case, expected number of words
def test_count_words():
    assert count_words() == 104 #Number of words in the file