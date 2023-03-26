def solution(picks, minerals):
    answer = 0

    hash_sum = []
    n = 5
    hash_min_list = []
    sorted_hash_min_list = []

    divide_list = [minerals[i * n:(i + 1) * n] for i in range((len(minerals) + n - 1) // n)]

    for i in range(sum(picks)):
        sum1 = 0
        if i > len(divide_list) - 1:
            break
        for j in divide_list[i]:
            if j == "diamond":
                sum1 += 25
            elif j == "iron":
                sum1 += 5
            else:
                sum1 += 1
        hash_sum.append(sum1)
        hash_min_list.append([i, sum1, divide_list[i]])

    sorted_hash_min_list = sorted(hash_min_list, key=lambda x: x[1], reverse=True)

    count = 0

    for i in range(len(picks)):
        if count == len(sorted_hash_min_list):
            break
        for j in range(picks[i]):
            now = sorted_hash_min_list.pop(0)
            for k in now[2]:
                if i == 0:
                    answer += 1
                elif i == 1:
                    if k == "diamond":
                        answer += 5
                    else:
                        answer += 1
                else:
                    if k == "diamond":
                        answer += 25
                    elif k == "iron":
                        answer += 5
                    else:
                        answer += 1
            if count == len(sorted_hash_min_list):
                break
    return answer