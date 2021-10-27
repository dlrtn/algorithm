n = int(input())
arr = []
for i in range(n):
    temp = int(input())
    arr.append(temp)
max = 0
cnt = 0
c = []
print(int(sum(arr)//len(arr)))
print(sorted(arr)[len(arr)//2])
for i in range(n):
    if max < arr.count(arr[i]):
        max = arr[i]
        cnt+=1
        c.append(arr[i])
        if cnt == 2:
            break
if len(c) == 1:
    print(sorted(c)[0])
else:
    print(sorted(c)[1])
if n == 1:
    print(0)
else:
    print(sorted(arr)[n-1]-sorted(arr)[0])