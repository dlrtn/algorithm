def solution(a, b, c, d):
    arr = [0] * 6
    value = []
    for i in [a, b, c, d]:
        arr[i - 1] += 1

    min_value = min([a, b, c, d])
    max_value = max([a, b, c, d])

    for i in range(6):
        if arr[i] != 0:
            value.append(arr[i])

    answer = 1

    if max(value) == 4:
        return 1111 * (arr.index(max(arr)) + 1)
    elif max(value) == 3:
        return ((arr.index(max(value)) + 1) * 10 + (arr.index(min(value)) + 1)) ** 2
    elif max(value) == 2 and min(value) == 2:
        return (min_value + max_value) * (max_value - min_value)
    elif max(value) == 2:
        for i in range(len(arr)):
            if arr[i] == 1:
                answer *= i + 1
        return answer
    elif max(value) == 1:
        return min_value

    return arr