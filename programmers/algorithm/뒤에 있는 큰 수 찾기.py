def solution(numbers):
    stack = []
    answer = [-1 for i in range(len(numbers))]

    for i in range(len(numbers)):
        while len(stack) > 0 and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop(-1)] = numbers[i]

        stack.append(i)

    return answer
