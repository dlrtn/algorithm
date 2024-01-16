def find(x, parent):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x], parent)
        parent[x] = p
        return parent[x]


def union(x, y, parent):
    x = find(x, parent)
    y = find(y, parent)

    if x != y:
        parent[y] = x


def solution(n, computers):
    parent = [i for i in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if computers[i][j] == 1:
                union(i, j, parent)
    for i in range(n - 1, -1, -1):
        for j in range(i, -1, -1):
            if computers[i][j] == 1:
                union(i, j, parent)

    return len(set(parent))


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
print(solution(4, [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]))
