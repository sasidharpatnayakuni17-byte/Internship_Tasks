# Problem: Find the Runner-Up Score!
# HackerRank:  https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

num = int(input())
scores = list(map(int, input().split()))
unique_scores = list(set(scores))
unique_scores.sort()
print(unique_scores[-2])