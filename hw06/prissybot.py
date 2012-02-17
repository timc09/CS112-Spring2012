#!/usr/bin/env python
"""
prissybot.py
Tim Carroll
CS112 Homework 3:   PrissyBot

Prissy bot, the rude chat bot, is just mean!  It does not listen, asks obnoxious questions, and says anything it likes.
"""

name = raw_input("Enter your name: ")   #stores raw input in name
print "PrissyBot: Hello there, %s." % name
in1 = raw_input("%s: "%name)
print "PrissyBot: You mean, \"%s, sir!\""%in1   #using escape character for ""
in1 = raw_input("%s: "%name)
print "PrissyBot: That's right, you dolt."  #insult 1
print "PrissyBot: now, %s, I will amaze your tiny mind."%name   #insult 2
print "PrissyBot: what do you have to say to that?"
in1 = raw_input("%s: "%name)
print "PrissyBot: Pitiful."     #insult 3
print "PrissyBot: I will begin with sums."
in1 = raw_input("Enter an integer: ")
in2 = raw_input("Enter a 2nd integer: ")
print "%i + %i = %i"%(int(in1),int(in2),int(in1)+int(in2))   #math problem 1
print "PrissyBot: Now division."
in1 = raw_input("Enter an integer: ")
in2 = raw_input("Enter a 2nd integer: ")
#math problem 2 using ints
print "%i / %i = %i"%(int(in1),int(in2),int(in1)/int(in2))
#checks to see if the math apeared strange due to integer math
if float(in1)%float(in2)!= 0:
    print"Ha! Integer math."    #if so, prissybot comments on it
print "To be more acurate:"
print "%f / %f = %f"%(float(in1),float(in2),float(in1)/float(in2))#math problem 3 using floats
print "That's enough for now..."
print "idiot."      #Zing!
print "Good bye, %s." %name



    

