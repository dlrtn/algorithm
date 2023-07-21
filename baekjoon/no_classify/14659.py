import sys

N = int(sys.stdin.readline())
lst = list(map(int, input().split()))

m = 0
prev_max = lst[0]
count = 0

for i in range(1, N):
    if lst[i] >= prev_max:
        prev_max = lst[i]
        count = 0
    else:
        count += 1
    m = max(count, m)

print(m)
