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
    Represents a coordinate system.
    """
    def __init__(self,
                 pos=[0, 0, 0],
                 a=0, b=0, c=0):
        # Rotation block
        rotation_block = rotation_matrix(a, b, c)
        zeros = np.zeros(shape=(3,4))
        self.transformation_matrix = zeros
        self.transformation_matrix[:,:-1] = rotation_block
        # Translation row
        position = vector(pos, 1)
        self.transformation_matrix = np.vstack((self.transformation_matrix, position))
        # Inverse matrix
        self.transformation_matrix_inv = np.linalg.inv(self.transformation_matrix)


class object:
    """
    (at the moment only a point with a position
    and rotation values)
    """
    def __init__(self,
                 coord_sys,
                 pos=[0, 0, 0],
                 color=WHITE):
        self.coord_sys = coord_sys
        self.pos = vector(pos, 1)
        self.color = color


class camera:
    """
    A cemara.
    """
    def __init__(self,
                 pos=[0, 0, 0],
                 a=0, b=0, c=0,
                 sW=640, sH=480):
        self.coord_sys = coordinate_system(pos=pos,
                                           a=a, b=b, c=c)
        self.sW = sW
        self.sH = sH
        self.objects = []

    def reset_objects(self):
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def draw_object(self, screen):
        for obj in self.objects:
            # NOTE: Should first transform using own coords,
            # at the moment only world coordinate system exists
            pos_cam = np.dot(obj.pos, self.coord_sys.transformation_matrix)
            if pos_cam[2] != 0:
                screen_x = int(-1 * (pos_cam[0] / pos_cam[2]) * self.sW) + self.sW // 2
                screen_y = int(-1 * (pos_cam[1] / pos_cam[2]) * self.sH) + self.sH // 2
                pos_screen = (screen_x, screen_y)
                print(pos_screen)


##### Tests? #####

