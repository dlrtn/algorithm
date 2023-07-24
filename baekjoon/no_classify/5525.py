def make_table(p):
    table = [0] * len(p)
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = table[j - 1]

        if p[i] == p[j]:
            j += 1
            table[i] = j
    return table

def KMP(p):
    table = make_table(p)
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