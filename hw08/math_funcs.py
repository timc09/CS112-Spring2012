#!/usr/bin/env python

import math

# Distance formula
#   calculate a function called "distance" to calculate the distance between two points.
#   http://www.purplemath.com/modules/distform.htm
#   ex: 
#      >>> distance((0,0), (3,4))
#      5

def distance(a, b):
    c = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
    return c

# ADVANCED
# Normalizing Vectors
#   normalize a vector of length N.  If given all zeros, just spit back the same vector
#   http://www.fundza.com/vectors/normalize/index.html

#   ex:
#     >>> normalize((1,1))
#     [0.70710678118654746, 0.70710678118654746]
#     >>> normalize([0,0,0])
#     [0,0,0]
#     >>> normalize([1,1,1,1])
#     [0.25, 0.25, 0.25, 0.25]

def normalize(vec):
    total = 0.0
    for i in vec:
        total += (i*i)
    if(total != 0):
        output = []
        length = math.sqrt(total)
        for j in vec:
            output.append(j/length)
    else:
        output = vec
    return output
