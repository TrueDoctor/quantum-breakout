import pygame
import math
from pygame.math import Vector2 as Vec2
import colors
import random

h = 1


def drawArc(screen, center, direction, theta):
    (dx, dy) = direction
    direction = Vec2(dx, -dy)
    (length, myAngle) = direction.as_polar()
    #(dx, dy) = direction
    myAngle = myAngle / 360 * 2 * math.pi
    (cx, cy) = center
    #length = math.sqrt(dx**2 + dy**2)
    rect = [cx - length, cy - length, 2 * length, 2 * length]

    #myAngle = math.copysign(angle(direction, (1, 0)), dy)

    pygame.draw.arc(screen, colors.white, rect, myAngle - theta / 2,
                    myAngle + theta / 2, 2)


class Arc:
    def __init__(self, center, direction, arc_length):
        self.center = center
        self.direction = direction
        self.arc_length = arc_length

    def render(self, screen):
        drawArc(screen, self.center, self.direction, self.arc_length)

    def random_direction(self):
        (dx, dy) = self.direction
        direction = Vec2(dx, dy)
        (length, myAngle) = direction.as_polar()
        theta = random.randrange(-100, 100) / 100 * self.arc_length / (2* math.pi) * 360
        theta = theta + myAngle
        self.direction.from_polar((length, theta))

    def next(self, dt):
        length = self.direction.magnitude()
        new_length = length * self.arc_length + dt
        center_offset = self.direction.normalize() * -((new_length - dt) - length)
        new_direction = self.direction * ((new_length) / length)
        new_center = self.center + (self.direction - new_direction) + new_direction.normalize() * dt

        new_arc_length = self.arc_length / ((new_length / length) **0.1)
        new_arc = Arc(new_center, new_direction, new_arc_length)

        return new_arc


class Beam:
    def __init__(self, arc):
        self.arcs = [arc]
        self.dead = False

    def next(self, dt, lines):
        if not self.dead:
            self.arcs.append(self.arcs[-1].next(dt))
        return [self]

    def render(self, screen):
        for arc in self.arcs:
            arc.render(screen)


class Wavefront:
    def __init__(self, arc):
        self.beams = [Beam(arc)]

    def next(self, dt, lines):
        new_beams = []
        for beam in self.beams:
            new_beams.extend(beam.next(dt, lines))

    def render(self, screen):
        for beam in self.beams:
            beam.render(screen)
