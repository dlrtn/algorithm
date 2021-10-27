n = int(input())
arr = []
for i in range(n):
    temp = int(input())
    arr.append(temp)
a = [0] * 100000
for i in arr:
    a[i] += 1
for i in range(n):
    for j in range(a[i]):
        print(i)