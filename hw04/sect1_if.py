#!/usr/bin/env python
from hwtools import *

print "Section 1:  If Statements"
print "-----------------------------"

# 1.  Is n even or odd?
# 2. If n is odd, double it  
n = raw_input("Enter a number: ")
n = int(n)
if n%2 == 0:
    print "1. number is even"
    print "2.", n
else:
    print "1. number is odd"
    print "2.", n*2


# 3. If n is evenly divisible by 3, add four
if n%3 == 0:
    print "3.", n+4
else:
    print "3.", n

# 4. What is grade's letter value (eg. 90-100)
grade = raw_input("Enter a grade [0-100]: ")
grade = int(grade)
letter = 'F'
if grade > 90:
    letter = 'A'
elif grade > 80:
    letter = 'B'
elif grade > 70:
    letter = 'C'
elif grade > 60:
    letter = 'D'
print "4.", letter

