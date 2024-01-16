import itertools


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    all_numbers = set()

    for i in range(1, len(numbers) + 1):
        permutations = itertools.permutations(numbers, i)
        for perm in permutations:
            temp = int(''.join(perm))
            all_numbers.add(temp)

    for num in all_numbers:
        if is_prime(num):
            answer += 1

    return answer
