N, k = map(int, input().split())

x = list(map(int, input().split()))

x.sort()

print(x[N-k])
