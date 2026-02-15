#Testing and verifying output for task7.py
import numpy as np
import pytest
from task7 import normalize_vector

#Test Cases
#Normal case
def test_normalize_vector():
    v = np.array([3, 4])
    result = normalize_vector(v)
    expected = np.array([0.6, 0.8])

    assert np.allclose(result, expected)

#Zero vector error
def test_normalize_vector_VE():
    with pytest.raises(ValueError):
        normalize_vector([0, 0, 0])