# split and join in Python - Hacker Rank Solution
# START
def split_and_join(line):
    line = line.split(" ")
    line= "-".join(line)
    return(line)

ifd __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
# END