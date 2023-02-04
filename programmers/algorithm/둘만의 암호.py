def solution(s, skip, index):
    answer = ''

    alphabet = []

    for i in range(ord('a'), ord('z') + 1):
        alphabet.append(chr(i))

    for i in list(skip):
        alphabet.remove(i)

    for i in list(s):
        answer += alphabet[(alphabet.index(i) + index) % len(alphabet)]

    return answer
