def solution(n):
    board = [[0] * n for _ in range(n)]

    trans = 1
    cnt = 1
    row, col = 0, -1

    while n > 0:
        for i in range(n):
            col += trans
            board[row][col] = cnt
            cnt += 1

        n -= 1

        for i in range(n):
            row += trans
            board[row][col] = cnt
            cnt += 1

        trans *= -1

    return board
