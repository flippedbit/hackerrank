#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    minRecord = scores[0]
    maxRecord = scores[0]
    numMin, numMax = 0, 0
    for game in scores:
        if game < minRecord:
            minRecord = game
            numMin += 1
        if game > maxRecord:
            maxRecord = game
            numMax += 1
    return [numMax, numMin]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    #print(result)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
