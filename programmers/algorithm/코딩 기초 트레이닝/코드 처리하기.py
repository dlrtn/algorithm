def solution(code):
    answer = ''
    mode = False

    for i in range(len(code)):
        if mode:
            if code[i] == '1':
                mode = not mode
            else:
                if i % 2 == 1:
                    answer += code[i]
        else:
            if code[i]  == '1':
                mode = not mode
            else:
                if i % 2 == 0:
                    answer += code[i]

    if len(answer) == 0:
        return "EMPTY"

    return str(answer)
