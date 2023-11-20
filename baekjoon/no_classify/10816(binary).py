import sys

N = int(sys.stdin.readline().rstrip())
N_array = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
M_array = list(map(int, sys.stdin.readline().rstrip().split()))

N_array.sort()


def lower_bound(N, array):
    left = 0
    right = len(array)

    while left < right:
        median = (left + right) // 2
        if array[median] >= N:
            right = median
        else:
            left = median + 1

    return left


def higher_bound(N, array):
    left = 0
    right = len(array)

    while left < right:
        median = (left + right) // 2
        if array[median] > N:
            right = median
        else:
            left = median + 1

    return left


for i in M_array:
    print(higher_bound(i, N_array) - lower_bound(i, N_array), end=' ')
