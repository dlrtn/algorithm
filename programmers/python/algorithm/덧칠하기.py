def solution(n, m, section):
    answer = 0

    color_list = [1] * n

    for i in section:
        color_list[i - 1] = 0

    for i in range(len(color_list)):
        if color_list[i] == 0:
            answer += 1
            for j in range(m):
                if i + j >= n:
                    break
                color_list[i + j] = 1

    return answer