N = int(input())

lst = []
graph = []
for i in range(N):
    lst.append(list(map(int, input().split()))[1:])

visited = [[False for _ in range(10)] for _ in range(1001)]

for i in range(N - 1):
    for j in range(len(lst[i])):
        for k in range(len(lst[i + 1])):
            if lst[i][j] == lst[i + 1][k]:
                pass
            else:
                if len(graph) == i:
                    graph.append({})
                if lst[i][j] not in graph[i].keys():
                    graph[i][lst[i][j]] = []
                graph[i][lst[i][j]].append(lst[i + 1][k])

print(graph)

answer = []

def dfs(start, depth=1):
    visited[depth][start] = True # 조회 부분
    print(start, depth)
    if depth > len(graph): # 만약 깊이가 graph보다 깊어지면 스탑
        return visited

    for i in graph[depth - 1][start]:
        if not visited[depth][i]:
            dfs(i, depth + 1)

    return visited


for i in graph[0].keys():
    visited = [[False for _ in range(10)] for _ in range(1001)]
    print(dfs(i))
