from collections import deque

N, M = map(int, input().split())

graph = dict()
for _ in range(M):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)

    if b not in graph:
        graph[b] = [a]
    else:
        graph[b].append(a)


def bfs(graph, start):
    visited = set()
    queue = deque([(start, 0)])
    visited.add(start)
    visited_count = 0

    while queue:
        node, count = queue.popleft()
        visited_count += count

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, count + 1))
                visited.add(neighbor)

    return visited_count

answer_list = []
for i in range(1, N + 1):
    answer_list.append(bfs(graph, i))

print(answer_list.index(min(answer_list)) + 1)
