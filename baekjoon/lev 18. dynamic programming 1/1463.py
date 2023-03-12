n = int(input())

arr = [0, 0, 1]

for i in range(3, n+1):
    temp = i

    if temp % 2 == 0 and temp % 3 == 0:
        arr.append(min(arr[temp//2], arr[temp//3]) + 1)
    elif temp % 2 == 0:
        arr.append(min(arr[temp - 1], arr[temp // 2]) + 1)
    elif temp % 3 == 0:
        arr.append(min(arr[temp - 1], arr[temp // 3]) + 1)
    else :
        arr.append(arr[temp - 1] + 1)

print(arr)