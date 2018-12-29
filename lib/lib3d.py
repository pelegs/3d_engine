import numpy as np
from vecs import *


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

    def calc_screen_pos(self, p):
        connecting_line = vec_sub(p.pos, self.pos)
        direction = normalize(connecting_line)
        d = (self.screen_center - p.pos) / dot(

class point:
    def __init__(self,
                 pos,
                 color=WHITE,
                 radius=1)
