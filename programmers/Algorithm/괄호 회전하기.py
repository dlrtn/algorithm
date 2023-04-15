def solution(s):
    answer = 0

    for i in range(len(s)):
        if len(check(s[i:len(s)] + s[0:i])) == 0:
            answer += 1

    return answer

def check(s):
    stack = []

    for i in s:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] == '{' and i == '}':
                stack.pop()
            elif stack[-1] == '(' and i == ')':
                stack.pop()
            elif stack[-1] == '[' and i == ']':
                stack.pop()
            else:
                stack.append(i)

    return stack
