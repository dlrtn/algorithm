def solution(lines):
    answer = 0
    arr = [0] * 200

    for i in lines:
        for j in range(i[0], i[1]):
            arr[j + 100] += 1

    return arr.count(2) + arr.count(3)