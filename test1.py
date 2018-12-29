#!/usr/bin/env python3

import numpy as np
import sys
sys.path.append('lib')
from lib3d import camera
from vecs import *

vec = normalize(np.random.uniform(-1, 1, size=3).astype(np.float64))
a, b, c = angles(vec)
print(vec)
