def solution(n):
    answer = []

    def move(start, end):
        answer.append([start, end])

    def hanoi(N, start, end, sub):
        if N == 1:
            move(start, end)
            return
        else:
            hanoi(N - 1, start, sub, end)
            move(start, end)
            hanoi(N - 1, sub, end, start)

    hanoi(n, 1, 3, 2)

    return answer
