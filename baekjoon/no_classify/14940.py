from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

y, x = 0, 0


def find_start():
    global y, x
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                graph[i][j] = -1
            if graph[i][j] == 2:
                y = i
                x = j


find_start()


def bfs(y, x):
    visited = set()
    queue = deque([(y, x, 0)])

    neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        y, x, count = queue.popleft()
        visited.add((y, x))
        graph[y][x] = count

        for dy, dx in neighbors:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == -1 and (ny, nx) not in visited:
                queue.append((ny, nx, count + 1))
                visited.add((ny, nx))


bfs(y, x)

for i in range(n):
    for j in range(m):
        print(graph[i][j], end=' ')
    print()
