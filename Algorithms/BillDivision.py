#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    n = bill[:k]+bill[k+1:]
    t = 0
    for i in n:
        t += i
    s = t / 2
    if s == b:
        return "Bon Appetit"
    else:
        return int(b - s)

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    print(bonAppetit(bill, k, b))

