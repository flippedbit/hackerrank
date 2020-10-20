#!/bin/python3

import math
import os
import random
import re
import sys
import operator

def counter(ar, x):
    c = 0
    for a in ar:
        if a == x:
            c += 1
    return c

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    # this took too long because it was running through the loop every time
    # one of the test cases had 125k entries in the array causing the
    # execution time to be very long
    # x = { k:counter(arr, k) for k in arr }
    x = {}
    for i in arr:
        if i in x:
            x[i] += 1
        else:
            x[i] = 1
    print(x)
    m = max(x.items(), key=operator.itemgetter(1))
    result = m[0]
    if counter(x.values(), m[1]) > 1:
        for k, v in x.items():
            if v == m[1]:
                if k < m[0]:
                    result = k
    return result

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
