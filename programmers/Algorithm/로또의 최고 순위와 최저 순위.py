def solution(lottos, win_nums):
    n = lottos.count(0)
    count = 0
    for i in lottos:
        for j in win_nums:
            if i == j:
                count += 1
    if count > 1:
        return [7-count-n, 7-count]
    elif n == 0:
        return [6, 6]
    else:
        return [7-count-n, 6]