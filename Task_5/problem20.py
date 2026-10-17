# Problem: Piling Up!
# HackerRank: https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque
def can_stack(blocks):
    blocks = deque(blocks)
    top = float('inf')
    while blocks:
        if blocks[0] >= blocks[-1]:
            cube = blocks.popleft()
        else:
            cube = blocks.pop()
        if cube > top:
            return "No"
        top = cube
    return "Yes"
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        blocks = list(map(int, input().split()))
        print(can_stack(blocks))