#!/bin/python3

import math
import os
import random
import re
import sys

# Two cats and a mouse are at various positions on a line. You will be given their starting positions.
# Your task is to determine which cat will reach the mouse first, assuming the mouse does not move
# and the cats travel at equal speed. If the cats arrive at the same time, the mouse will be allowed
# to move and it will escape while they fight.
#
# You are given  queries in the form of x, y, and z representing the respective positions for 
# cats A and A, and for mouse C. Complete the function  to return the appropriate answer to 
# each query, which will be printed on a new line.
#
# If cat A catches the mouse first, print Cat A.
# If cat B catches the mouse first, print Cat B.
# If both cats reach the mouse at the same time, print Mouse C as the two cats fight and mouse escapes.
#
# Example:
# x = 2
# y = 5
# z = 4
#
# The cats are at positions 2 (Cat A) and 5 (Cat B), and the mouse is at position 4.
# Cat B, at position  will arrive first since it is only  unit away while the other is  units away.
# Return 'Cat B'.
#
# Sample Input:
# 2
# 1 2 3
# 1 3 2
# Sample Output:
# Cat B
# Mouse C


# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    if abs(x - z) < abs(y - z):
        return "Cat A"
    elif abs(x - z) > abs(y - z):
        return "Cat B"
    else:
        return "Mouse C"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        # fptr.write(result + '\n')
        print(result)

    # fptr.close()
