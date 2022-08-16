#!/bin/python3

import math
import os
import random
import re
import sys

# A teach asks the class to open their books to a page number.
# A student can either start turning pages from the front of the book or from the back of the book.
# They always turn pages one at a time.
# When they open the book, page 1 is always on the right side
# When they flip page 1, they see pages 2 and 3.
# Each page except the last page will always be printed on both sides.
# The last page may only be printed on the front, given the length of the book.
# If the book is n pages long, and a student wants to turn to page p, what is the minimum number of pages to turn?
# They can start at the beginning or the end of the book.
# Given n and p, find and print the minimum number of pages that must be turned in order to arrive at page p.
#
# Example:
# n = 5
# p = 3
# If the student wants to get to page 3, they open the book to page 1, flip 1 page and they are on the correct page.
# If they open the book at the last page, page 5, they turn 1 page and are at the correct pate. Return 1.
#
# Sample Input 0:
# 6
# 2
# Sample Output:
# 1
#
# Sample Input 1:
# 5
# 4
# Sample Output 1:
# 0

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    #turnCount = 0

    # base cases:
    # desired page is first page
    # desired page is last page
    if p == 1 or p == n:
        #return turnCount
        return 0

    fromFront = (p / 2)
    fromBack = (n - p) / 2
    print(f"{fromFront=}{fromBack=}")
    if fromFront > fromBack:
        if n % 2 == 0:
            if n - p == 1:
                return 1
        print(f"{fromBack=}")
        return int(fromBack)
    else:
        print(f"{fromFront=}")
        return int(fromFront)

    # WRONG
    #
    # check if book length is even or odd
    # will determine if last page is on front or back
    # if n % 2 != 0:
    #     n = n - 1
    # check if desired page is closer to front or back of book
    # if n / 2 < p:
    #     for i in range(n, p, -2):
    #         turnCount = turnCount + 1
    # elif n / 2 == p:
    #     # if desired page is in the middle of the book
    #     # if odd number of pages then start from back
    #     # if even number start from front
    #     if n % 2 == 0:
    #         for i in range(n, p, 2):
    #             turnCount = turnCount +1
    #     else:
    #         for i in range(n, p, -2):
    #             turnCount = turnCount + 1
    # else:
    #     for i in range(0, p, 2):
    #         turnCount = turnCount + 1
    # return turnCount
    #
    # WRONG



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    #fptr.write(str(result) + '\n')

    #fptr.close()
    print(result)