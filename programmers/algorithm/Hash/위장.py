def solution(clothes):
    answer = 0
    clothes_count = []
    clothes_list = []

    for i in clothes:
        if i[1] not in clothes_list:
            clothes_count.append([i[1], 1])
            clothes_list.append(i[1])
        else:
            for j in clothes_count:
                if j[0] == i[1]:
                    j[1] += 1

    gob = 1
    if len(clothes_count) == 1:
        return clothes_count[0][1]
    else:
        for i in clothes_count:
            gob *= i[1] + 1
    answer += gob - 1
    return answer