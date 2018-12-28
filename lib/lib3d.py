import numpy as np
from vecs import *


class camera:
    def __init__(self,
                 pos=np.zeros(3),
                 dir=np.zeros(3),
                 sd=1,
                 sw=500,
                 sh=500):
        self.pos = pos
        self.dir = dir
        self.sd = sd
        self.sw = sw
        self.sh = sh
        self.normal = normalize(dir)
