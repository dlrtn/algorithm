c = int(input())
arr = []
for i in range(c):
    arr.append(list(map(int, input().split())))
max = 0
temp = 0
cnt = 1
for i in range(c-1):
    temp = i
    if arr[temp][1] < arr[temp+1][0]:
        cnt += 1

print(cnt)