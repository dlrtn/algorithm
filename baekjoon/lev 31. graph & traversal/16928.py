from collections import deque

N, M = map(int, input().split())

ladder = {}
snake = {}
for i in range(N):
    start, end = map(int, input().split())
    ladder[start] = end

for j in range(M):
    start, end = map(int, input().split())
    snake[start] = end


def bfs():
    queue = deque([(1, 0)])
    visited = set()

    while queue:
        x, count = queue.popleft()
        if x in visited:
            continue

        visited.add(x)

        if x in ladder:
            x = ladder[x]
        elif x in snake:
            x = snake[x]

        for k in range(1, 7):
            new_x = x + k
            if new_x == 100:
                return count + 1

            if new_x < 100:
                queue.append((new_x, count + 1))

    return -1


print(bfs())
