# itertools.Permutations in Python - Hacker Rank Solution
# START
from itertools import permutations

a = input().split()
x = int(a[1])
for i in range(x, int(a[1]) + 1):
    for j in permutations(sorted(a[0]), i):
        print (''.join(j))

# END