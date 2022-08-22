#!/bin/python3

import math
import os
import random
import re
import sys

# A video player plays a game in which the character competes in a hurdle race. Hurdles are of varying heights,
# and the characters have a maximum height they can jump. There is a magic potion they can take that will
# increase their maximum jump height by 1 unit for each dose. How many doses of the potion must the character
# take to be able to jump all of the hurdles. If the character can already clear all of the hurdles, return 0.
#
# Example:
# height = [1, 2, 3, 3, 2]
# k = 1
# The character can jump 1 unit high initially and must take 3 - 1 = 2 doses of potion to be able to jump all of the hurdles.
#
# Sample Input 0:
# 5 4
# 1 6 3 5 2
# Sample Output 0:
# 2
# Sample Input 1:
# 5 7
# 2 5 4 5 2
# Sample Output 1:
# 0

#
# Complete the 'hurdleRace' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY height
#

def hurdleRace(k, height):
    # Write your code here
    height.sort()
    if height[-1] < k:
        return 0
    else:
        return height[-1] - k

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
