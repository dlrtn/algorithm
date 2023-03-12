a, b = map(int, input().split())

lst = []

for i in range(a):
    lst.append(str(i + 1))

print(lst)

for i in range(b):
    x, y = map(int, input().split())
    temp_lst = lst[x - 1:y]

    temp_lst.reverse()
    for i in range(x - 1, y):
        lst[i] = temp_lst[i - x + 1]


print(' '.join(lst))