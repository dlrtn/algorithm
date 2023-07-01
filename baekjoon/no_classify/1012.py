T = int(input())

def dfs(farm, x, y):
    farm[y][x] = 0

    if x > 0 and farm[y][x - 1] == 1:
        dfs(farm, x - 1, y)
    if x < M - 1 and farm[y][x + 1] == 1:
        dfs(farm, x + 1, y)
    if y > 0 and farm[y - 1][x] == 1:
        dfs(farm, x, y - 1)
    if y < N - 1 and farm[y + 1][x] == 1:
        dfs(farm, x, y + 1)

    return 1

for _ in range(T):
    M, N, K = map(int, input().split())
    count = 0

    farm = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            print(farm[i][j], end=' ')
        print()

    print('================ 배추 심기 ================')
    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1

    for i in range(N):
        for j in range(M):
            print(farm[i][j], end=' ')
        print()

    for y in range(N):
        for x in range(M):
            if farm[y][x] == 1:
                count += 1
                dfs(farm, x, y)

                print('================ 애벌레 열일 중 ================')
                for i in range(N):
                    for j in range(M):
                        print(farm[i][j], end=' ')
                    print()

    print(count)