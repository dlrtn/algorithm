n = int(input())
arr = []
for i in range(n):
    temp = int(input())
    arr.append(temp)

for i in sorted(arr):
    print(i)