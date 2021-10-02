#!/usr/bin/env python3

import pygame
import sys
from math import pi

pygame.init()
size = width, height = 400, 600
screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    screen.fill((0,0,0))

    pygame.draw.arc(screen, (255,255,255), [50,50,50,50], pi/2, pi, 2)

    pygame.display.flip()
