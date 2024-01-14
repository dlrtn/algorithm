import itertools

def solution(orders, course):
    answer = []

    combinations_list = []

    for i in range(len(orders)):
        orders[i] = ''.join(sorted(list(orders[i])))

    for i in course:
        temp_set = set()
        for j in orders:
            temp_set = temp_set | set(itertools.combinations(j, i))

        combinations_list.append(list(set(temp_set)))

    for i in combinations_list:
        temp_answer = []
        max_count = 0
        for j in i:
            count = 0
            for k in orders:
                ccount = 0
                for x in j:
                    if x in k:
                        ccount += 1

                if ccount == len(j):
                    count += 1

            if count >= 2:
                if count > max_count:
                    max_count = count
                    temp_answer.clear()
                    temp_answer.append((''.join(sorted(list(j)))))
                elif count == max_count:
                    temp_answer.append((''.join(sorted(list(j)))))

        answer.append(temp_answer)

    a = []
    for i in answer:
        for j in i:
            a.append(j)

    return sorted(a)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))