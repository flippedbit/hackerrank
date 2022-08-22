#!/bin/python3

import math
import os
import random
import re
import sys

# A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline,
# the professor decides to cancel class if fewer than some number of students are present when class starts.
# Arrival times go from on time (arrivalTime <= 0) to arrived late (arrivalTime > 0).
#
# Given the arrival time of each student and a threshhold number of attendees, determine if the class is cancelled.
# Example:
# n = 5
# k = 3
# a = [-2, -1, 0, 1, 2]
# The first 3 students arrived on. The last 2 were late. The threshold is 3 students, so class will go on. Return YES.
#
# Sample Input:
# 2
# 4 3
# -1 -3 4 2
# 4 2
# 0 -1 2 1
# Sample Output:
# YES
# NO

#
# Complete the 'angryProfessor' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a
#

def angryProfessor(k, a):
    # Write your code here
    late = [i for i in a if i > 0]
    if len(late) > (len(a) - k):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)
        print(result)
        # fptr.write(result + '\n')

    # fptr.close()
