from collections import deque

N, K = map(int, input().split())

if N == K:
    print(0)
    exit()

graph = [0] * 100001

queue = deque([N])

while queue:
    x = queue.popleft()

    for nx in (x - 1, x + 1, x * 2):
        if 0 <= nx <= 100000 and not graph[nx]:
            graph[nx] = graph[x] + 1
            queue.append(nx)

print(graph[K])
