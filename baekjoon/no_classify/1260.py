from collections import deque


def create_graph():
    graph = dict()

    for _ in range(M):
        a, b = map(int, input().split())

        if a not in graph:
            graph[a] = set()
        graph[a].add(b)

        if b not in graph:
            graph[b] = set()
        graph[b].add(a)

    return graph


def dfs(graph, start, visited=None):
    if visited is None:
        visited = []

    visited.append(start)

    if start not in graph:
        return visited

    for i in graph[start]:
        if i not in visited:
            dfs(graph, i, visited)

    return visited


def bfs(graph, start):
    visited = []
    queue = deque([start])
    visited.append(start)

    if start not in graph:
        return visited

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)

    return visited


def print_result(result):
    for i in result:
        print(i, end=' ')
    print()


N, M, V = map(int, input().split())
graph = create_graph()

dfs_result = dfs(graph, V)
bfs_result = bfs(graph, V)

print_result(dfs_result)
print_result(bfs_result)
