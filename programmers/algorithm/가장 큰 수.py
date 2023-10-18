import itertools


def solution(numbers):
    answer = ''

    max_number = 0
    for permutations in itertools.permutations(numbers):
        num = int(''.join(list(map(str, permutations))))
        max_number = max(num, max_number)

    return max_number


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
