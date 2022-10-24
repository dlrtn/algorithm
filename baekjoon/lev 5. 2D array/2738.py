n, m = map(int, input().split())

MAP_1 = [list(map(int, input().split())) for _ in range(n)]
MAP_2 = [list(map(int, input().split())) for _ in range(n)]

answer = []


for i in range(n):
    temp = []
    for j in range(m):
        print(MAP_1[i][j] + MAP_2[i][j], end=' ')
    print()