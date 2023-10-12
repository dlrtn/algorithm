import sys

N = int(sys.stdin.readline().rstrip())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

global minus_1, zero, plus_1
minus_1, zero, plus_1 = 0, 0, 0


def divide_and_conquer(x, y, n):
    global minus_1, zero, plus_1

    if n == 1:
        if paper[x][y] == 0:
            zero += 1
        elif paper[x][y] == -1:
            minus_1 += 1
        else:
            plus_1 += 1

        return

    check = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != paper[i][j]:
                check = -2
                break

    if check == -2:
        divide_and_conquer(x, y, n // 3)
        divide_and_conquer(x, y + n // 3, n // 3)
        divide_and_conquer(x, y + (n // 3) * 2, n // 3)
        divide_and_conquer(x + n // 3, y, n // 3)
        divide_and_conquer(x + n // 3, y + n // 3, n // 3)
        divide_and_conquer(x + n // 3, y + (n // 3) * 2, n // 3)
        divide_and_conquer(x + (n // 3) * 2, y, n // 3)
        divide_and_conquer(x + (n // 3) * 2, y + n // 3, n // 3)
        divide_and_conquer(x + (n // 3) * 2, y + (n // 3) * 2, n // 3)
    else:
        if check == 0:
            zero += 1
        elif check == -1:
            minus_1 += 1
        else:
            plus_1 += 1


divide_and_conquer(0, 0, N)

print(minus_1)
print(zero)
print(plus_1)
