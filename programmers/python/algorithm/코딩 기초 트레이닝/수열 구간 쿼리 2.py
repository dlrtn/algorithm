def solution(arr, queries):
    answer = []

    for i in queries:
        temp = []
        for j in range(i[0], i[1] + 1):
            if i[2] < arr[j]:
                temp.append(arr[j])
        if len(temp) == 0:
            answer.append(-1)
        else:
            answer.append(min(temp))
    return answer
