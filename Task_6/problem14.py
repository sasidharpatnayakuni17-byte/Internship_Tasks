# Problem: Set .intersection() Operation
# HackerRank:  https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

if __name__ == '__main__':
    n = int(input())
    english = set(map(int, input().split()))
    b = int(input())
    french = set(map(int, input().split()))
    print(len(english.intersection(french)))
