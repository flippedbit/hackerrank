#!/bin/python

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    #zero = arr.count(0)
    #positive = [num for num in arr if (num != 0) and (num > 0)]
    #negative = [num for num in arr if (num != 0) and (num < 0)]
    zero, positive, negative = 0, 0, 0
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        elif i == 0:
            zero += 1
    print("%6f" % (float(positive / len(arr))))
    print("%6f" % (float(negative / len(arr))))
    print("%6f" % (float(zero / len(arr))))

if __name__ == '__main__':
    # 8
    n = int(input())
    # 1 2 3 -1 -2 -3 0 0
    arr = list(map(int, input().rstrip().split()))
    # expected output
    # 0.375000
    # 0.375000
    # 0.250000
    plusMinus(arr)
