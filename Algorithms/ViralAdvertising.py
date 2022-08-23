#!/bin/python3

import math
import os
import random
import re
import sys

# HackerLand Enterprise is adopting a new viral advertising strategy.
# When they launch a new product, they advertise it to exactly 5 people
# on social media.
#
# On the first day, half of those  people (i.e., floor(5/2) = 2) like
# the advertisement and each shares it with 3 of their friends. At the
# beginning of the second day, floor(5/2) x 3 = 2 x 3 = 6 people receive
# the advertisement.
#
# Each day, floor(recipients/2) of the recipients like the advertisement
# and will share it with 3 friends on the following day. Assuming nobody
# receives the advertisement twice, determine how many people have liked
# the ad by the end of a given day, beginning with launch day as day 1.
#
# Sample Input:
# 3
# Sample Output:
# 9

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    shared = 5
    likes = 0
    cumulative = 0
    for day in range(1, n+1):
        likes = int(shared / 2)
        cumulative = cumulative + likes
        shared = likes * 3
        # print(f"{day=} {shared=} {likes=} {cumulative=}")
    return cumulative

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
