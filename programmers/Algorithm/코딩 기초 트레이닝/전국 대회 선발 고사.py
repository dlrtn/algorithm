def solution(rank, attendance):
    answer = []
    arr = []
    dic = {}
    for i in range(len(rank)):
        if attendance[i]:
            answer.append(rank[i])
            arr.append(i)
            dic[rank[i]] = i
    answer.sort()

    return dic[answer[0]] * 10000 + dic[answer[1]] * 100 + dic[answer[2]]
