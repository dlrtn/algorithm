def solution(n):
    answer = [[0] * 6] * 6
    queue = []
    # 오른쪽 x + 1
    # 아래 y + 1
    # 왼쪽 x - 1
    # 위 순서 y - 1
    count = 1
    x, y = 0, 0
    for i in range(n, 0, -1):
        if i == n:
            queue.append(i)
        else:
            queue.append(i)
            queue.append(i)

    for i in range(len(queue)):
        if i % 4 == 0: #오른
            # x + 1
            for j in range(queue[i]):
                print(y, x)
                print(count)
                answer[y][x] = count
                count += 1
                x += 1
        elif i % 4 == 1: #아래
            # y + 1
            for j in range(queue[i]):
                print(y, x)
                print(count)
                answer[y][x] = count
                y += 1
                count += 1
        elif i % 4 == 2: #왼
            # x - 1
            for j in range(queue[i]):
                print(y, x)
                print(count)
                answer[y][x] = count
                x -= 1
                count += 1
        elif i % 4 == 3: #위
            # y - 1
            for j in range(queue[i]):
                print(y, x)
                print(count)
                answer[y][x] = count
                y -= 1
                count += 1

    for i in range(6):
        print(answer[i])

    return answer

solution(4)