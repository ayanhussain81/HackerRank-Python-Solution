# SwapCase in Python - Hacker Rank Solution
# START
def swap_case(s):
    list=[]
    lenght = len(s)
    for i in range(lenght):
        if (s[i].islower()== True):
            list.append(s[i].upper())
        elif (s[i].islower()== False):
            list.append(s[i].lower())
            
    result=""  
    
    for i in range (lenght):
        result+= list[i]
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# END