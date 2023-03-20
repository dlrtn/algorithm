def solution(triangle):
    answers = []
    for i in range(len(triangle)):
        answers.append([])

    answers[0].append(triangle[0][0])
    for i in range(1, len(triangle)):
        for k in range(i + 1):
            if k == 0:
                triangle[i][k] = triangle[i][k] + triangle[i - 1][k]
            elif k == i:
                triangle[i][k] = triangle[i][k] + triangle[i - 1][k - 1]
            else:
                if triangle[i][k] + triangle[i - 1][k] > triangle[i][k] + triangle[i - 1][k - 1]:
                    triangle[i][k] += triangle[i - 1][k]
                else:
                    triangle[i][k] += triangle[i - 1][k - 1]

    answer = max(triangle[len(triangle) - 1])

    return answer