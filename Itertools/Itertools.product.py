# itertools.product() in Python - Hacker Rank Solution
# START
from itertools import product
arr1 = input().split()
arr1 = list(map(int,arr1))
arr2 = input().split()
arr2 = list(map(int, arr2))
result = list(product(arr1,arr2))
for i in result:
    print(i, end = " ");
# END