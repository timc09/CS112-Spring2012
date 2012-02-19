#!/usr/bin/env python
"""
Binary Search

This was supposed to be a binary search algorithm but it isn't working...
I used the Iterative implementation from here:
    http://en.wikipedia.org/wiki/Binary_search_algorithm
"""
from hwtools import input_nums

nums = input_nums()
nums = sorted(nums)
print nums
print "I have sorted your numbers"
x = int (raw_input("Which number should I find: "))
m = 0
M = len(nums)-1
while M >= m:
    md = (M + m) / 2
    if nums[md] == x:
        break
    elif x > nums[md]:
       m = m + 1
    else:
        M -= 1
if nums[md]== x:
    print "Found", x, "at", md
else:
    print "Could not find", x
