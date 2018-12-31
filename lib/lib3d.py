import numpy as np
from vecs import *
from pygame_colors import WHITE


class camera:
    def __init__(self,
                 pos=np.zeros(3),
                 dir=vector(1, 0, 0),
                 sw=500,
                 sh=500):
        self.pos = pos
        self.dir = dir
        self.sw = sw
        self.sh = sh
        self.normal = normalize(dir)
        self.screen_center = self.pos + self.normal
        self.points_on_screen = []

    def reset_points_on_screen(self):
        self.points_on_screen = []

    def get_screen_position(self, p):
        l = normalize(self.pos - p.pos)
        new_point = line_plance_intersection(self.screen_center,
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
