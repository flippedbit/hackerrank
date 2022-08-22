#!/bin/python3

import math
import os
import random
import re
import sys

# When a contiguous block of text is selected in a PDF viewer, the selection is highlighted
# with a blue rectangle. In this PDF viewer, each word is highlighted independently. For example:
# There is a list of  character heights aligned by index to their letters. For example, 'a' is at
# index 0 and 'z' is at index 25. There will also be a string. Using the letter heights given,
# determine the area of the rectangle highlight in mm^2 assuming all letters are 1mm wide.
#
# Example:
# h = [1,3,1,3,1,4,1,3,2,5,5,5,5,1,1,5,5,1,5,2,5,5,5,5,5,5]
# word = ' torn'
# The heights are t = 2, o = 1, r = 1, n = 1. The tallest letter is 2 high and there are 4 letters.
# The highlighted area will be 2 * 4 = 8mm^2 so the answer is 8.
#
# Sample Input 0:
# 1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
# abc
# Sample Output 0:
# 9
# Sample Input 1:
# 1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7
# zaba
# Sample Output 1:
# 28

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    import string
    alphabetHeights = {string.ascii_lowercase[i]:h[i] for i in range(len(h))}
    wordHeight = [alphabetHeights[i] for i in word]
    wordHeight.sort()
    return wordHeight[-1] * len(word)
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
