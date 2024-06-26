import copy

def solution(arr, queries):
    answer = copy.deepcopy(arr)

    for i in queries:
        for j in range(i[0], i[1] + 1):
            if j % i[2] == 0:
                answer[j] += 1

    return answer
