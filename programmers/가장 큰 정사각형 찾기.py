import copy

def solution(board):
    answer = 0
    answer_list = copy.deepcopy(board)

    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if answer_list[i - 1][j - 1] > 0 and answer_list[i][j - 1] and answer_list[i - 1][j] and board[i][j] > 0:
                answer_list[i][j] = min(answer_list[i - 1][j - 1], answer_list[i][j - 1], answer_list[i - 1][j]) + 1

    for i in range(len(board)):
        for j in range(len(board[0])):
            if answer_list[i][j] > answer:
                answer = answer_list[i][j]

    return answer * answer