def square(a):
    return a * a


def solve(x, y):
    if x == n:
        return 0
    if dp[x][y] != -1:
        return dp[x][y]
    ret = solve(x + 1, y)
    if y != 0:
        ret = min(ret, solve(x + 1, y - 1))
    if y != m - 1:
        ret = min(ret, solve(x + 1, y + 1))
    ret += square(abs(a[x][y] - b[x][y]))
    dp[x][y] = ret
    return ret


n, m = map(int, input().split())
a = []
b = []
for _ in range(n):
    a.append(list(map(int, input().split())))
for _ in range(n):
    b.append(list(map(int, input().split())))

dp = [[-1] * m for _ in range(n)]
for i in range(m):
    solve(0, i)

print(min(dp[0]))