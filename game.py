#!/usr/bin/env python3

import pygame
import sys
import math
from math import pi

pygame.init()
size = width, height = 400, 600
screen = pygame.display.set_mode(size)

def angle(vector1, vector2):
    x1, y1 = vector1
    x2, y2 = vector2
    inner_product = x1*x2 + y1*y2
    len1 = math.hypot(x1, y1)
    len2 = math.hypot(x2, y2)
    return math.acos(inner_product/(len1*len2))


def drawArc(center, direction, theta):
    (dx, dy) = direction
    (cx, cy) = center
    length = math.sqrt(dx**2 + dy**2)
    rect = [cx-length, cy-length,2*length, 2*length]

    myAngle = math.copysign(angle(direction, (1,0)),dy)

    #theta = 0, 

    pygame.draw.arc(screen, (255,255,255), rect, myAngle-theta/2, myAngle+theta/2, 2)




screen.fill((0,0,0))





while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    key_input = pygame.key.get_pressed()   
    if key_input[pygame.K_SPACE]:
        drawArc((100,100), (-50,-50), pi/4)
    for i in range(1,10):
        drawArc((200,300), (i*10, i*10), pi/4)
    




    pygame.display.update()




