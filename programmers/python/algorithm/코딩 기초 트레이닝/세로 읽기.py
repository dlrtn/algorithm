def solution(my_string, m, c):
    answer = ''
    now_index = c - 1

    while now_index < len(my_string):
        answer += my_string[now_index]
        now_index += m

    return answer
