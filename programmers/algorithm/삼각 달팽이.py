def solution(n):
    answer = []

    arr = [[] for i in range(n)]
    control = 0
    count = 1
    x = -1
    for i in range(n, 0, -1):
        for j in range(i):
            print(x)
            if control == 0:
                if x < n - 1:
                    x += 1
                arr[x].append(count)

            elif control == 1:
                arr[x].append(count)

            elif control == 2:
                if x >= 0:
                    x -= 1
                arr[x].append(count)
            count += 1

        if control == 0:
            control = 1
        elif control == 1:
            control = 2
        else:
            control = 0
        print(i)

        print(arr)
    return answer

solution(5)