#!/usr/bin/env python3

import pygame
import sys
import math
from math import pi

from paddle import Paddle
from ball import Ball
from brick import Brick

pygame.init()

# Define some colors
white = (255,255,255)
darkblue = (12,20,50)
lightblue = (0,176,240)
paddle1 = (0,0,255)
paddle2 = (175,0,255)
paddle3 = (255,0,255)
paddle4 = (255,0,175)
paddle5 = (255,0,0)
red = (255,0,0)
orange = (255,100,0)
yellow = (255,255,0)
black = (0,0,0)

score = 0
lives = 3



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
ball = Ball(white,10,10)
ball.rect.x = 345
ball.rect.y = 195

all_bricks = pygame.sprite.Group()
for i in range(7):
    brick = Brick(red,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(orange,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(yellow,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)
 
# Add the paddle to the list of sprites
all_sprites_list.add(paddleLeftest)
all_sprites_list.add(paddleLeft)
all_sprites_list.add(paddleCenter)
all_sprites_list.add(paddleRight)
all_sprites_list.add(paddleRightest)
all_sprites_list.add(ball)


# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()


while carryOn:
    #-------------Main Event Loop----------
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Pressing the x Key will quit the game
                     carryOn=False

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

    all_sprites_list.update()

    #Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x>=790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y<40:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y>590:
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        if lives == 0:
            #Display Game Over Message for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, WHITE)
            screen.blit(text, (250,300))
            pygame.display.flip()
            pygame.time.wait(3000)
 
            #Stop the Game
            carryOn=False


    #Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddleLeftest):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.velocity[1] = -0.8*ball.velocity[1]
        ball.velocity[0] = -7
    if pygame.sprite.collide_mask(ball, paddleLeft):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.velocity[1] = -ball.velocity[1]
        ball.velocity[0] = -3
    if pygame.sprite.collide_mask(ball, paddleCenter):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.velocity[1] = -1.1*ball.velocity[1]
        ball.velocity[0] = 0
    if pygame.sprite.collide_mask(ball, paddleRight):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.velocity[1] = -ball.velocity[1]
        ball.velocity[0] = 3
    if pygame.sprite.collide_mask(ball, paddleRightest):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.velocity[1] = -0.8*ball.velocity[1]
        ball.velocity[0] = 7

    #Check if there is the ball collides with any of bricks
    brick_collision_list = pygame.sprite.spritecollide(ball,all_bricks,False)
    for brick in brick_collision_list:
      ball.velocity[1] = -ball.velocity[1]
      score += 1
      brick.kill()
      if len(all_bricks)==0:
           #Display Level Complete Message for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, WHITE)
            screen.blit(text, (200,300))
            pygame.display.flip()
            pygame.time.wait(3000)
 
            #Stop the Game
            carryOn=False



    #-------------Drawing code----------
    screen.fill(darkblue)
    pygame.draw.line(screen, white, [0,38], [800,38], 2)


    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, white)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives), 1, white)
    screen.blit(text, (650,10))

    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)


pygame.quit()

