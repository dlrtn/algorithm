import sys


def solution(sequence, k):
    size = len(sequence)
    array = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(i, size):
            if i == j:
                array[i][j] += sequence[j]
            else:
                array[i][j] += array[i][j - 1] + sequence[j]

    gap = sys.maxsize
    answer_x, answer_y = 0, 0
    for i in range(size):
        for j in range(i, size):
            if array[i][j] == k and gap > (abs(i - j)):
                gap = abs(i - j)
                answer_x, answer_y = i, j

    return [answer_x, answer_y]
