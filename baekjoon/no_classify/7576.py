from collections import deque

M, N = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

queue = deque([])

zero_count = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            zero_count += 1
        if graph[i][j] == 1:
            queue.append([i, j])

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])


bfs()
m = 0

for i in range(N):
    for j in range(M):
        m = max(m, graph[i][j])
        if graph[i][j] == 0:
            print(-1)
            exit()
print(m - 1)
