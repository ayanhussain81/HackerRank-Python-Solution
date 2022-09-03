# Nested Lists in Python - Hacker Rank Solution
# START
Result =[]
scorelist = []
if __name__ == '__main__':
    for i in range(int(input())):
        name = input()
        score = float(input())
        Result+=[[name,score]]
        scorelist+=[score]
    b=sorted(list(set(scorelist)))[1] 
    for a,c in sorted(Result):
        if c==b:
            print(a)
# END