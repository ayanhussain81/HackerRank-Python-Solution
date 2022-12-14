# Collections.Counter in Python - Hacker Rank Solution
# START
from collections import Counter
n = int(input())
l = input().split()
numCust = int(input())

arr = list(map(int,l))
ans=0
for i in range(numCust):
    money = input().split()
    mmm = list(map(int,money))
    if mmm[0] in arr:
        x= mmm[0]
        ans = ans + mmm[1]
        arr.remove(x)
    else:
        pass
print(ans)
# END
#                                   OR

import collections

numShoes = int(input())
shoes = collections.Counter(map(int, input().split()))
numCust = int(input())
income = 0

for i in range(numCust):
    size, price = map(int, input().split())
    if shoes[size]: 
        income += price
        shoes[size] -= 1

print(income)