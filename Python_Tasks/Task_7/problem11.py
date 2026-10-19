# Problem:  Two Strings
# HackerRank:

import math
import os
import random
import re
import sys
def twoStrings(s1, s2):
    if set(s1) & set(s2):
        return "YES"
    else:
        return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    p = int(input().strip())
    for _ in range(p):
        s1 = input().strip()
        s2 = input().strip()
        result = twoStrings(s1, s2)
        fptr.write(result + '\n')
    fptr.close()