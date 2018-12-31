import numpy as np
from pygame_colors import WHITE


##### Functions #####

"""
Mathematical functions
"""

def normalize(vec):
    L = np.linalg.norm(vec)
    if L == 0:
        raise ValueError('can not normalize the zero-vector!')
    else:
        return vec / L

def distance2(v1, v2):
    return np.linalg.norm(v1-v2)

def distance(v1, v2):
    return np.sqrt(distance2(v1, v2))

def vector(x, y, z):
    return np.array([x, y, z])

def line_plane_intersection(p0, l, l0, n):
    numerator = np.dot((p0-l0), n)
    denominator = np.dot(l, n)
    if denominator == 0:
        return False
    else:
        d = numerator / denominator
        return l0 + d*l


##### Classes #####

class camera:
    def __init__(self,
                 pos=np.zeros(3),
                 dir=vector(1, 1, -2),
                 sw=500,
                 sh=500):
        self.pos = pos
        self.dir = dir
        self.sw = sw
        self.sh = sh
        self.normal = normalize(dir)
        self.screen_center = self.pos - self.dir
        self.points_on_screen = []

    def reset_points_on_screen(self):
        self.points_on_screen = []

    def get_screen_position(self, p):
        l = normalize(self.pos - p.pos)
        new_point = line_plane_intersection(self.screen_center,
                                            l, p.pos, self.normal)
        self.points_on_screen.append(new_point)

    def print_points_on_screen(self):
        for p in self.points_on_screen:
            print(' '.join(map(str, p)), 1)


class point:
    def __init__(self,
                 pos,
                 color=WHITE,
                 radius=1):
        self.pos = pos
        self.color = color
        self.radius = radius

    def print_data(self):
        print(' '.join(map(str, self.pos)), 0)
