def solution(id_list, report, k):
    answer = []
    a = []

    my_set = set(report)
    my_list = list(my_set)

    for i in my_list:
        a.append(i.split())

    b = []
    cnt = 0
    for i in id_list:
        answer.append(0)
        b.append(0)
        for j in a:
            if j[1] == i:
                b[cnt] += 1
        cnt += 1

    quited = []
    for i in range(len(id_list)):
        if b[i] >= k:
            quited.append(id_list[i])

    for i in a:
        for j in quited:
            if i[1] == j:
                answer[id_list.index(i[0])] += 1

    return answer