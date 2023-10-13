def solution(n):
    answer = [[0 for _ in range(i + 1)] for i in range(n)]

    x, y = 0, 0
    count = 1
    for i in range(n):
        if i % 3 == 0:
            for j in range(n - i):
                answer[x][y] = count
                count += 1
                x += 1
            x -= 1
            y += 1

        elif i % 3 == 1:
            for j in range(n - i):
                answer[x][y] = count
                count += 1
                y += 1
            x -= 1
            y -= 2

        else:
            for j in range(n - i):
                answer[x][y] = count
                count += 1
                x -= 1
                y -= 1
            x += 2
            y += 1

    answer_list = []

    for i in answer:
        while i:
            answer_list.append(i.pop(0))

    return answer_list
