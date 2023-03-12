a, b = map(int, input().split())

lst = []

for i in range(a):
    lst.append(str(i + 1))

for i in range(b):
    a, b = map(int, input().split())

    temp = str(lst[a - 1])
    lst[a - 1] = str(lst[b - 1])
    lst[b - 1] = str(temp)

print(' '.join(lst))
