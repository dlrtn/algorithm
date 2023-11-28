import sys
sys.setrecursionlimit(10**6)

def dfs(maps, y, x, count):
    count += int(maps[y][x])
    maps[y][x] = "X"
    if x - 1 >= 0 and maps[y][x - 1] != "X":
        count = dfs(maps, y, x - 1, count)
    if x + 1 < len(maps[0]) and maps[y][x + 1] != "X":
        count = dfs(maps, y, x + 1, count)
    if y - 1 >= 0 and maps[y - 1][x] != "X":
        count = dfs(maps, y - 1, x, count)
    if y + 1 < len(maps) and maps[y + 1][x] != "X":
        count = dfs(maps, y + 1, x, count)

    return count


def solution(maps):
    answer = []

    for i in range(len(maps)):
        maps[i] = list(maps[i])

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != "X":
                answer.append(dfs(maps, i, j, 0))
    answer.sort()
    if len(answer) == 0:
        return [-1]
    return answer

