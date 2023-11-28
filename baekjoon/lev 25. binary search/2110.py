import sys
import itertools
N, C = map(int, sys.stdin.readline().split())

x = list()
for i in range(N):
    x.append(int(sys.stdin.readline().rstrip()))
x.sort()
print(x)
print(list(itertools.combinations(x, C)))