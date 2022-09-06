# Find a String in Python - Hacker Rank Solution
# START
def count_substring(string, sub_string):
    ans=0
    lenght=len(sub_string)
    for i in range(0, len(string)):
        if sub_string in string[i:lenght+i]:
            ans+=1
        else:
            pass
    return ans

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

# END