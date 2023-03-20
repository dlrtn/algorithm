arr = []

for i in range(1, 31):
    arr.append(i)

for i in range(28):
    n = int(input())
    arr.remove(n)

print(arr[0])
print(arr[1])