def solution(records):
    user = {}

    for record in records:
        temp = record.split(' ')
        action = temp[0]
        user_id = temp[1]
        if action == 'Enter' or action == 'Change':
            nickname = temp[2]
            user[user_id] = nickname

    answer = []

    for record in records:
        temp = record.split(' ')
        action = temp[0]
        user_id = temp[1]

        if action == 'Enter':
            answer.append(f'{user[user_id]}님이 들어왔습니다.')
        elif action == 'Leave':
            answer.append(f'{user[user_id]}님이 나갔습니다.')

    return answer
