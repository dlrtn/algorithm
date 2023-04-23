def solution(arr):
    x = len(arr)
    y = len(arr[0])

    result = x - y

    if result == 0:
        return arr
    elif result < 0:
        for i in range(abs(result)):
            arr.append([0] * y)
    else:
        for i in range(x):
            for j in range(result):
                arr[i].append(0)
    return arr