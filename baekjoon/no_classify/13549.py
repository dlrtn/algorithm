from collections import deque

N, K = map(int, input().split())

graph = [-1] * 100001
graph[N] = 0
queue = deque([N])

while queue:
    x = queue.popleft()
    if x == K:
        print(graph[K])
        break

    if 0 <= x - 1 <= 100000 and graph[x - 1] == -1:
        graph[x - 1] = graph[x] + 1
        queue.append(x - 1)

    if 0 <= x * 2 <= 100000 and graph[x * 2] == -1:
        graph[x * 2] = graph[x]
        queue.appendleft(x * 2)

    if 0 <= x + 1 <= 100000 and graph[x + 1] == -1:
        graph[x + 1] = graph[x] + 1
        queue.append(x + 1)
