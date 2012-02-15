#!/usr/bin/env python
"""
tictactoe.py
Tim Carroll
A Simple tic tac toe game
"""
gameover = False
top = [" "," "," "]
mid = [" "," "," "]
bot = [" "," "," "]
board = [top,mid,bot]
player = 2
spaceLeft = 9
tie = False
             
#main loop
while gameover == False:

    #print board
    print"  0   1   2"
    print "0 %s | %s | %s"%(top[0],top[1],top[2])
    print"  --|---|--"
    print "1 %s | %s | %s"%(mid[0],mid[1],mid[2])
    print"  --|---|--"
    print "2 %s | %s | %s"%(bot[0],bot[1],bot[2])

    #switches turns
    player += 1
    if player > 2:
        player = 1
    print "palyer %i,"%player

    #input
    row = int(raw_input("choose row: "))
    column = int(raw_input("choose column: "))

    #if space is not filled, fill space with appropriate symbol
    if board[row][column] == " ":
        if player == 1:
            board[row][column] ="X"
        if player == 2:
            board[row][column] ="O"
        spaceLeft -= 1
    else:
        print"space is already filled"
        player -= 1

    print ""

    #having lists for verticle and diagonal checking might be inefficient
    #but I was interested to see how lists could reference other lists
    left = [top[0],mid[0],bot[0]]
    center = [top[1],mid[1],bot[1]]
    right = [top[2],mid[2],bot[2]]
    slash = [top[0],mid[1],bot[2]]
    backSlash = [top[2],mid[1],bot[0]]

    #checking win conditions
    if top == ["X","X","X"] or top == ["O","O","O"]:
        gameover = True
    elif mid == ["X","X","X"] or mid == ["O","O","O"]:
        gameover = True
    elif bot == ["X","X","X"] or bot == ["O","O","O"]:
        gameover = True
    elif left == ["X","X","X"] or left == ["O","O","O"]:
        gameover = True
    elif center == ["X","X","X"] or center == ["O","O","O"]:
        gameover = True
    elif right == ["X","X","X"] or right == ["O","O","O"]:
        gameover = True
    elif slash == ["X","X","X"] or slash == ["O","O","O"]:
        gameover = True
    elif backSlash == ["X","X","X"] or backSlash == ["O","O","O"]:
        gameover = True
    else:
        #checking for tie game
        if spaceLeft == 0:
            tie = True
            gameover = True


print ""        
print "FINAL RESULT:"    
print "  0   1   2"
print "0 %s | %s | %s"%(top[0],top[1],top[2])
print "  --|---|--"
print "1 %s | %s | %s"%(mid[0],mid[1],mid[2])
print "  --|---|--"
print "2 %s | %s | %s"%(bot[0],bot[1],bot[2])
print ""

#checks for tie to find out which endgame message to display
if tie == False:
    print "This Victory Strengthened The Soul Of Player",player #Soul Blade reference
else:
    print "Cat's Game"
print "GAMEOVER"
