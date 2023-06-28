n = int(input())

arr = [0]
for i in range(1, n):
    arr.append(arr[i - 1] + 2 * i)

print(arr[n-1])

