import itertools
import re

def solution(user_id, banned_id):
    new_banner_id = []
    for i in banned_id:
        new_banner_id.append(i.replace('*', '.'))
    total = list(itertools.permutations(user_id, len(banned_id)))

    answer_set = set()
    for i in total:
        if is_banned(i, new_banner_id):
            item = list(i)
            item.sort()
            answer_set.add(''.join(item))

    return len(answer_set)

def is_banned(user_id, banned_id):
    for i in range(len(user_id)):
        p = re.compile(banned_id[i])
        match = p.match(user_id[i])
        if match is None or match.end() != len(user_id[i]):
            return False

    return True



print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))