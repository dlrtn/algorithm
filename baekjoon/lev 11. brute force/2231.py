n = int(input())

for i in range(n):
    arr = map(int, str(i))
    if n == i+sum(arr):
        print(i)
        exit()
print(0)