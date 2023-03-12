a, b = map(int, input().split())

lst = [str(0)] * a

for i in range(b):
    a, b, c = map(int, input().split())
    for j in range(a - 1, b):
        lst[j] = str(c)

print(' '.join(lst))
