def solution(numbers, hand):
    answer = ''

    now_left = '10'
    now_right = '11'

    left_list = [1, 4, 7]
    center_list = [2, 5, 8, 0]
    right_list = [3, 6, 9]

    point = [[1, 3], [0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2], [0, 3], [2, 3]]

    for i in range(len(numbers)):

        if numbers[i] in left_list:
            answer += "L"
            now_left = str(numbers[i])
        elif numbers[i] in center_list:
            num_x = point[numbers[i]][0]
            num_y = point[numbers[i]][1]

            right_x = point[int(now_right)][0]
            right_y = point[int(now_right)][1]

            left_x = point[int(now_left)][0]
            left_y = point[int(now_left)][1]

            if abs(num_x - right_x) + abs(num_y - right_y) > abs(num_x - left_x) + abs(num_y - left_y):
                answer += "L"
                now_left = str(numbers[i])
            elif abs(num_x - right_x) + abs(num_y - right_y) < abs(num_x - left_x) + abs(num_y - left_y):
                answer += "R"
                now_right = str(numbers[i])
            else:
                if hand == "right":
                    answer += "R"
                    now_right = str(numbers[i])
                else:
                    answer += "L"
                    now_left = str(numbers[i])

        elif numbers[i] in right_list:
            answer += "R"
            now_right = str(numbers[i])

    return answer
