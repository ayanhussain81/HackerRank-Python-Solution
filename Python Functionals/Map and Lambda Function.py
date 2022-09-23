# Map and lambda in Python - Hacker Rank Solution
# START
cube = lambda x: x*x*x

def fibonacci(n):
    a =0
    b = 1
    x=[0,1]
    for i in range(n-2):
        nextt= a+b
        x.append(nextt)
        a=b
        b=nextt
    return(x[0:n])


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))