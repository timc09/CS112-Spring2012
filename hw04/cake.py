#!/usr/bin/env python
'''
cake.py
Tim Carroll
'''
slices = 3
answer = ""#initialize answer
dead = False
while dead == False:
    answer = raw_input("Cake or Death?")
    if answer == "cake" or answer == "Cake":
        if slices > 0:#give out slices if there are slices left
            print "Here is your cake."
            slices -= 1
        else:
            print "We have no more cake."
            print"We had no Idea there would be such a rush."
    elif answer == "death" or answer == "Death":
        #if answer is "death", break out of loop
        dead = True
    
print"You were torn limb from limb by a band of excitable four year olds"
print"who were told you were full of candy."
