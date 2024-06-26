def solution(arr):
    answer = []
    i = 0
    while True:
        if i >= len(arr):
            break

        if len(answer) == 0:
            answer.append(arr[i])
            i += 1

        elif answer[-1] == arr[i]:
            del answer[-1]
            i += 1
        else:
            answer.append(arr[i])
            i += 1

    if len(answer) == 0:
        return [-1]

    return answer
