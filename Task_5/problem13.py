# Problem: Nested Lists
# HackerRank: https://www.hackerrank.com/challenges/nested-list/problem

students = []
num = int(input())

for i in range(num):
    name = input()
    grade = float(input())
    students.append([name, grade])

grades = sorted(set(student[1] for student in students))
second_lowest = grades[1]
names = []
for student in students:
    if student[1] == second_lowest:
        names.append(student[0])

names.sort()

for name in names:
    print(name)