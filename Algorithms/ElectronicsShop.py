#!/bin/python3

import os
import sys

# A person wants to determine the most expensive computer keyboard and USB drive that can be
# purchased with a given budget. Given price lists for keyboards and USB drives and a budget,
# find the cost to buy them. If it is not possible to buy both items, return -1.
#
# Example:
# b = 60
# keyboards = [40,50,60]
# drives = [5,8,12]
# The person can buy a 40 keyboard + 12 USB drive = 52, or a
# 50 keyboard + 8 USB drive = 58. Choose the latter as the more expensive option and return 58.
#
# Sample Input 0:
# 10 2 3
# 3 1
# 5 2 8
# Sample Output 0:
# 9
# Sample Input 1:
# 5 1 1
# 4
# 5
# Sample Output 1:
# -1

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    keyboards.sort(reverse=True)
    drives.sort(reverse=True)

    max = 0

    # base case: cheapest of both is more than budget
    if keyboards[-1] + drives[-1] > b:
        return -1
    
    for i in keyboards:
        for j in drives:
            if i + j <= b:
                if i + j > max:
                    max = i + j
    return max

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)
    print(moneySpent)
    #fptr.write(str(moneySpent) + '\n')

    #fptr.close()
