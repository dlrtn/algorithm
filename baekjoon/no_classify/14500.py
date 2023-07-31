N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
m = 0

dr = [(1, 0), (-1, 0), (0, -1), (0, 1)]

visited = [[False for _ in range(M)] for _ in range(N)]


def dfs(y, x, depth, s):
    global m

    if depth == 3:
        m = max(m, s)
        return

    for k in range(4):
        nx = x + dr[k][0]
        ny = y + dr[k][1]

        if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == False:
            visited[ny][nx] = True
            dfs(ny, nx, depth + 1, s + graph[ny][nx])
            visited[ny][nx] = False


def exce(i, j):
    global m

    for n in range(4):
        tmp = graph[i][j]
        for k in range(3):
            t = (n + k) % 4
            ni = i + dr[t][0]
            nj = j + dr[t][1]

            if not (0 <= ni < N and 0 <= nj < M):
                tmp = 0
                break
            tmp += graph[ni][nj]

        m = max(m, tmp)


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 0, graph[i][j])
        visited[i][j] = False

        exce(i, j)

print(m)
