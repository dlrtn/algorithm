def solution(files):
    lis = [];

    for i in files:
        head_flag = True
        number_flag = False
        tail_flag = False
        temp_head = ''
        temp_number = ''
        temp_tail = ''

        for j in i:
            if j.isdigit() and head_flag:
                head_flag = False
                number_flag = True

            if not j.isdigit() and number_flag:
                number_flag = False
                tail_flag = True

            if number_flag:
                if j == '0' and temp_number == '':
                    continue
                temp_number += j
            if head_flag:
                temp_head += j
            if tail_flag:
                temp_tail += j

        lis.append((i, temp_head, temp_number, temp_tail))
    answer = sorted(lis, key=lambda x: (x[1].lower(), int(x[2])))
    answers = []
    for i in answer:
        answers.append(i[0])

    return answers
