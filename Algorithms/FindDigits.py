#!/bin/python3

import math
import os
import random
import re
import sys

# An integer d is a divisor of an integer n if the remainder of n / d = 0.
# Given an integer, for each digit that makes up the integer determine whether it is a divisor.
# Count the number of divisors occurring within the integer.
#
# Example:
# n = 124
# Check whether 1, 2 and 4 are divisors of 124. All 3 numbers divide evenly into 124 so return 3.
# n = 111
# Check whether 1, 1 and 1 are divisors of 111. All 3 numbers divide evenly into 111 so return 3.
# n = 10
# Check whether 1 and 0 are divisors of 10. 1 is, but 0 is not. Return 1.
#
# Sample Input:
# 2
# 12
# 1012
# Sample Output:
# 2
# 3

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # Write your code here
    # count = 0
    # nStr = str(n)
    # nList = [*nStr]
    # for digit in nList:
    #     if int(digit) == 0:
    #         continue
    #     if n % int(digit) == 0:
    #         count = count + 1
    # return count
    divisors = [d for d in [*str(n)] if int(d) != 0 and n % int(d) == 0]
    return len(divisors)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)
        print(result)
        # fptr.write(str(result) + '\n')

    # fptr.close()
