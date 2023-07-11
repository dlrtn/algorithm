def solution(msg):
    dic = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
        'I': 9,
        'J': 10,
        'K': 11,
        'L': 12,
        'M': 13,
        'N': 14,
        'O': 15,
        'P': 16,
        'Q': 17,
        'R': 18,
        'S': 19,
        'T': 20,
        'U': 21,
        'V': 22,
        'W': 23,
        'X': 24,
        'Y': 25,
        'Z': 26
    }
    answer = []

    while msg:
        for i in range(len(msg), 0, -1):
            if msg[:i] in dic:
                answer.append(dic[msg[:i]])
                dic[msg[:i + 1]] = len(dic) + 1
                msg = msg[i:]
                break

    return answer

