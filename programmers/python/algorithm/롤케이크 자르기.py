from collections import Counter


def solution(topping):
    answer = 0
    little = Counter(topping)
    big = set()

    for i in topping:
        little[i] -= 1

        if little[i] == 0:
            del little[i]

        big.add(i)

        if len(little) == len(big):
            answer += 1

    return answer
