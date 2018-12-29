import numpy as np
from vecs import *
from pygame_colors import WHITE


class camera:
    def __init__(self,
                 pos=np.zeros(3),
                 dir=np.zeros(3),
                 sw=500,
                 sh=500):
        self.pos = pos
        self.dir = dir
        self.sw = sw
        self.sh = sh
        self.normal = normalize(dir)
        self.screen_center = vec_add(self.pos, self.normal)


class point:
    def __init__(self,
                 pos,
                 color=WHITE,
                 radius=1):
        self.pos = pos
        self.color = color
        self.radius = radius
