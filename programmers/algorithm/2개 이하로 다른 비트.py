def solution(numbers):
    answer = []

    for number in numbers:
        binary = bin(number)[2:][::-1]

        count = binary.find('0')
        if count == 0:
            answer.append(number + 1)
        elif count == -1:
            answer.append(number + 2 ** (len(str(binary)) - 1))
        else:
            answer.append(number + 2 ** (count - 1))

    return answer