#!/bin/python3

import math
import os
import random
import re
import sys

# The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by 1 meter.
# A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring. How tall will the tree be after n growth cycles?
# For example, if the number of growth cycles is n = 5, the calculations are as follows:
# Period Height
# 0       1
# 1       2
# 2       3
# 3       6
# 4       7
# 5       14
#
# Sample Input:
# 3
# 0
# 1
# 4
# Sample Ouput:
# 1
# 2
# 7

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # Write your code here
    height = 1
    if n == 0:
        return 1
    while n > 0:
        # spring
        height = height * 2
        n = n - 1
        if n == 0:
            break
        # summer
        height = height + 1
        n = n - 1
    return height

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)
        print(result)
    #     fptr.write(str(result) + '\n')

    # fptr.close()
