n = int(input())
arr = []
for i in range(n):
    [a, b] = list(map(int, input().split()))
    arr.append([a, b])
str = []

for x, y in arr:
    cnt = 0
    for i, j in arr:
        if arr[i] > arr[x] and arr[j] > arr[y]:
            cnt += 1
    str.append(cnt+1)
