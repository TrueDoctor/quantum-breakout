import pygame
import math
from pygame.math import Vector2 as Vec2
import colors

h = 1


def angle(vector1, vector2):
    x1, y1 = vector1
    x2, y2 = vector2
    inner_product = x1 * x2 + y1 * y2
    len1 = math.hypot(x1, y1)
    len2 = math.hypot(x2, y2)
    return math.acos(inner_product / (len1 * len2))


def drawArc(screen, center, direction, theta):
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

    def next(self, dt):
        length = self.direction.magnitude()
        new_length = length * self.arc_length + dt
        center_offset = self.direction.normalize() * -((new_length - dt) - length)
        new_direction = self.direction * ((new_length) / length)
        new_center = self.center #- new_direction + self.direction

        new_arc_length = self.arc_length
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
