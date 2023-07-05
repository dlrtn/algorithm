N, M = map(int, input().split())

arr = []
def dfs(depth, N, M):
    if depth == M:
        print(' '.join(map(str, arr)))
    else:
        for i in range(1, N + 1):
            arr.append(i)
            dfs(depth + 1, N, M)
            arr.pop()
dfs(0, N, M)