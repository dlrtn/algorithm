n = int(input())
M = list(map(int,input().split()))
c = int(input())
A = list(map(int,input().split()))
B = []
for i in range(c):
    B.append(M.count(A[i]))
for i in range(c):
    print(B[i], end=' ')