#!/usr/bin/env python3

import pygame
import sys
sys.path.append('lib')
from lib3d import *


WIDTH = 640
HEIGHT = 480
FPS = 30

# Inititialize 3d stuff
world_coord = coordinate_system()
cam = camera([0, 0, 5])
points = [object(world_coord, [i, j, k])
          for i in range(2)
          for j in range(2)
          for k in range(2)]

for i, p in enumerate(points):
    cam.add_object(p)

cam.draw_object(screen=1)
sys.exit()
# Inititialize pygame and create a window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Title')
clock = pygame.time.clock()

# Game loop
running = True
while running:
    # Inputs
    # Screen update
    # Draw / Render
    screen.fill(color)

    # Flip display (after drawing everything)
    pygame.display.flip()
