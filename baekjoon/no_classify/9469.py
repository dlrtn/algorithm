T = int(input())

for _ in range(T):
    a, b, c, d, e = map(float, input().split())

    print("{} {:.6f}".format(int(a), b/(c+d)*e))