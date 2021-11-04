n = int(input())
arr = []
for i in range(n):
    [a, b] = list(map(int, input().split()))
    arr.append([a, b])
str = []

for x, y in arr:
    cnt = 0
    for i, j in arr:
        if i > x and j > y:
            cnt += 1
    str.append(cnt+1)
for i in range(n):
    print(str[i], end = ' ')