#!/usr/bin/env python
"""
ascii.py
Tim Carroll
CS112 Homework 3:   Ascii

prints an ascii lightning bolt using user input.
"""
c = raw_input("input character to make an ascii lightning bolt: ")
print""#puts a space between the input line and the picture
for i in range(17):#loops over each line and determines how many characters will be drawn
    if i > 11:#depending on the line, this changes how the charaters are spaced 
        print"    "+"%s"%c*(17-i)#uses '+' to seperate two parts of the print statement so one part can be repeated
    elif i>5:
        print"  "+"%s"%c*(17-i)
    else:
        print"%s"%c*(17-i) 



               
