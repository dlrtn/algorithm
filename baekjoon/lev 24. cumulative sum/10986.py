import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(len(A) + 1)]

for i in range(1, len(A) + 1):
    dp[i] = (dp[i - 1] + A[i - 1]) % M

count = 0

count_array = [0 for _ in range(M)]

for i in range(len(dp)):
    count_array[dp[i]] += 1

for i in range(M):
    count += count_array[i] * (count_array[i] - 1) // 2

print(count)
