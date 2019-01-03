import numpy as np
from pygame_colors import WHITE


##### Functions #####

"""
Mathematical functions
"""

def vector(args=[], last=0):
    """
    Returns a 4-vector (x, y, z, 1)
    from a 3-tuple (x, y, z)
    """
    if len(args) > 3:
        raise ValueError('Max 3 elements allowed!')
    else:
        rest = [0] * (3-len(args))
    return np.hstack((args, rest, last))

def rotation_matrix(a=0, b=0, c=0):
    ca, sa = np.cos(a), np.sin(a)
    cb, sb = np.cos(b), np.sin(b)
    cc, sc = np.cos(c), np.sin(c)
    rot_x = np.array([[1, 0, 0],
                      [0, ca, -sa],
                      [0, sa, ca]])
    rot_y = np.array([[cb, 0, sb],
                      [0, 1, 0],
                      [-sb, 0, cb]])
    rot_z = np.array([[cc, -sc, 0],
                      [sc, cc, 0],
                      [0, 0, 1]])
    return np.dot(rot_z, np.dot(rot_y, rot_x))


##### Classes #####

class coordinate_system:
    """
    Represents a coordinate system
    """
    def __init__(self,
                 a=0, b=0, c=0,
                 pos=[0, 0, 0]):
        # Rotation block
        rotation_block = rotation_matrix(a, b, c)
        zeros = np.zeros(shape=(3,4))
        self.transformation_matrix = zeros
        self.transformation_matrix[:,:-1] = rotation_block

        # Translation row
        position = vector(pos, 1)
        self.transformation_matrix = np.vstack((self.transformation_matrix, position))


##### Tests? #####

v1 = vector([1, 2, 3], 0)
v2 = vector([2, 3], 1)
v3 = vector([1])
v4 = vector([])

for v in [v1, v2, v3, v4]:
    print(type(v), v)

coord = coordinate_system(5, 0, 0, [1, 3, 3])
print(coord.transformation_matrix)
