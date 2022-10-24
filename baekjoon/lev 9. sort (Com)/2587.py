arr = []
n = 0
for i in range(5):
    x = int(input())
    arr.append(x)
    n += x

arr.sort()
print(n//5)
print(arr[2])

