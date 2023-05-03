def solution(board, k):
    answer = 0

    for i in range(len(board[0])):
        for j in range(len(board)):
            if i + j <= k:
                answer += board[j][i]

    return answer
