def solution(ineq, eq, n, m):
    if ineq == '>':
        if eq == '=':
            answer = n >= m
        else:
            answer = n > m
    else:
        if eq == '=':
            answer = n <= m
        else:
            answer = n < m

    if answer:
        return 1
    return 0
