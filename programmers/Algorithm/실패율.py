def solution(N, stages):
    answer = []
    a = {}
    temp = len(stages)
    for i in range(1, N + 1):
        if temp != 0:
            a[i] = stages.count(i) / temp
        else:
            a[i] = 0
        temp -= stages.count(i)

    for i in sorted(a.items(), key=lambda x: x[1], reverse=True):
        answer.append(i[0])

    return answer

//사칙연산이 많은 문제에서 runtime error가 발생했을 때는 division by zero error가 아닐지 생각해보자!