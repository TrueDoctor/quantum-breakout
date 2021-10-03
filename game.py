#!/usr/bin/env python3

import pygame
import sys
import math
from math import pi
from pygame.math import Vector2 as Vec2

from paddle import Paddle
from ball import Ball
from brick import Brick
from slit import Slit
from wall import Wall
from colors import *
import wave
from wave import Arc
from wave import Beam
from wave import Wavefront

pygame.init()


score = 0
lives = 3

# Open a new Window
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Quantum Breakout")

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

#Create the Paddle
paddleLeftest = Paddle(paddle1, 20, 10)
paddleLeftest.rect.x = 200
paddleLeftest.rect.y = 560

paddleLeft = Paddle(paddle2, 20, 10)
paddleLeft.rect.x = 220
paddleLeft.rect.y = 560

paddleCenter = Paddle(paddle3, 20, 10)
paddleCenter.rect.x = 240
paddleCenter.rect.y = 560

paddleRight = Paddle(paddle4, 20, 10)
paddleRight.rect.x = 260
paddleRight.rect.y = 560

paddleRightest = Paddle(paddle5, 20, 10)
paddleRightest.rect.x = 280
paddleRightest.rect.y = 560

#Create the ball sprite
ball = Ball(white, 20, 20, pygame.Vector2(345, 195), pygame.Vector2(4,4))

brickEndPoints = []
wallEndPoints = []
slitEndPoints = []
allEndPoints = []

all_bricks = pygame.sprite.Group()
for i in range(7):
    brick = Brick(red, 80)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)
    brickEndPoints.append([(brick.rect.x, brick.rect.y), (brick.rect.x+brick.myWidth, brick.rect.y)])
for i in range(7):
    brick = Brick(orange, 80)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)
    brickEndPoints.append([(brick.rect.x, brick.rect.y), (brick.rect.x+brick.myWidth, brick.rect.y)])
for i in range(7):
    brick = Brick(yellow, 80)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)
    brickEndPoints.append([(brick.rect.x, brick.rect.y), (brick.rect.x+brick.myWidth, brick.rect.y)])

all_slits = pygame.sprite.Group()
for i in range(3):
    slit = Slit(white, 10)
    slit.rect.x = 195 + i * 200
    slit.rect.y = 350
    all_sprites_list.add(slit)
    all_slits.add(slit)
    slitEndPoints.append([(slit.rect.x, slit.rect.y), (slit.rect.x+slit.myWidth, slit.rect.y)])

all_walls = pygame.sprite.Group()
for i in range(2):
    wall = Wall(gray, 190)
    wall.rect.x = 205 + i * 200
    wall.rect.y = 350
    all_sprites_list.add(wall)
    all_walls.add(wall)
    wallEndPoints.append([(wall.rect.x, wall.rect.y), (wall.rect.x+wall.myWidth, wall.rect.y)])

allEndPoints = brickEndPoints + slitEndPoints + wallEndPoints


# Add the paddle to the list of sprites
all_sprites_list.add(paddleLeftest)
all_sprites_list.add(paddleLeft)
all_sprites_list.add(paddleCenter)
all_sprites_list.add(paddleRight)
all_sprites_list.add(paddleRightest)
all_sprites_list.add(ball)

# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True
quantumFlag = False
frames = 0

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

while carryOn:
    #-------------Main Event Loop----------
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  #Pressing the x Key will quit the game
                carryOn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddleLeftest.moveLeft(5, 0)
        paddleLeft.moveLeft(5, 20)
        paddleCenter.moveLeft(5, 40)
        paddleRight.moveLeft(5, 60)
        paddleRightest.moveLeft(5, 80)

    if keys[pygame.K_RIGHT]:
        paddleLeftest.moveRight(5, 0)
        paddleLeft.moveRight(5, 20)
        paddleCenter.moveRight(5, 40)
        paddleRight.moveRight(5, 60)
        paddleRightest.moveRight(5, 80)

    if keys[pygame.K_SPACE]:
        if not quantumFlag:
            quantumFlag = True
            (dx, dy) = ball.velocity
            directon = Vec2(dx, -dy)
            myArc = Arc(ball.position, directon, 1.5)
            myWavefront = Wavefront(myArc)

            #dt = pygame.time.Clock().get_time()

            #myArc.next(dt)
            #myWavefront.next(dt, allEndPoints)

            ball.kill()
        else:
            #quantumFlag = False
            pass

    all_sprites_list.update()
    frames += 1

    #Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x >= 790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y < 40:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y > 590:
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        if lives == 0:
            #Display Game Over Message for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, white)
            screen.blit(text, (250, 300))
            pygame.display.flip()
            pygame.time.wait(3000)

            #Stop the Game
            carryOn = False

    #Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddleLeftest):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.velocity[1] = -0.8 * ball.velocity[1]
        ball.velocity[0] = -7
    if pygame.sprite.collide_mask(ball, paddleLeft):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.velocity[1] = -ball.velocity[1]
        ball.velocity[0] = -3
    if pygame.sprite.collide_mask(ball, paddleCenter):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.velocity[1] = -1.25 * ball.velocity[1]
        ball.velocity[0] = 0
    if pygame.sprite.collide_mask(ball, paddleRight):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.velocity[1] = -ball.velocity[1]
        ball.velocity[0] = 3
    if pygame.sprite.collide_mask(ball, paddleRightest):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.velocity[1] = -0.8 * ball.velocity[1]
        ball.velocity[0] = 7

    #Check if there is the ball collides with any of bricks
    brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
    for brick in brick_collision_list:
        ball.velocity[1] = -ball.velocity[1]
        score += 1
        brick.kill()
        if len(all_bricks) == 0:
            #Display Level Complete Message for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, white)
            screen.blit(text, (200, 300))
            pygame.display.flip()
            pygame.time.wait(3000)

            #Stop the Game
            carryOn = False

    wall_collision_list = pygame.sprite.spritecollide(ball, all_walls, False)
    for wall in wall_collision_list:
        ball.velocity[1] = -ball.velocity[1]





    #-------------Drawing code----------
    screen.fill(darkblue)

    pygame.draw.line(screen, white, [0, 38], [800, 38], 2)

    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, white)
    screen.blit(text, (20, 10))
    text = font.render("Lives: " + str(lives), 1, white)
    screen.blit(text, (650, 10))

    all_sprites_list.draw(screen)

    if quantumFlag and (frames % 60) == 0:
        myWavefront.next(10, allEndPoints)

    if quantumFlag:
        myWavefront.render(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
