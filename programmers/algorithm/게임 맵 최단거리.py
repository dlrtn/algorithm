from collections import deque

def solution(maps):
    start = (0, 0, 1)
    n = len(maps[0])
    m = len(maps)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    que = deque([start])
    visited = set()
    visited.add((0, 0))

    while que:
        y, x, count = que.popleft()

        if y == m-1 and x == n-1:
            return count

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < n and 0 <= ny < m and maps[ny][nx] == 1 and (ny, nx) not in visited:
                que.append((ny, nx, count + 1))
                visited.add((ny, nx))

    return -1