import math


def solution(r1, r2):
    answer = 0

    for i in range(1, r2 + 1):
        y2_squared = r2 ** 2 - i ** 2
        y1_squared = r1 ** 2 - i ** 2

        y2 = math.sqrt(y2_squared)

        if y1_squared >= 0:
            y1 = math.sqrt(y1_squared)
        else:
            y1 = 0

        answer += int(y2) - int(math.ceil(y1)) + 1

    answer *= 4

    return answer
