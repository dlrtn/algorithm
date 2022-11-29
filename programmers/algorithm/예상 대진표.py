def solution(n, a, b):
    answer = 1

    while abs(a - b) != 1 or min(a, b) % 2 == 0:
        answer += 1
        if a % 2 == 0:
            a = a // 2
        else:
            a = a // 2 + 1

        if b % 2 == 0:
            b = b // 2
        else:
            b = b // 2 + 1

    return answer