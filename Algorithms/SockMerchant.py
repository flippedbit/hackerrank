#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
#def sockMerchant(n, ar):
def sockMerchant(n, ar):
    numberPairs = 0
    uniqueSocks = list(set(ar))
    numOfSocks = {sock:ar.count(sock) for sock in uniqueSocks}
    for i in uniqueSocks:
        numberPairs += numOfSocks[i] / 2
    return numberPairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
