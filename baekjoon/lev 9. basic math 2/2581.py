a = int(input())
b = int(input())
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
        sum += i
        arr.append(i)
if sum == 0:
    print(-1)
    exit()
print(sum)
print(arr[0])