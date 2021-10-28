n = int(input())
a = [[1, 0], [0, 1]]
for i in range(2, 41):
    a.append([a[i - 1][0] + a[i - 2][0], a[i - 1][1] + a[i - 2][1]])
for j in range(n):
    temp = int(input())
    print(a[temp][0], a[temp][1])

