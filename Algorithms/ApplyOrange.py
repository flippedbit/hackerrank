#!/bin/python3

from cmath import atan
from colorsys import TWO_THIRD
import math
import os
import random
import re
import sys
#from tkinter.tix import Tree

# Sam's house has an apple tree and an orange tree that yield an abundance of fruit.
# Using the information given below, determine the number of apples and orange that land on Sam's house.
# In the diagram below:
#     - The red region denotes the house, where s is the start point, and t is the endpoint. The apple tree
#       is to the left of the house, and the orange tree is to its right.
#     - Assume the trees are located on a single point, where the apple tree is at a point a, and the orange
#       tree is at a point b.
#     - When a fruit falls from its tree, it lands d units of distance from its tree of origin along the x-axis.
#       * A negative value of d means the fruit fell d unites to the tree's left, and a positive value of d means
#         if falls d units to the tree's right. *
# Given the value of d for m apples and n oranges, determine how many apples and oranges will fall on Sam's house
# (i.e., in the inclusive range [s,t])
# For example, Sam's house is between s = 7 and t = 10. The apple tree is located at a = 4 and the orange tree
# at b = 12. There are m = 3 apples and n = 3 oranges. Apples are thrown apples = [2,3,-4] units distance from a,
# and oranges = [3,-2,-4] units distance. Adding each apple distance to the position of the tree, they land at
# [4 + 2, 4 + 3, 4 + -4] = [6,7,0]. Oranges land at [12 + 3, 12 + -2, 12 + -4] = [15,10,8]. One apple and two
# oranges land in the inclusive range 7 - 10 so we print
# 1
# 2
#
# Sample Input:
# 7 11
# 5 15
# 3 2
# -2 2 1
# 5 -6
# Sample Output:
# 1
# 1

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s = starting point of Sam's house location
#  2. INTEGER t = ending location of Sam's house location
#  3. INTEGER a = location of theApple tree
#  4. INTEGER b = location of the Orange tree
#  5. INTEGER_ARRAY apples = distances at which each apple falls from the tree
#  6. INTEGER_ARRAY oranges = distances at which each orange falls from the tree
#
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    count = 0
    for i in apples:
        if (i + a >= s) and (i + a <= t):
            count = count + 1
    print(count)
    count = 0
    for i in oranges:
        if (i + b >= s) and (i + b <= t):
            count = count + 1
    print(count)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
