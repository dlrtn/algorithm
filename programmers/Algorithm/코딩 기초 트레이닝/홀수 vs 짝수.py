def solution(num_list):
    answer_odd = []
    answer_even = []
    for i in range(len(num_list)):
        if i % 2 == 0:
            answer_even.append(num_list[i])
        else:
            answer_odd.append(num_list[i])
    if sum(answer_odd) > sum(answer_even):
        return sum(answer_odd)
    return sum(answer_even)
