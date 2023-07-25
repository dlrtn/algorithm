def make_table(p):
    table = [0] * len(p)
    for i in range(len(p)):
        if i == 0 or i == 1:
            table[i] = 0
        else:
            table[i] = i - 1


    return table

def KMP(p):
    table = make_table(p)
    print(table)
    cnt = 0
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = table[j - 1]

        if s[i] == p[j]:
            if j == len(p)-1:
                cnt += 1
                j = table[j]
            else:
                j += 1

    return cnt

N = int(input())
M = int(input())
s = input()
target = 'IO' * N + 'I'
ans = KMP(target)
print(ans)