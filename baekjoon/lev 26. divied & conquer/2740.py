import sys

A = []
B = []
N, M = map(int, sys.stdin.readline().split())
for i in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

M, K = map(int, sys.stdin.readline().split())
for i in range(M):
    B.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(K):
        temp = 0
        for k in range(M):
            temp += A[i][k] * B[k][j]
        print(temp, end=' ')
    print()
