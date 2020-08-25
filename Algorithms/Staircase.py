#!/bin/python

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    a = '#'
    s = ' '
    for i in range(n):
        print("%s%s" % (s * (n - (i + 1)), a * (i + 1)))

if __name__ == '__main__':
    n = int(raw_input())

    staircase(n)
