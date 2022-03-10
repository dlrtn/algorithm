a = int(input())

arr = []
arr.append(1)
arr.append(2)
for i in range(2, a):
    arr.append((arr[i-2]+arr[i-1])%15746)
print(arr[a-1])