#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    total = 0
    for i in range(len(s)):
        if i + m > len(s):
            print("Breaking")
            break
        tempChocolate = s[i:i+m]
        print(tempChocolate)
        sum = 0
        for a in tempChocolate:
            sum += a
        if sum == d:
            total += 1
    return total

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
