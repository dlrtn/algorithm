a, b = map(int, input().split())
arr = []

sum = 0
for i in range(a, b+1):
    cnt = 0
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            cnt += 1
            break
    if cnt == 0:
        print(i)