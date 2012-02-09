#!/usr/bin/env python
from hwtools import *

print "Section 4:  For Loops"
print "-----------------------------"

nums = input_nums()
# 1. What is the sum of all the numbers in nums?
total = 0
for i in nums:
    total += i
print "1.", total


# 2. Print every even number in nums
print "2. even numbers"

for i in nums:
    if i%2 == 0:
        print " ",i


# 3. Does nums only contain even numbers? 
only_even = False
total = 0
for i in nums:
    if i%2 == 0:
        total += 1
    if total == len(nums):
        only_even = True

print "3.",
if only_even:
    print "only even"
else:
    print "some odd"


# 4. Generate a list every odd number less than 100. Hint: use range()
odd_nums = []
for i in range(1,100,2):
    odd_nums.append(i)
print "4.",odd_nums


# 5. [ADVANCED]  Multiply each element in nums by its index
for i in range(len(nums)-1):
    nums[i] = nums[i]*nums[i+1]
print "5.", nums
