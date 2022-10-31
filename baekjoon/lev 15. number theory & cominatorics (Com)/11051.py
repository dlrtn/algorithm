arr = [1, 1, 2]

for i in range(3, 1001):
    arr.append(arr[i-1] * i)

n, r = map(int, input().split())
print((arr[n]//(arr[r]*arr[n-r]))%10007)
