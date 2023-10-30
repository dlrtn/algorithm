import sys

A = [[0 for _ in range(128)] for _ in range(128)]
B = [[0 for _ in range(128)] for _ in range(128)]

N, M = map(int, sys.stdin.readline().split())

for i in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        A[i][j] = arr.pop(0)

M, K = map(int, sys.stdin.readline().split())
for i in range(M):
    arr = list(map(int, sys.stdin.readline().split()))
    for j in range(K):
        B[i][j] = arr.pop(0)

print(A, B)
