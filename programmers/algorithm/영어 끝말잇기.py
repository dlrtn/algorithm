def solution(n, words):
    answer = []

    for i in range(len(words)):
        if 0 < i < len(words):
            if words[i - 1][-1] != words[i][0]:
                return [i % n + 1, i // n + 1]

        if words[i] in answer:
            return [i % n + 1, i // n + 1]
        else:
            answer.append(words[i])

    return [0, 0]
