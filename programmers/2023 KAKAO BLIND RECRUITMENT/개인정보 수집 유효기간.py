def solution(today, terms, privacies):
    answer = []
    today_num = int(today[0:4]) * 12 * 28 + int(today[5:7]) * 28 + int(today[8:10])
    cnt_num = []

    for i in range(len(privacies)):
        cnt_num.append(int(privacies[i][0:4]) * 12 * 28 + int(privacies[i][5:7]) * 28 + int(privacies[i][8:10]))

    for i in range(len(privacies)):
        for j in terms:
            if j[0] == privacies[i][-1]:
                cnt_num[i] += int(j[2:]) * 28

    for i in range(len(privacies)):
        if today_num >= cnt_num[i]:
            answer.append(i + 1)

    return answer