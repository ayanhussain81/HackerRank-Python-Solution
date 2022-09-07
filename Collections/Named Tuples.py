# Named.tuple  in Python - Hacker Rank Solution
# START
from collections import namedtuple
N = int(input())
lst = []

for i in range(N+1):
    if i == 0:
        header = input()
        Students = namedtuple('Students',header)
    else:
        student = input().split()
        lst.append(Students(student[0],student[1],student[2], student[3]))

std_sum = 0
for std in lst:
    std_sum += int(std.MARKS)

print(std_sum/N)

# END