#!/usr/bin/env python3

import numpy as np
import sys
sys.path.append('lib')
from lib3d import camera, point
from vecs import *

cam = camera(pos=vector(0,30,0))
N = 100
ps = [point(pos=np.random.uniform(-10, 10, 3))
      for _ in range(N)]

for p in ps:
    cam.get_screen_position(p)
    p.print_data()
cam.print_points_on_screen()
