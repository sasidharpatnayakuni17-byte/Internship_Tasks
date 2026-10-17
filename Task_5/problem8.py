# Problem: Set .add()
# HackerRank: https://www.hackerrank.com/challenges/py-set-add/problem

num = int(input())
countries = set()
for i in range(num):
    country = input()
    countries.add(country)
print(len(countries))