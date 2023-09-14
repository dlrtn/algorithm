import sys

sys.setrecursionlimit(10 ** 6)

def main():
    N, M, R = map(int, sys.stdin.readline().split())
    adjacency_list = [[] for _ in range(N)]

    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1
        v -= 1
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    for i in range(N):
        adjacency_list[i].sort()

    visited = [0] * N
    count = 1

    def dfs(start):
        nonlocal count
        visited[start] = count
        count += 1
        for neighbor in adjacency_list[start]:
            if not visited[neighbor]:
                dfs(neighbor)

    dfs(R - 1)

    for i in range(N):
        print(visited[i])

if __name__ == "__main__":
    main()
