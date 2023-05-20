global flag

def dfs(places, come, y, x, depth): # 출발좌표와 어디서 왔는지
    if depth == 3 or y < 0 or x < 0 or x > 4 or y > 4:
        return None

    if come != 0 and places[y][x] == 'X':
        print(y, x, places[y][x], "come", come, "depth", depth)
        return None

    if come != 0 and places[y][x] == 'P':
        print(y, x, places[y][x], "come", come, "depth", depth)
        global flag
        flag = 1

        return None

    if depth > 0:
        print(y, x, places[y][x], "come", come, "depth", depth)

    if come == 0 or places[y][x] == 'O':
        # 상 : 1, 하 : 2, 좌 : 3, 우 : 4
        if come != 1: # 위에서 온거야,  위로 보냄
            dfs(places, 2, y - 1, x, depth + 1)

        if come != 2: # 아래에서 옴
            dfs(places, 1, y + 1, x, depth + 1)

        if come != 3: # 왼쪽에서 옴
            dfs(places, 4, y, x - 1, depth + 1)

        if come != 4: # 오른쪽에서 옴
            dfs(places, 3, y, x + 1, depth + 1)

def solution(places):
    global flag

    answer = [1, 1, 1, 1, 1]
    for i in range(5):
        for j in range(5):
            for k in range(5):
                if places[i][j][k] == 'P':
                    global flag
                    flag = 0
                    dfs(places[i], 0, j, k, 0)
                    if flag == 1:
                        answer[i] = 0
    return answer