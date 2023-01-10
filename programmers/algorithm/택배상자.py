def solution(order):
    stack = [] # stack을 사용하고자 함
    answer = 0 # 정답으로 제출할 겸, order의 순서 값으로 응용

    for i in range(1, len(order) + 1):
        stack.append(i)

        while len(stack) > 0:
            if stack[-1] == order[answer]:
                answer += 1
                stack.pop()
            else:
                break

    return answer
