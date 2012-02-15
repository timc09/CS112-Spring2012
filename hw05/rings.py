#!/usr/bin/env python
#Tim Carroll

import pygame
from pygame.locals import *
import math

## COLORS
BLUE = 0, 133, 199
RED = 223, 0, 36
YELLOW = 244, 195, 0
GREEN = 0, 159, 61
BLACK = 0, 0, 0
WHITE = 255, 255, 255

THICKNESS = 20


## MAIN
pygame.init()
screen = pygame.display.set_mode((800, 388))
pygame.display.set_caption("Olympic Rings   [press ESC to quit]")

## Draw
screen.fill(WHITE)

#each ring is created by drawing an elipse inside a rect

blue_ring = pygame.Rect((0,0), (250,250))
pygame.draw.ellipse(screen, BLUE, blue_ring, THICKNESS)

red_ring = pygame.Rect((550,0), (250,250))
pygame.draw.ellipse(screen, RED, red_ring, THICKNESS)

black_ring = pygame.Rect((275,0), (250,250))
pygame.draw.ellipse(screen, BLACK, black_ring, THICKNESS)

yellow_ring = pygame.Rect((137.5,133), (250,250))
pygame.draw.ellipse(screen, YELLOW, yellow_ring, THICKNESS)
pygame.draw.arc(screen, YELLOW, yellow_ring,math.radians(115),math.radians(300), THICKNESS)

green_ring = pygame.Rect((412.5,133), (250,250))
pygame.draw.ellipse(screen, GREEN, green_ring, THICKNESS)

#each gap is created by drawing a short white arc with an inflated rect and increased thickness over the ellipse followed by a normal sized, appropriatly colored arc over that.

#blue gap
pygame.draw.arc(screen, WHITE, blue_ring.inflate(20,20) ,math.radians(-30),math.radians(20), THICKNESS+20)
pygame.draw.arc(screen, BLUE, blue_ring,math.radians(-32),math.radians(22), THICKNESS)

#yellow gaps
pygame.draw.arc(screen, WHITE, yellow_ring.inflate(20,20) ,math.radians(150),math.radians(190), THICKNESS+20)
pygame.draw.arc(screen, YELLOW, yellow_ring,math.radians(148),math.radians(192), THICKNESS)

pygame.draw.arc(screen, WHITE, yellow_ring.inflate(20,20) ,math.radians(50),math.radians(90), THICKNESS+20)
pygame.draw.arc(screen, YELLOW, yellow_ring,math.radians(48),math.radians(92), THICKNESS)

#black gap
pygame.draw.arc(screen, WHITE, black_ring.inflate(20,20) ,math.radians(-30),math.radians(20), THICKNESS+20)
pygame.draw.arc(screen, BLACK, black_ring,math.radians(-32),math.radians(22), THICKNESS)

pygame.draw.arc(screen, WHITE, black_ring.inflate(20,20) ,math.radians(-120),math.radians(-90), THICKNESS+20)
pygame.draw.arc(screen, BLACK, black_ring,math.radians(-122),math.radians(-88), THICKNESS)

#green gaps
pygame.draw.arc(screen, WHITE, green_ring.inflate(20,20) ,math.radians(150),math.radians(190), THICKNESS+20)
pygame.draw.arc(screen, GREEN, green_ring,math.radians(148),math.radians(192), THICKNESS)

pygame.draw.arc(screen, WHITE, green_ring.inflate(20,20) ,math.radians(50),math.radians(90), THICKNESS+20)
pygame.draw.arc(screen, GREEN, green_ring,math.radians(48),math.radians(92), THICKNESS)

#red gap
pygame.draw.arc(screen, WHITE, red_ring.inflate(20,20) ,math.radians(-120),math.radians(-90), THICKNESS+20)
pygame.draw.arc(screen, RED, red_ring,math.radians(-122),math.radians(-88), THICKNESS)

## Loop
clock = pygame.time.Clock()
done = False
while not done:
    event = pygame.event.poll()
    if event.type == QUIT:
        done = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        done = True

    pygame.display.flip()
    clock.tick(30)

print "ByeBye"
