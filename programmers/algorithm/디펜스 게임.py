def solution(n, k, enemy):
    for i in range(len(enemy)):
        arr = enemy[:i + 1]

        if sum(sorted(arr)[:-k]) > n:
            return i

    return len(enemy)