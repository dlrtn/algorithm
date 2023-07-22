from collections import deque

N, M = map(int, input().split())

visited = [[False for _ in range(M)] for _ in range(N)]
map = []
for i in range(N):
    map.append(list(input()))

start_node = []
for i in range(N):
    for j in range(M):
        if map[i][j] == 'I':
            start_node = (i, j)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

count = 0
queue = deque([start_node])
while queue:
    y, x = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == False and map[ny][nx] != "X":
            queue.append([ny, nx])
            visited[ny][nx] = True
            if map[ny][nx] == 'P':
                count += 1
if count == 0:
    print('TT')
else:
    print(count)
