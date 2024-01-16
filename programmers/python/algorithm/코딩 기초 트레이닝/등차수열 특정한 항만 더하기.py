def solution(a, d, included):
    answer = 0
    arr = [a + d * i for i in range(len(included))]
    for i in range(len(included)):
        if included[i]:
            answer += arr[i]
    return answer
열