def solution(keymap, targets):
    answer = []
    key_dic = {}

    for i in keymap:
        for j in range(len(i)):
            if i[j] in key_dic.keys():
                if j + 1 > key_dic[i[j]]:
                    pass
                else:
                    key_dic[i[j]] = j + 1
            else:
                key_dic[i[j]] = j + 1

    for i in targets:
        temp = 0
        for j in i:
            if j in key_dic.keys():
                temp += key_dic[j]
            else:
                temp = 0
                break
        if temp == 0:
            answer.append(-1)
        else:
            answer.append(temp)

    return answer