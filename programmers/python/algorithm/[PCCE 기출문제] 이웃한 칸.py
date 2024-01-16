def solution(board, h, w):
    answer = 0

    color = board[h][w]

    if h > 0 and board[h-1][w] == color:
        answer += 1

    if h < len(board[0]) - 1 and board[h+1][w] == color:
        answer += 1

    if w > 0 and board[h][w - 1] == color:
        answer += 1

    if w < len(board) - 1 and board[h][w + 1] == color:
        answer += 1


    return answer