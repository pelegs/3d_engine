#!/usr/bin/env python3

import numpy as np
import sys
sys.path.append('lib')
from lib3d import *

N = 10
ps = [point(pos=np.random.uniform(-10, 10, 3) - vector(10,0,0))
      for _ in range(N)]
cam = camera(pos=vector(30,0,0))

for p in ps:
    cam.get_screen_position(p)
    cam.rotate_screen_to_z()
    #p.print_data()
#cam.print_points_on_screen()
print(' '.join(map(str, cam.pos)), 2)
