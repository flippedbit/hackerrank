#!/bin/python3

import math
import os
import random
import re
import sys

# An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly steps steps, 
# for every step it was noted if it was an uphill, U, or a downhill, D step. Hikes always start and end at sea level,
# and each step up or down represents a 1 unit change in altitude. We define the following terms:
#     * A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
#     * A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
# Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.
#
# Example:
# steps = 8 path = [DDUUUUDD]
# The hiker first enters a valley  units deep. Then they climb out and up onto a mountain  units high. Finally, the hiker returns to sea level and ends the hike.
#
# Sample Input:
# 8
# UDDDUDUU
# Sample Output:
# 1


#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#
def countingValleys(steps, path):
    # Write your code here
    valleys = 0
    altitude = 0
    for step in path:
        originalAltitude = altitude
        # need to keep track of our current altitude
        if step == "D":
            altitude = altitude - 1
        elif step == "U":
            altitude = altitude + 1
        else:
            # just in case...
            pass
        # we really only care about when coming out of a valley
        # back to sea level
        if originalAltitude < 0 and altitude == 0:
            valleys = valleys + 1
    return valleys

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    #fptr.write(str(result) + '\n')

    #fptr.close()
    print(result)