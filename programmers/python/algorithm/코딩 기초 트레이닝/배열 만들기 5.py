def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        part = int(i[s:s+l])
        if part > k:
            answer.append(part)
    return answer
