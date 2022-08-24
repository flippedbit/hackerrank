#!/bin/python3

import math
import os
import random
import re
import sys

# John Watson knows of an operation called a right circular rotation on an array of integers.
# One rotation operation moves the last array element to the first position and shifts all
# remaining elements right one. To test Sherlock's abilities, Watson provides Sherlock with
# an array of integers. Sherlock is to perform the rotation operation a number of times then
# determine the value of the element at a given position.
#
# For each array, perform a number of right circular rotations and return the values of the
# elements at the given indices.
#
# Example:
# a = [3,4,5]
# k = 2
# queries = [1,2]
#
# Here k is the number of rotations on a, and queries holds the list of indices to report. First
# we perform the two rotations: [3,4,5] -> [5,3,4] -> [4,5,3]
# Now return the values from the zero-based indices 1 and 2 as indicated in the queries array.
# a[1] = 5
# a[2] = 3
#
# Sample Input:
# 3 2 3
# 1 2 3
# 0
# 1
# 2
# Sample Output:
# 2
# 3
# 1

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#

def circularArrayRotation(a, k, queries):
    # Write your code here

    # TAKES TOO LONG
    #
    # for rotation in range(k):
    #     tmp = [a[-1]]
    #     for i in range(len(a)-1):
    #         tmp.append(a[i])
    #     a = tmp
    # answers = []
    # for i in queries:
    #     answers.append(a[i])
    # return answers
    #
    # TAKES TOO LONG
    
    # THIS IS WRONG TOO
    # print(f"Start: {a=} {k=} {queries=}")
    tmp = [0 for a in range(len(a))]
    for i in range(len(a)):
        location = (i + k) % len(a)
        print(f"{location=} {a[i]=}")
        tmp[location] = a[i]
        print(f"{tmp=}")
    
    return [tmp[i] for i in queries]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)
    print('\n'.join(map(str, result)))
    print('\n')
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
