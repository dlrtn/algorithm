def solution(park, routes):
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                now = [j, i]

    print(now)

    park_x = len(park[0])  # x
    park_y = len(park)  # y

    for i in routes:
        cnt = 0
        n = int(i[2])

        now_x = now[0]
        now_y = now[1]
        if i[0] == "E":
            for j in range(1, n + 1):
                if now_x + j >= park_x or park[now_y][now_x + j] == "X":
                    break
                cnt += 1

            if cnt == n:
                now[0] += n
        elif i[0] == "W":
            for j in range(1, n + 1):
                if now_x - j < 0 or park[now_y][now_x - j] == "X":
                    break
                cnt += 1

            if cnt == n:
                now[0] -= n
        elif i[0] == "S":
            for j in range(1, n + 1):
                if now_y + j >= park_y or park[now_y + j][now_x] == "X":
                    break
                cnt += 1

            if cnt == n:
                now[1] += n
        elif i[0] == "N":
            for j in range(1, n + 1):
                if now_y - j < 0 or park[now_y - j][now_x] == "X":
                    break
                cnt += 1

            if cnt == n:
                now[1] -= n

    return [now[1], now[0]]