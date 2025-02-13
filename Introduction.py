# Task
# Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

# Input Format
# A single line containing a positive integer, n.

# Output Format
# Print Weird if the number is weird. Otherwise, print Not Weird.

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if (n % 2 != 0):
        print("Weird")
    else:
        if n > 20:
            print("Not Weird")
        elif n > 5:
            print("Weird")
        elif n > 1:
            print("Not Weird")

# Task
# The provided code stub reads two integers, a and b, from STDIN.

# Add logic to print two lines. The first line should contain the result of integer division, a // b. The second line should contain the result of float division, a / b.

# No rounding or formatting is necessary.

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if b!=0:
        print(a//b)
        print(a/b)

# Task
# The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a*b)

# Task
# The provided code stub reads an integer, n, from STDIN. For all non-negative integers i < n, print i^2.

if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i**2)

# In the Gregorian calendar, three conditions are used to identify leap years:

# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.

#Task

#Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
#Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    
    return leap

year = int(input())
print(is_leap(year))