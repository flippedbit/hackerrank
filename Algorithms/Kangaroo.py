#!/bin/python

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if ((x1 > x2) and (v1 > v2)) or ((x1 < x2) and (v1 < v2)):
        return "NO"
    hops = 0
    lead = {x1:{"speed":v1,"place":x1}, x2:{"speed":v2,"place":x2}}
    while lead[min(lead.keys())]["place"] < lead[max(lead.keys())]["place"] and hops < 10000:
        print(lead)
        hops += 1
        lead[x1]["place"] += lead[x1]["speed"]
        lead[x2]["place"] += lead[x2]["speed"]
        if lead[x1]["place"] == lead[x2]["place"]:
            return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = raw_input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
