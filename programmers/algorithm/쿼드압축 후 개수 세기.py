import math


def solution(arr):
    answer = []
    z_count = 0
    o_count = 0

    def divide(x, y, N):
        nonlocal z_count
        nonlocal o_count
        print('now_x : ', x, 'now_y : ', y, 'now_N : ', N)

        zero_count = 0
        one_count = 0

        for i in range(y, y + 2 ** N):
            for j in range(x, x + 2 ** N):
                if arr[i][j] == 0:
                    zero_count += 1
                else:
                    one_count += 1

        print("zero_count = ", zero_count, "one_count = ", one_count)

        if zero_count == (2 ** N) ** 2:
            z_count += 1
            print("z_count = ", z_count, "o_count = ", o_count)
        elif one_count == (2 ** N) ** 2:
            o_count += 1
            print("z_count = ", z_count, "o_count = ", o_count)
        elif N > 1:
            divide(x, y, N - 1)
            divide(x + 2 ** (N - 1), y, N - 1)
            divide(x, y + 2 ** (N - 1), N - 1)
            divide(x + 2 ** (N - 1), y + 2 ** (N - 1), N - 1)
        else:
            z_count += zero_count
            o_count += one_count
            print("z_count = ", z_count, "o_count = ", o_count)

    N = int(math.log2(len(arr)))
    divide(0, 0, N)

    return [z_count, o_count]


arr = [[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1]]

print(solution(arr))
