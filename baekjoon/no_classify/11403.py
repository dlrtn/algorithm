from collections import deque

N = int(input())

graph = []
line = {}
for i in range(N):
    graph.append(list(map(int, input().split())))

    for j in range(len(graph[i])):
        if graph[i][j] == 1:
            if j not in line.keys():
                line[j] = []
            if i not in line.keys():
                line[i] = []
            line[j].append(i)
            line[i].append(j)


def bfs(n):
    queue = deque([n])

    while queue:
        print(queue)
        x = queue.popleft()
        print(x)
        for i in line[x - 1]:
            graph[n - 1][i] = 1
            queue.append(i)


print(line)
print(graph)

bfs(1)
