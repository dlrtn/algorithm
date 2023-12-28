d = [[0, 0], [0, 1], [1, 0], [1, 1]]


def solution(m, n, board):
    answer = 0

    delete_set = list()

    horizontal_board = list(map(list, board))
    while True:
        for i in range(m - 1):
            for j in range(n - 1):
                if horizontal_board[i][j] != '' and is_deleted(i, j, horizontal_board):
                    for x in d:
                        delete_set.append((x[1] + i, x[0] + j))
        delete_set = list(set(delete_set))
        delete_set.sort(key=lambda x: (x[1], x[0]))
        if delete_set:
            vertical_board = makeVeticalBoard(n, m, horizontal_board)

            for i in delete_set:
                answer += 1
                vertical_board[i[1]].pop(i[0])
                vertical_board[i[1]].insert(0, '')
            horizontal_board = makeHorizontalBoard(n, m, vertical_board)
            delete_set.clear()
            continue
        break
    return answer


def is_deleted(y, x, board):
    for i in d:
        if board[y][x] != board[y + i[1]][x + i[0]] or board[y + i[1]][x + i[0]] == '':
            return False
    return True


def makeVeticalBoard(n, m, board: [[]]):
    vertical_board = []

    for i in range(n):
        temp_list = []
        for j in range(m):
            temp_list.append(board[j][i])
        vertical_board.append(temp_list)

    return vertical_board


def makeHorizontalBoard(n, m, board: [[]]):
    horizontal_board = []

    for i in range(m):
        temp_list = []
        for j in range(n):
            temp_list.append(board[j][i])
        horizontal_board.append(temp_list)

    return horizontal_board


def printVerticalBoard(board):
    for i in board:
        print(i)


def printHorizontalBoard(board):
    for i in board:
        print(i)


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
