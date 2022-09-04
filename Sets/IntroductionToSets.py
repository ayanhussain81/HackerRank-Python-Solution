# Introduction's to set in Python - Hacker Rank Solution
# START
def average(array):
    x = sum(set(array))
    z= len(set(array))
    ans = x/z
    return ans


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
# END