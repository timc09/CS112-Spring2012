#!/usr/bin/env python
"""
tron.py

The simple game of tron with two players.  Press the space bar to start the game.  Player 1 (red) is controlled with WSAD and player 2 (blue) is controlled with the arrow keys.  Once the game is over, press space to reset and then again to restart.  Escape quits the program.
"""

import pygame
from pygame import draw
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()


def game(screen, clock, scores):
    done = False
    screen_bounds = screen.get_rect()
    screen.fill((0,0,0))

    BLUE = (0,0,255)
    RED = (255,0,0)

    NORTH = (0, -10)
    SOUTH = (0, 10)
    EAST = (10, 0)
    WEST = (-10, 0)

    def move(pos, color, size):
        #draws line
        draw.rect(screen, color, (pos[0], pos[1], size, size))
        
    def changePos(pos, moves, direction):
        #returns pos * direction, appends it to moves.
        pos = (pos[0] + direction[0], pos[1]+direction[1])
        moves.append(pos)
        return pos

    def AI(pos, directon, moves):
        #clunky AI
        bMoves = blueMoves[:]
        rMoves = redMoves[:]
        pos = (pos[0] + EAST[0], pos[1]+EAST[1])
        if pos in bMoves or pos in rMoves or out_of_bounds(pos):
            pos = (pos[0] - EAST[0], pos[1]-EAST[1])
            pos = (pos[0] + NORTH[0], pos[1]+NORTH[1])
            if pos in bMoves or pos in rMoves or out_of_bounds(pos):
                pos = (pos[0] - NORTH[0], pos[1]-NORTH[1])
                pos = (pos[0] + WEST[0], pos[1]+WEST[1])
                if pos in bMoves or pos in rMoves or out_of_bounds(pos):
                    pos = (pos[0] - WEST[0], pos[1]-WEST[1])
                    pos = (pos[0] + SOUTH[0], pos[1]+SOUTH[1])
        moves.append(pos)
        return pos
        
        
    def out_of_bounds(pos):
        #checking for out of bounds
        hit = False
        if pos[0] >= 800 or pos[0] < 0:
            hit = True
        elif pos[1] >= 600 or pos[1] < 0:
            hit = True
        return hit
        

    def collision(bPos,rPos):
        bHit = False
        rHit = False
        bMoves = blueMoves[:]
        rMoves = redMoves[:]
        bMoves.pop()
        rMoves.pop()

        #checking for head on collision
        if bPos == rPos:
            bHit = True
            rHit = True

        #checking for wall collision
        if out_of_bounds(bPos):
            bHit = True
        if out_of_bounds(rPos):
            rHit = True

        #checking for line collision   
        elif bPos in bMoves or bPos in rMoves:
            bHit = True
        elif rPos in rMoves or rPos in bMoves:
            rHit = True

        #messy end game system
        if bHit or rHit:
            if bHit and not rHit:
                print '   RED WINS'
                print '--GAME OVER--'
                pygame.draw.circle(screen,(0,100,255),(bPos[0]+5,bPos[1]+5),20)
                scores[1] += 1
            elif rHit and not bHit:
                print '  BLUE WINS'
                print '--GAME OVER--'
                pygame.draw.circle(screen,(255,100,0),(rPos[0]+5,rPos[1]+5),20)
                scores[0] += 1
            else:
                print '     TIE'
                print '--GAME OVER--'
                pygame.draw.circle(screen,(255,255,255),(bPos[0]+5,bPos[1]+5),20)
            return True
        else:
            return False

    #starting positions
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
          
##            elif event.type == KEYDOWN and event.key == K_w:
##                bDir = NORTH
##            elif event.type == KEYDOWN and event.key == K_a:
##                bDir = WEST
##            elif event.type == KEYDOWN and event.key == K_s:
##                bDir = SOUTH
##            elif event.type == KEYDOWN and event.key == K_d:
##                bDir = EAST

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
        bPos = AI(blueMoves[-1], bDir, blueMoves)
        rPos = changePos(redMoves[-1], redMoves, rDir)
        if collision(bPos, rPos):
            done = True
            return scores


        #REFRESH   
        pygame.display.flip()
        clock.tick(20)

finished = False
font = pygame.font.Font(None, 40)
scores = [0,0]


while not finished:
    #INPUT
    for event in pygame.event.get():
        if event.type == QUIT:
            finished = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            finished = True
        elif event.type == KEYDOWN and event.key == K_SPACE:
            scores = game(screen, clock, scores)

    #UPDATE
        
    #DRAW
    text = font.render('Space to play', True, (255,255, 255))
    bScore = font.render(str(scores[0]), True, (0,0,200))
    rScore = font.render(str(scores[1]), True, (200,0,0))
    # Create a rectangle
    textRect = text.get_rect()

    # Center the rectangle
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery

    # Blit the text
    screen.blit(text, textRect)
    screen.blit(bScore, (40,40))
    screen.blit(rScore, (760,40))


    #REFRESH   
    pygame.display.flip()
    clock.tick(20)       
print "ByeBye"
