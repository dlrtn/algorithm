s = list(map(int, input().split()))

for i in range(len(s)):
    min_index = i
    for j in range(i, len(s)):
        if s[j] < s[min_index]:
            min_index = j

    s[i], s[min_index] = s[min_index], s[i]

print(s)
