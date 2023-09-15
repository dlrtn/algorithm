import sys

N = int(sys.stdin.readline())
stair_list = []

for _ in range(N):
    stair_list.append(int(sys.stdin.readline()))

dp = [0 for _ in range(N + 1)]

dp[1] = stair_list[0]
dp[2] = stair_list[1] + dp[1]
dp[3] = max(stair_list[2] + dp[1], stair_list[2] + dp[2])

for i in range(4, N):
    dp[i] = max(dp[N-3] + dp[N-2], dp[N-3] + dp[N-1], dp[N-2] + dp[N-1]) + stair_list[i - 1]

print(dp)
print(dp[N])
