def solution(arr1, arr2):
    answer = []

    # i는
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr2[0])):
            t = 0
            for k in range(len(arr1[0])):
                t += arr2[k][j] * arr1[i][k]
            temp.append(t)
        answer.append(temp)

    return answer