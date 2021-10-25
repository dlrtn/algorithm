n = int(input())
arr = list(map(int, input().split()))
c = 0
for i in range(n):
    cnt = 0
    if arr[i] == 1:
        continue
    for j in range(2, arr[i]):
        if arr[i] % j == 0:
            cnt += 1
            break
    if cnt == 0:
        c += 1
print(c)
