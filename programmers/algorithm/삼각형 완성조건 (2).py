def solution(sides):
    sides.sort()
    result_set = set()

    for i in range(sides[1] + 1, sides[0] + sides[1]):
        result_set.add(i)

    for i in range(sides[1] - sides[0] + 1, sides[1] + 1):
        result_set.add(i)

    return len(result_set)