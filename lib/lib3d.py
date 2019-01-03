import numpy as np
import pygame
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
    rot_x = np.array([[1, 0, 0, 0],
                      [0, ca, -sa, 0],
                      [0, sa, ca, 0],
                      [0, 0, 0, 1]])
    rot_y = np.array([[cb, 0, sb, 0],
                      [0, 1, 0, 0],
                      [-sb, 0, cb, 0],
                      [0, 0, 0, 1]])
    rot_z = np.array([[cc, -sc, 0, 0],
                      [sc, cc, 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])
    return np.dot(rot_z, np.dot(rot_y, rot_x))


def dim_color(color, distance):
    new_color = np.array(color)
    return color * 10 / distance

##### Classes #####

class coordinate_system:
    """
    Represents a coordinate system.
    """
    def __init__(self,
                 pos=[0, 0, 0],
                 a=0, b=0, c=0):
        # Rotation block
        self.transformation_matrix = rotation_matrix(a, b, c)
        self.transformation_matrix[-1] = vector(pos, 1)
        # Inverse matrix
        self.transformation_matrix_inv = np.linalg.inv(self.transformation_matrix)

    def translate(self, vec):
        self.transformation_matrix[-1] += vec
        self.transformation_matrix_inv = np.linalg.inv(self.transformation_matrix)

    def rotate(self, a=0, b=0, c=0):
        self.transformation_matrix = np.dot(rotation_matrix(a, b, c), self.transformation_matrix)
        self.transformation_matrix_inv = np.linalg.inv(self.transformation_matrix)

class object:
    """
    (at the moment only a point with a position
    and rotation values)
    """
    def __init__(self,
                 coord_sys,
                 pos=[0, 0, 0],
                 rad=1,
                 color=WHITE):
        self.coord_sys = coord_sys
        self.pos = vector(pos, 1)
        self.rad = rad
        self.color = color
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)
        if self not in neighbor.neighbors:
            neighbor.neighbors.append(self)

    def add_neighbors(self, list):
        for neighbor in list:
            self.add_neighbor(neighbor)

    def reset_neighbors(self):
        self.neighbors = []


class camera:
    """
    A cemara.
    """
    def __init__(self,
                 pos=[0, 0, 0],
                 a=0, b=0, c=0,
                 screen=None,
                 sW=640, sH=480):
        self.coord_sys = coordinate_system(pos=pos,
                                           a=a, b=b, c=c)
        self.screen = screen
        self.sW = sW
        self.sH = sH
        self.objects = []

    def reset_objects(self):
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def draw_object(self, obj):
        # NOTE: Should first transform using own coords,
        # at the moment only world coordinate system exists
        pos_cam = np.dot(obj.pos, self.coord_sys.transformation_matrix)
        if pos_cam[2] > 0:
            # Draw points
            screen_x = int(-1 * (pos_cam[0] / pos_cam[2]) * self.sW) + self.sW // 2
            screen_y = int(-1 * (pos_cam[1] / pos_cam[2]) * self.sH) + self.sH // 2
            pos_screen = (screen_x, screen_y)

            # Calculate visible radius
            vis_rad = int(obj.rad * 10/pos_cam[2])
            pygame.draw.circle(self.screen, obj.color, pos_screen, vis_rad)

            # Dim color
            vis_color = dim_color(obj.color, pos_cam[2])

            # Draw lines
            for neighbor in obj.neighbors:
                pos_cam2 = np.dot(neighbor.pos, self.coord_sys.transformation_matrix)
                screen_x2 = int(-1 * (pos_cam2[0] / pos_cam2[2]) * self.sW) + self.sW // 2
                screen_y2 = int(-1 * (pos_cam2[1] / pos_cam2[2]) * self.sH) + self.sH // 2
                pos_screen2 = (screen_x2, screen_y2)
                pygame.draw.line(self.screen, vis_color, pos_screen, pos_screen2, 2)

    def draw_all_objects(self):
        for obj in self.objects:
            self.draw_object(obj)

    def translate(self, vec):
        self.coord_sys.translate(vec)

    def rotate(self, a=0, b=0, c=0):
        self.coord_sys.rotate(a, b, c)


def make_neighbors(obj1, obj2):
    obj1.add_neighbor(obj2)
