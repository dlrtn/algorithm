s = list(map(int, input().split()))
n = int(input())

for i in range(len(s)):
    for j in range(i):
        if s[i] < s[j]:
            s[i], s[j] = s[j], s[i]

print(s)