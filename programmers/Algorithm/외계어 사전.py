def solution(spell, dic):
    count = 0

    for i in dic:
        count = 0
        for j in spell:
            if j in i:
                count += 1
        if count == len(spell):
            return 1

    return 2