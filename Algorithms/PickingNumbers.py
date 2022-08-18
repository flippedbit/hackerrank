#!/bin/python3

import math
import os
import random
import re
import sys

# Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to 1.
#
# Example:
# a = [1,1,2,2,4,4,5,5,5]
# There are two subarrays meeting the criterion: [1,1,2,2] and [4,4,5,5,5]. The maximum length subarray is 5 elements.
#
# Sample Input 0:
# 6
# 4 6 5 3 3 1
# Sample Output 0:
# 3
# Sample Input 1:
# 6
# 1 2 2 3 1 2
# Sample Output 1:
# 5

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    # base case: array only has 1 element
    if len(a) == 1:
        return 1
    
    # base case: all elements are the same
    temp = list(set(a))
    if len(temp) == 1:
        return len(a)

    max = 0
    for i in range(len(a)):
        count = 1
        currentHighest = a[i]
        currentLowest = a[i]
        for j in range(len(a)):
            if i == j:
                pass
            else:
                if abs(currentHighest - a[j]) <=1 and abs(currentLowest - a[j]) <= 1:
                    count = count + 1
                    if a[j] > currentHighest:
                        currentHighest = a[j]
                    elif a[j] < currentLowest:
                        currentLowest = a[j]
                    else:
                        pass
                    
        if count > max:
            max = count

    return max

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
