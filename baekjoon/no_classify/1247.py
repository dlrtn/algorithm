import sys

input = sys.stdin.readline

for i in range(3):
    N = int(input())
    s = 0
    for j in range(N):
        s += int(input())
    if s > 0:
        print('+')
    elif s < 0:
        print('-')
    else:
        print(0)