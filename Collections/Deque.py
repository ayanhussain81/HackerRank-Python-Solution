# Collections.Deque in Python - Hacker Rank Solution
# START
from collections import deque
n = int(input())
d = deque()
for i in range(n):
    s= input().split()
    if 'appendleft' in s:
        d.appendleft(s[1])
    elif 'append' in s:
        d.append(s[1])
    elif 'popleft' in s:
        d.popleft()
    else:
        d.pop()
print (' '.join(map(str,d)))

#END