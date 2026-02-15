#Testing and verifying output for task5.py
import pytest
from task5 import list_slicing, student_dict

#Test cases
#Sliced list with first three books
def test_list_slicing(capsys):
    list_slicing()
    captured = capsys.readouterr() #Captures stdout

    #First three books and authors
    assert captured.out == "['Before the Coffee gets Cold, Toshikazu Kawaguchi', 'Piranesi, Susanna Clarke', 'Hamnet, Maggie OFarrell']\n"

#Requested student ID
def test_student_dict(capsys):
    student_dict("Nyx")
    captured = capsys.readouterr() #Captures stdout
    assert captured.out == "777767\n" #Student ID of Nyx