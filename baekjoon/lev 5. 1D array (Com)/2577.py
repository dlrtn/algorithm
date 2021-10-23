A = int(input())
B = int(input())
C = int(input())

n = A * B * C
a = [100000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1]
b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if n < 10000000:
    for i in a[2:]:
        c[b[n // i % 10]] += 1
elif n < 100000000:
    for i in a[1:]:
        c[b[n // i % 10]] += 1
else:
    for i in a:
        c[b[n // i % 10]] += 1

for i in c:
    print(i)