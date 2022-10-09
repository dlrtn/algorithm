T = int(input())

arr = [1, 1, 2]

for i in range(3, 30):
    arr.append(arr[i-1] * i)

for i in range(T):
    r, n = map(int, input().split())
    print(arr[n]//(arr[r]*arr[n-r]))
