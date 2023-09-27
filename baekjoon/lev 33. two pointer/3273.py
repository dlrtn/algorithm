import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

a.sort()

i, j = 0, len(a) - 1

count = 0
while i < j:
    if a[i] + a[j] == x:
        count += 1
        j -= 1
        i += 1
    elif a[i] + a[j] > x:
        j -= 1
    else:
        i += 1

print(count)
