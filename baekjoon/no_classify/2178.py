from collections import deque

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

visited = [[False] * M for _ in range(N)]
queue = deque([(0, 0)])

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
while queue:
    y, x = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 1 and not visited[ny][nx]:
            visited[ny][nx] = True
            graph[ny][nx] = graph[y][x] + 1
            queue.append((ny, nx))

print(graph[N - 1][M - 1])
