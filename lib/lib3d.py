import numpy as np
from pygame_colors import WHITE


##### Functions #####

"""
Mathematical functions
"""

def vector(args=[]):
    """
    Returns a 4-vector (x, y, z, 1)
    from a 3-tuple (x, y, z)
    """
    if len(args) > 3:
        raise ValueError('Max 3 elements allowed!')
    else:
        rest = [0] * (3-len(args))
    return np.hstack((args, rest, 1))

##### Classes #####

class coordinate_system:
    """
    Represents a coordinate system
    """
    def __init__(self, pos, dir):
        pass

##### Tests? #####

v1 = vector([1, 2, 3])
v2 = vector([2, 3])
v3 = vector([1])
v4 = vector()

for v in [v1, v2, v3, v4]:
    print(type(v), v)
