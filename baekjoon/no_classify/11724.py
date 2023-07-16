import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)
count = 0


def bfs(start_node):
    queue = deque([start_node])
    visited[start_node] = True

    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

    return visited


for i in range(1, N + 1):
    if not visited[i]:
        if not graph[i]:
            count += 1
            visited[i] = True
        else:
            bfs(i)
            count += 1

print(count)
