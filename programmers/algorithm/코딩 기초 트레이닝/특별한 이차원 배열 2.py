def solution(arr):
    for i in range(len(arr[0])):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1
