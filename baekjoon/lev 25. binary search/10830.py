import sys

N, B = map(int, sys.stdin.readline().split())


def mul_mat(a_mat, b_mat, n):
    rst = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                rst[i][j] += (a_mat[i][k] * b_mat[k][j])
            rst[i][j] %= 1000
    return rst


A = []
for i in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(N):
        A[i][j] %= 1000

rst = [[0] * N for _ in range(N)]
for i in range(N):
    rst[i][i] = 1

while B > 0:
    if B % 2:
        rst = mul_mat(rst, A, N)
    B >>= 1
    A = mul_mat(A, A, N)

for i in rst:
    print(*i)
