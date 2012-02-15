#!/usr/bin/env python
"""
nims.py
Tim Carroll
A simple competitive game where players take stones from stone piles.
"""
def main():
    #initializing variables
    pile = 40
    max = 5
    min = 1
    current_player = 1

    #main loop
    while pile > 0:
        print "Number of stones in the pile: %i" %pile
        print "Max number of stones per turn: %i" %max
        num = int(raw_input("%i stones left. Player %i [%i-%i]: " %(pile, current_player, min, max)))
        if(error_check(num, max, min)):#error checking
            if pile >= num:
                pile = pile - num
                current_player = switch(current_player)#switch player
            else:
                print "Not enough stones"
        else:
            print "Invalid number of stones"
    print "Player %i wins!!!"%current_player
            

def error_check(input, max, min):
    #returns true if input is between min and max
    if (input >= min and input <= max):
        return True
    else:
        return False

def switch(player):
    #toggles between 1 and 2
    player += 1
    if player > 2:
        player = 1
    return player

main()
