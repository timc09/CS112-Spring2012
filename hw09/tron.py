#!/usr/bin/env python
"""
tron.py

The simple game of tron with two players.  Press the space bar to start the game.  Player 1 (red) is controlled with WSAD and player 2 (blue) is controlled with the arrow keys.  Once the game is over, press space to reset and then again to restart.  Escape quits the program.
"""

import pygame
from pygame import draw
from pygame.locals import *

BLUE = (0,0,255)
RED = (255,0,0)

NORTH = (0, -10)
SOUTH = (0, 10)
EAST = (10, 0)
WEST = (-10, 0)

redScore = 0
blueScore = 0


pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
done = False
screen_bounds = screen.get_rect()
screen.fill((0,0,0))

typeFace = pygame.font.Font(None, 40)


def move(pos, color, size):
    draw.rect(screen, color, (pos[0], pos[1], size, size))
    
def changePos(pos, moves, direction):
    pos = (pos[0] + direction[0], pos[1]+direction[1])
    moves.append(pos)
    return pos

def collision(bPos,rPos):
    bHit = False
    rHit = False
    bMoves = blueMoves[:]
    rMoves = redMoves[:]
    bMoves.pop()
    rMoves.pop()
    
    if bPos == rPos:
        bHit = True
        rHit = True
    #elif bPos[0] > 
    elif bPos in bMoves or bPos in rMoves:
        bHit = True
    elif rPos in rMoves or rPos in bMoves:
        rHit = True
    if bHit or rHit:
        if bHit and not rHit:
            print '   RED WINS'
            print '--GAME OVER--'
            redScore += 1
        elif rHit and not bHit:
            print '  BLUE WINS'
            print '--GAME OVER--'
            redScore += 1
        else:
            print '     TIE'
            print '--GAME OVER--'
        return True
    else:
        return False


bDir = EAST
rDir = WEST

blueMoves = [(200, 300)]
redMoves = [(600, 300)]


#GAME LOOP
while not done:
    #INPUT
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        
        elif event.type == KEYDOWN and event.key == K_w:
            bDir = NORTH
        elif event.type == KEYDOWN and event.key == K_a:
            bDir = WEST
        elif event.type == KEYDOWN and event.key == K_s:
            bDir = SOUTH
        elif event.type == KEYDOWN and event.key == K_d:
            bDir = EAST

        elif event.type == KEYDOWN and event.key == K_UP:
            rDir = NORTH
        elif event.type == KEYDOWN and event.key == K_LEFT:
            rDir = WEST
        elif event.type == KEYDOWN and event.key == K_DOWN:
            rDir = SOUTH
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            rDir = EAST


        

    #UPDATE
    bPos = blueMoves[-1]
    rPos = redMoves[-1]
    move(bPos, BLUE, 10)
    move(rPos, RED, 10)
    bPos = changePos(blueMoves[-1], blueMoves, bDir)
    rPos = changePos(redMoves[-1], redMoves, rDir)
    if collision(bPos, rPos):
        done = True


    #REFRESH   
    pygame.display.flip()
    clock.tick(20)
    
print "ByeBye"
