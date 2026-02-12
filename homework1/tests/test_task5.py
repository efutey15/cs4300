#Testing and verifying output for task1.py
import pytest
from task5 import list_slicing, student_dict

#Test cases
def test_list_slicing(capsys):
    list_slicing()
    captured = capsys.readouterr() #Captures stdout
    assert captured.out == "['Before the Coffee gets Cold, Toshikazu Kawaguchi', 'Piranesi, Susanna Clarke', 'Hamnet, Maggie OFarrell']\n"

def test_student_dict(capsys):
    student_dict("Nyx")
    captured = capsys.readouterr() #Captures stdout
    assert captured.out == "777767\n"