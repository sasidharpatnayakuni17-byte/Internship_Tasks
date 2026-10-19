# Problem: Pangrams
# HackerRank: https://www.hackerrank.com/challenges/pangrams/problem

import math
import os
import random
import re
import sys
import string
def pangrams(s):
    letters = set(s.lower())
    if set(string.ascii_lowercase).issubset(letters):
        return "pangram"
    else:
        return "not pangram"
if __name__ == '__main__':
    s = input()
    result = pangrams(s)
    print(result)