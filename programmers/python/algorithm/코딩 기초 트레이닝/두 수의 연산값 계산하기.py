def solution(a, b):
    answer = 0

    first = 2 * a * b
    second = int(str(a) + str(b))

    if first > second:
        return first

    return second
