import sys

sudoku = []

for _ in range(9):
    sudoku.append(list(map(int, sys.stdin.readline().split())))

zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]


def is_right(sudoku, number, i, j):
    x, y = (i // 3) * 3, (j // 3) * 3

    for dx in range(x, x + 3):
        for dy in range(y, y + 3):
            if sudoku[dx][dy] == number:
                return False

    for index in range(9):
        if sudoku[index][j] == number:
            return False
        if sudoku[i][index] == number:
            return False

    return True


def answer(sudoku, index, zeros):
    if index >= len(zeros):
        for i in range(9):
            print(*sudoku[i])
        exit()
    for num in range(1, 10):
        if is_right(sudoku, num, zeros[index][0], zeros[index][1]):
            sudoku[zeros[index][0]][zeros[index][1]] = num
            answer(sudoku, index + 1, zeros)
            sudoku[zeros[index][0]][zeros[index][1]] = 0


answer(sudoku, 0, zeros)
