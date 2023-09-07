def pi(s):
    j = 0
    i = 1
    pi = [0] * len(s)

    while i < len(s):
        if s[i] == s[j]:
            j += 1
            pi[i] = j
            i += 1
        else:
            if j == 0:
                i += 1
            else:
                j = pi[j - 1]

    return pi

def KMP(str, s):
    p = pi(s)
    i = 0
    j = 0
    while i < len(str):
        if str[i] == s[j]:
            j += 1
            if j == len(s):
                print(i)
            i += 1
        else:
            if j == 0:
                i += 1
            else:
                j = p[j - 1]
    return False

print(KMP("ababacabacaabacaaba", "abacaaba"))

