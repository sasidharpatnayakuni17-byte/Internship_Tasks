# Problem: Validating the Phone Number
# HackerRank: https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re
if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        number = input()
        if re.fullmatch(r'[7-9][0-9]{9}', number):
            print("YES")
        else:
            print("NO")