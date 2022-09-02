# Mutations in Python - Hacker Rank Solution
# START
def mutate_string(string, position, character):
    st= [*string]
    p=len(st)
    st[position] = character
    str = ''
    for i in range(p):
        str = str + st[i]
    return str

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
# END