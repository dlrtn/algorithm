N = int(input())

A = list(map(int, input().split()))

dp = [1] * N
dp1 = [1] * N
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i],dp[j]+1)
B = list(reversed(A))
for i in range(N):
    for j in range(i):
        if B[j] < B[i]:
            dp1[i] = max(dp1[i],dp1[j]+1)
for i in range(N):
    dp1[i] += dp[i]
print(max(dp1))