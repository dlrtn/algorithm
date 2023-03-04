import copy

N, M, H = map(int, input().split())

tomato = []

for i in range(H):
    temp = []
    for j in range(M):
        temp.append(list(map(int, input().split())))
    tomato.append(temp)

sum = 0

for i in range(H):
    for j in range(M):
        sum += tomato[i][j].count(0)

if sum == 0:
    print(0)
    exit()

count = 0

now_tomato = copy.deepcopy(tomato)

while True:
    cnt_tomato = copy.deepcopy(tomato)
    sum = 0
    count += 1
    for i in range(H):
        for j in range(M):
            for k in range(N):
                if tomato[i][j][k] == 1:
                    if i > 0 and tomato[i - 1][j][k] == 0:
                        cnt_tomato[i - 1][j][k] = 1
                    if i < H - 1 and tomato[i + 1][j][k] == 0:
                        cnt_tomato[i + 1][j][k] = 1
                    if j > 0 and tomato[i][j - 1][k] == 0:
                        cnt_tomato[i][j - 1][k] = 1
                    if j < M - 1 and tomato[i][j + 1][k] == 0:
                        cnt_tomato[i][j + 1][k] = 1
                    if k > 0 and tomato[i][j][k - 1] == 0:
                        cnt_tomato[i][j][k - 1] = 1
                    if k < N - 1 and tomato[i][j][k + 1] == 0:
                        cnt_tomato[i][j][k + 1] = 1

    tomato = copy.deepcopy(cnt_tomato)

    for i in range(H):
        for j in range(M):
            sum += tomato[i][j].count(0)

    if sum == 0:
        print(count)
        break

    if tomato == now_tomato:
        print(-1)
        break

    now_tomato = copy.deepcopy(tomato)
