# Find the runner up in Python - Hacker Rank Solution
# START
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(list(set(arr)))[-2])
# END