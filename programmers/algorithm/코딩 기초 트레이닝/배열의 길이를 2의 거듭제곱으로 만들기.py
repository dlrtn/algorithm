def solution(arr):
    array = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    for i in array:
        if len(arr) <= i:
            answer = [0] * i
            break

    for i in range(len(arr)):
        answer[i] = arr[i]

    return answer
