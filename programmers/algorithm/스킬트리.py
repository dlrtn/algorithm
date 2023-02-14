def solution(skill, skill_trees):
    answer = 0

    for i in skill_trees:
        temp = [x for x in i if x in list(skill)]
        if temp == list(skill):
            answer += 1

        for i in range(len(skill)):
            if list(skill)[:i] == temp:
                answer += 1

    return answer