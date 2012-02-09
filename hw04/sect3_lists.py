#!/usr/bin/env python
from hwtools import *

print "Section 3:  Lists"
print "-----------------------------"

nums = input_nums()
# 1. "nums" is a list of numbers entered from the command line.  How many
#    numbers were entered?

print "1.", len(nums)

# 2.  Append 3 and 5 to nums
nums.extend([3,5])
print "2.", nums

# 3.  Remove the last element from nums
#this removes and returns the last value, but it's much nicer than del a.[#]
nums.pop()
print "3.", nums


# 4.  Set the 3rd element to 7
nums[3] = 7
print "4.", nums


# 5. [ADVANCED] Grab a new list of numbers and add it to the existing one
nums2 = input_nums()
print "5.", nums


# 6. [ADVANCED] Make a copy of this new giant list and delete the 2nd 
#    through 4th values

nums_copy = nums[:]
print nums_copy
del nums_copy[4]
del nums_copy[3]
del nums_copy[2]
print "6.", nums, nums_copy

# 7-9. [ADVANCED] Print the following:

print "7.", nums[0],nums[1],nums[2]    # first 3 elements
print "8.", nums[-1]    # last element
temp = [nums[2]]    
print "9.", temp    # a list of the second element
