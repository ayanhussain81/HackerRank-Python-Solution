# Symmetric Difference in Python - Hacker Rank Solution
# START
n1 = int(input())
set1 = set(map(int,input().split()))
n2 = int(input())
set2 = set(map(int,input().split()))
set3 = (set1.difference(set2)).union(set2.difference(set1))
for i in sorted(list(set3)):
        print (i)
# END