#!/bin/python3

import math
import os
import random
import re
import sys

def isLeapYear(year):
    if year < 1919:
        if year % 4 == 0:
            return True
    if year % 400 == 0:
        return True
    if (year % 4 == 0) and not (year % 100 == 0):
        return True
    return False

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    if year == 1918:
        months[1] = 15
    elif isLeapYear(year):
        months[1] = 29
    total = 0
    print(months[1])
    for i in months[:8]:
        total += i
    dd = 256 - total
    return ("%.2d.09.%d" % (dd, year))

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)
    print(result)

    #fptr.write(result + '\n')

    #fptr.close()
