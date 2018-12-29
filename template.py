#!/usr/bin/env python3

import pygame


WIDTH = 640
HEIGHT = 480
FPS = 30

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
