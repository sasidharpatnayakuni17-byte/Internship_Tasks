# Problem: Weighted Uniform Strings
# HackerRank: https://www.hackerrank.com/challenges/weighted-uniform-string/problem

import math
import os
import random
import re
import sys
def weightedUniformStrings(s, queries):
    weights = set()
    previous_char = ''
    current_weight = 0
    for char in s:
        weight = ord(char) - ord('a') + 1
        if char == previous_char:
            current_weight += weight
        else:
            current_weight = weight
        weights.add(current_weight)
        previous_char = char
    result = []
    for query in queries:
        if query in weights:
            result.append("Yes")
        else:
            result.append("No")
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input().strip()
    queries_count = int(input().strip())
    queries = []
    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)
    result = weightedUniformStrings(s, queries)
    fptr.write('\n'.join(result))
    fptr.write('\n')
    fptr.close()