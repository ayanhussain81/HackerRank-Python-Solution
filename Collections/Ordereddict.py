# OrderedDict in Python - Hacker Rank Solution
# START
from collections import OrderedDict
n = int(input())
od = OrderedDict()
for i in range(n):
    item = input().split()
    itemPrice = int(item[-1])
    itemName = ' '.join(item[:-1])
    if(od.get(itemName)):
        od[itemName] += itemPrice
    else:
       od[itemName] = itemPrice
for i in od.keys():
    print(i, od[i])

# END