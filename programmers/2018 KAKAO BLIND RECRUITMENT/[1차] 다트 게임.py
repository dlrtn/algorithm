def solution(dart_result):
    dic = {'S': 1, 'D': 2, 'T': 3}
    score = []
    expression = list(dart_result)
    count = 0
    for i in range(len(expression)):
        if expression[i].isdigit():
            print(expression[i + 1])

            if expression[i + 1].isdigit():
                score.append(int(''.join(expression[i:i + 2])) ** dic[expression[i + 2]])
            else:
                score.append(int(expression[i]) ** dic[expression[i + 1]])
            count += 1

        if expression[i] == '*':

            if count == 1:
                score[count - 1] *= 2
            else:
                score[count - 2] *= 2
                score[count - 1] *= 2

        if expression[i] == '#':
            score[count - 1] *= -1

    return sum(score)
