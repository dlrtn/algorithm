from collections import deque

A, B = map(int, input().split())

visited = set()


def bfs(n, depth):
    que = deque([(n, depth)])

    while que:
        n, depth = que.popleft()

        if n == B:
            return depth

        if n * 2 not in visited and n * 2 <= B:
            visited.add(n * 2)
            que.append((n * 2, depth + 1))

        if n * 10 + 1 not in visited and n * 10 + 1 <= B:
            visited.add(n * 10 + 1)
            que.append((n * 10 + 1, depth + 1))

    return -1


print(bfs(A, 1))
