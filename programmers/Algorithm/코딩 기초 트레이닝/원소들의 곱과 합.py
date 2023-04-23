def solution(num_list):
    mul_list = 1
    sum_list = 0

    for i in num_list:
        mul_list *= i

    if sum(num_list) ** 2 < mul_list:
        return 0
    return 1
