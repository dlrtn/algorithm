N = int(input())

graph = []
for i in range(N):
    graph.append(list(str(input())))

count = 0


def dfs(x, y):
    global count
    graph[x][y] = 0

    if x > 0 and graph[x - 1][y] == '1':
        count += 1
        dfs(x - 1, y)
    if x < N - 1 and graph[x + 1][y] == '1':
        count += 1
        dfs(x + 1, y)
    if y > 0 and graph[x][y - 1] == '1':
        count += 1
        dfs(x, y - 1)
    if y < N - 1 and graph[x][y + 1] == '1':
        count += 1
        dfs(x, y + 1)


answer = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == '1':
            count = 1
            dfs(i, j)
            answer.append(count)

print(len(answer))
answer.sort()
for i in answer:
    print(i)
