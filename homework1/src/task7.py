#Task 7: Numpy showcase
import numpy as np

#Normalizing a vecotr to have a magnitude of 1
def normalize_vector(v):
    v = np.array(v, dtype=float)
    normal = np.linalg.norm(v)

    if normal == 0:
        raise ValueError("Cannot normalize the zero vector")
    
    return v / normal