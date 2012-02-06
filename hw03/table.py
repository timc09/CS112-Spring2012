#!/usr/bin/env python
"""
table.py
Tim Carroll
CS112 Homework 3:   decimal/hex/binary conversion table

displays a table which shows user input as decimal, hexidecimal and binary.
"""
def table():
    #function for drawing a table
    in1 = int(raw_input("Enter a number less than 256: "))
    if (in1 < 256):#if input is less than 256
        nums.append(in1)#add input to the list
        print""#an extra space
        print"|%10s|%10s|%11s|"%("DECIMAL","HEX","BINARY")#the heading for the table
        print"|"+"----------|"*2 + "-----------|"#top of the table
        for num in nums:#for each item in the list
            #print the float, hex and bin versions of num
            print"|%10f|%10s|%11s|" %(float(num), hex(num), bin(num))
        print"|"+"----------|"*2 + "-----------|"#bottom of the table
    else:#if input is >= 256
        print"Too big."
        print"Try again."
        table()#relaunch table function


nums = []#initializes list
for i in range(5):table()#runs table 5 times

