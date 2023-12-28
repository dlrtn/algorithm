def solution(number, k):
    stack = []
    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)

    while k > 0:
        stack.pop()
        k -= 1

    return ''.join(stack)


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
print(solution('10', 1))
print(solution('21', 1))
