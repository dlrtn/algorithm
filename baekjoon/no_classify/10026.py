from collections import deque

N = int(input())

graph = []
for i in range(N):
    graph.append(list(input()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

normal_count = 0
normal_visited = set()


def bfs_for_normal(color, x, y):
    global normal_count
    queue = deque([(x, y)])  # Corrected the queue initialization
    if (x, y) not in normal_visited:
        normal_visited.add((x, y))  # Corrected the visited set initialization
        normal_count += 1

    while queue:
        x1, y1 = queue.popleft()
        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in normal_visited and graph[nx][ny] == color:
                queue.append((nx, ny))  # Corrected the append() method
                normal_visited.add((nx, ny))

red_green_count = 0
red_green_visited = set()


def bfs_for_red_green(color, x, y):
    global red_green_count
    queue = deque([(x, y)])
    if (x, y) not in red_green_visited:
        red_green_visited.add((x, y))
        red_green_count += 1
    color_lst = []
    if color == 'B':
        color_lst.append('B')
    else:
        color_lst.append('R')
        color_lst.append('G')

    while queue:
        x1, y1 = queue.popleft()
        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in red_green_visited and graph[nx][ny] in color_lst:
                queue.append((nx, ny))  # Corrected the append() method
                red_green_visited.add((nx, ny))


for i in range(N):
    for j in range(N):
        bfs_for_normal(graph[i][j], i, j)
        bfs_for_red_green(graph[i][j], i, j)
print(normal_count)
print(red_green_count)
