#!/usr/bin/env python3

import pygame
import sys
sys.path.append('lib')
from lib3d import *
from pygame_colors import BLACK, WHITE


WIDTH = 600
HEIGHT = 600
FPS = 30


def move(x, y, z):
    dir = vector([x, y, z])
    cam.translate(dir)

def handle_keys():
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        move(0, 0, -0.01)
    if key[pygame.K_DOWN]:
        move(0, 0, 0.01)
    if key[pygame.K_a]:
        cam.rotate(0, 0, np.pi/500)
    if key[pygame.K_d]:
        cam.rotate(0, 0, -np.pi/500)
    if key[pygame.K_LEFT]:
        cam.rotate(0, np.pi/500, 0)
    if key[pygame.K_RIGHT]:
        cam.rotate(0, -np.pi/500, 0)
    if key[pygame.K_w]:
        cam.rotate(np.pi/500, 0, 0)
    if key[pygame.K_x]:
        cam.rotate(-np.pi/500, 0, 0)


# Inititialize pygame and create a window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Title')
clock = pygame.time.Clock()

# Inititialize 3d stuff
world_coord = coordinate_system()
cam = camera([0, 0, 5], screen=screen, sW=WIDTH, sH=HEIGHT)
points = [object(world_coord, [i, j, k])
          for i in [-1, 1]
          for j in [-1, 1]
          for k in [-1, 1]]
make_neighbors(points[0], points[1])
make_neighbors(points[0], points[2])
make_neighbors(points[0], points[4])
make_neighbors(points[1], points[3])
make_neighbors(points[2], points[6])
make_neighbors(points[2], points[3])
make_neighbors(points[3], points[7])
make_neighbors(points[4], points[5])
make_neighbors(points[4], points[6])
make_neighbors(points[5], points[1])
make_neighbors(points[5], points[7])
make_neighbors(points[6], points[7])

# TEMP
trans_vec = vector([0, 0, 0])

# Game loop
running = True
while running:
    # Inputs
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
                break
    handle_keys()

    # Actions
    for i, p in enumerate(points):
        cam.add_object(p)

    # Draw / Render
    screen.fill(BLACK)
    cam.draw_all_objects()

    # Reset
    cam.reset_objects()

    # Flip display (after drawing everything)
    pygame.display.flip()

pygame.quit()
sys.exit()
