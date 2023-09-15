import sys

first_str = sys.stdin.readline().rstrip()
second_str = sys.stdin.readline().rstrip()

dp = [[0 for _ in range(len(second_str) + 1)] for _ in range(len(first_str) + 1)]

for i in range(len(first_str)):
    for j in range(len(second_str)):
        if first_str[i] == second_str[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

for i in range(len(dp)):
    print(dp[i])
