def solution(friends, gifts):
    answer = 0

    friends_index = dict()
    next_month_gift_predict = dict()
    for i in range(len(friends)):
        friends_index[friends[i]] = i
        next_month_gift_predict[friends[i]] = 0

    giver_dict = dict()
    taker_dict = dict()
    gift_indicator = dict()

    gift_table = [[0 for _ in range(len(friends))] for _ in range(len(friends))]

    for i in friends:
        giver_dict[i] = 0
        taker_dict[i] = 0

    for i in gifts:
        giver, taker = i.split(' ')

        giver_dict[giver] += 1
        taker_dict[taker] += 1

        gift_table[friends_index[giver]][friends_index[taker]] += 1

    for i in friends:
        gift_indicator[i] = giver_dict[i] - taker_dict[i]

    for i in range(len(friends)):
        # giver
        for j in range(i, len(friends)):
            # taker
            if i == j:
                continue

            # 선물 주고받은 기록이 있다.
            if gift_table[i][j] > 0 or gift_table[j][i] > 0:
                if gift_table[i][j] > gift_table[j][i]:
                    next_month_gift_predict[friends[i]] += 1

                elif gift_table[i][j] < gift_table[j][i]:
                    next_month_gift_predict[friends[j]] += 1

                else:
                    if gift_indicator[friends[i]] > gift_indicator[friends[j]]:
                        next_month_gift_predict[friends[i]] += 1

                    elif gift_indicator[friends[i]] < gift_indicator[friends[j]]:
                        next_month_gift_predict[friends[j]] += 1
            # 선물을 주고 받지 않았다.
            else:
                if gift_indicator[friends[i]] > gift_indicator[friends[j]]:
                    next_month_gift_predict[friends[i]] += 1

                elif gift_indicator[friends[i]] < gift_indicator[friends[j]]:
                    next_month_gift_predict[friends[j]] += 1
    return max(list(next_month_gift_predict.values()))


print(solution(["muzi", "ryan", "frodo", "neo"],
               ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan",
                "neo muzi"]))

print(solution(["joy", "brad", "alessandro", "conan", "david"],
               ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]))
print(solution(["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"]))
