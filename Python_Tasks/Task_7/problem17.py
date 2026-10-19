# Problem: Separate the Numbers
# HackerRank: https://www.hackerrank.com/challenges/separate-the-numbers/problem

import math
import os
import random
import re
import sys
def separateNumbers(s):
    for i in range(1, len(s)):
        first = s[:i]
        if first[0] == '0':
            break
        num = int(first)
        expected = first
        next_num = num + 1
        while len(expected) < len(s):
            expected += str(next_num)
            next_num += 1
        if expected == s:
            print("YES", num)
            return
    print("NO")
if __name__ == '__main__':
    q = int(input().strip())
    for _ in range(q):
        s = input().strip()
        separateNumbers(s)