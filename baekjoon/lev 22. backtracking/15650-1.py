N, M = map(int, input().split())

arr = []
def dfs(start, N, M, depth):
    if M == depth:
        print(' '.join(map(str, arr)))
    else:
        for i in range(start, N + 1):
            arr.append(i)
            dfs(i + 1, N, M, depth + 1)
            arr.pop()


dfs(1, N, M, 0)