N = int(input())


def rabin_karp(str, s):
    i = 0
    w = len(s) - 1

    find_list = []

    s_hashValue = 0
    str_hashValue = 0

    for x in range(len(s)):
        s_hashValue += ord(s[x]) * (2 ** x)

    for x in range(len(s)):
        str_hashValue += ord(str[x]) * (2 ** x)

    while True:
        if str_hashValue == s_hashValue:
            find_list.append(i)

        if i >= len(str) - len(s):
            break

        str_hashValue -= ord(str[i])
        str_hashValue //= 2
        w += 1
        str_hashValue += ord(str[w]) * (2 ** (len(s) - 1))
        i += 1

    return find_list

for i in range(N):
    str = input()
    s = input()

    print(rabin_karp(str, s))
