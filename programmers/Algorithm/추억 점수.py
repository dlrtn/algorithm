def solution(name, yearning, photo):
    answer = []

    for i in photo:
        result_sum = 0
        for j in name:
            if j in i:
                result_sum += yearning[name.index(j)]
        answer.append(result_sum)

    return answer