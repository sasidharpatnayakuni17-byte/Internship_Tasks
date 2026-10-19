# Problem:  Game of Thrones - I
# HackerRank: https://www.hackerrank.com/challenges/game-of-thrones/problem

import math
import os
import random
import re
import sys
from collections import Counter
def gameOfThrones(s):
    counts = Counter(s)
    odd_count = 0
    for count in counts.values():
        if count % 2 != 0:
            odd_count += 1
    if odd_count <= 1:
        return "YES"
    else:
        return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = gameOfThrones(s)
    fptr.write(result + '\n')
    fptr.close()