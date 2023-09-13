N = int(input())

lst = [[0] * N for _ in range(N)]

graph = {}
T = int(input())
if T == 0:
    print(0)
    exit()
for i in range(T):
    a, b = map(int, input().split())

    if a not in graph.keys():
        graph[a] = []
    graph[a].append(b)
    if b not in graph.keys():
        graph[b] = []
    graph[b].append(a)


def dfs(graph, start_node):
    visited = []
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])

    return visited


print(len(dfs(graph, 1)) - 1)
