import sys

N, P, Q = map(int, sys.stdin.readline().split())

dp = dict()
dp[0] = 1


def dynamic_programming(n):
    if n == 0:
        return 1
    else:
        if dp.get(n // P) is None or dp.get(n // Q) is None:
            dp[n // P] = dynamic_programming(n // P)
            dp[n // Q] = dynamic_programming(n // Q)

    return dp[n // Q] + dp[n // P]


print(dynamic_programming(N))
