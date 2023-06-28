a, b = map(int, input().split())
c = int(input())
n_0 = int(input())

if (c - a) * n_0 - b >= 0 and a <= c:
    print(1)
else:
    print(0)
