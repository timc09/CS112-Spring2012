#!/usr/bin/env python
"""
fraction.py
Tim Carroll
CS112 Homework 3:   reduce a fraction

Reduces fration
"""
wholeNum = 0
temp = 0

numerator = int(raw_input("Enter a numerator: "))
denominator = int(raw_input("Enter a denominator: "))
if numerator > denominator and denominator != 0:
    origNum = numerator
    origDenom = denominator
    while numerator > denominator:
        numerator -= 1
        temp += 1
        if temp == denominator:
            temp = 0
            wholeNum += 1
    wholeNum += 1
    if temp == 0: print"%i/%i = %i"%(origNum, origDenom, wholeNum)
    else: print"%i/%i = %i %i/%i"%(origNum, origDenom, wholeNum, temp, denominator)
else: print"No reduction needed: %i/%i = %i/%i"%(numerator,denominator,numerator,denominator)
        
        
