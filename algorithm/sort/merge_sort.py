s = list(map(int, input().split()))

p = 0
r = len(s) - 1
def merge_sort(s, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(s, p, q)
        merge_sort(s, q + 1, r)
        merge(s, p, q, r)



def merge(s, p, q, r):
    s1 = s[p:q + 1]
    s2 = s[q + 1:r + 1]
    i = 0
    j = 0
    k = p
    while i < len(s1) and j < len(s2):
        if s1[i] < s2[j]:
            s[k] = s1[i]
            i += 1
        else:
            s[k] = s2[j]
            j += 1
        k += 1
    while i < len(s1):
        s[k] = s1[i]
        i += 1
        k += 1
    while j < len(s2):
        s[k] = s2[j]
        j += 1
        k += 1

merge_sort(s, p, r)

print(s)