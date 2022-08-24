#!/bin/python3

import math
import os
import random
import re
import sys

# A child is playing a cloud hopping game. In this game, there are sequentially numbered clouds
# that can be thunderheads or cumulus clouds. The character must jump from cloud to cloud until
# it reaches the start again.
#
# There is an array of clouds, c and an energy level e = 100. The character starts from c[0] and
# uses 1 unit of energy to make a jump of size k to cloud c[(i + k) % n]. If it lands on a thundercloud,
# c[i] = 1 , its energy (e) decreases by 2 additional units. The game ends when the character lands
# back on cloud e.
#
# Given the values of n, k, and the configuration of the clouds as an array c, determine the final
# value of e after the game ends.
#
# Example:
# c = [0,0,1,0]
# k = 2
# The indices of the path are 0 -> 2 -> 0. The energy level reduces by 1 for each jump to 98.
# The character landed on one thunderhead at an additional cost of 2 energy units. The final energy level is 96.
#
# Sample Input:
# 8 2
# 0 0 1 0 0 1 1 0
# Sample Output:
# 92

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    cloud = 0
    e = 100
    # keep jumping until we get back to start
    while True:
        # figure out how far we jump and if it circles back to the start of array
        cloud = (cloud + k) % len(c)
        e = e - 1
        if c[cloud] == 1:
            e = e - 2
        # if we go back to the beginning the stop
        if cloud == 0:
            break
    return e

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
