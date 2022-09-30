# Set Mutation in Python - Hacker Rank Solution
# START
N = int(input())
a = set(map(int, input().split()))
nn = int(input())
for i in range(nn):
    s = input().split()
    if(s[0] == 'intersection_update'):
        aa = set(map(int, input().split()))
        a.intersection_update(aa)
    elif (s[0] == 'update'):
        aa = set(map(int, input().split()))
        a.update(aa)
    elif (s[0] == 'symmetric_difference_update'):
        aa = set(map(int, input().split()))
        a.symmetric_difference_update(aa)
    elif (s[0] == 'difference_update'):
        aa = set(map(int, input().split()))
        a.difference_update(aa)
print(sum(a))
       