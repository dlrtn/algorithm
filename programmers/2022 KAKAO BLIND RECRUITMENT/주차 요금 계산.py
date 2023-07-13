def convert(n, base):
    T = "0123456789ABCDEF"
    result = ''

    while n > 0:
        n, r = divmod(n, base)
        result = T[r] + result

    return result


def solution(n, t, m, p):
    answer = ''
    converted = ''

    for i in range(t * m):
        converted += convert(i, n)

    for i in range(t):
        answer += converted[i * m + p - 1]

    return answer
