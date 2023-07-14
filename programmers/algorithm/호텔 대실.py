def solution(book_time):
    if len(book_time) == 1:
        return 1

    time_list = [
        [int(i[0][:2]) * 60 + int(i[0][3:]), int(i[1][:2]) * 60 + int(i[1][3:])]
        for i in book_time
    ]

    time_list.sort(key=lambda x: (x[0], x[1]))

    answer = 0

    while time_list:
        answer += 1
        current_time = time_list.pop(0)
        i = 0
        while i < len(time_list):
            if current_time[1] + 10 <= time_list[i][0]:
                current_time = time_list[i]
                time_list.pop(i)
            else:
                i += 1

    return answer
