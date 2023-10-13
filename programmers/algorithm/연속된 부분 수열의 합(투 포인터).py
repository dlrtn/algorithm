def solution(sequence, k):
    # 오름차순으로 주어진다는 것에 주목을 해보자!
    size = len(sequence)

    answer = []
    for i in range(size):
        end = i
        partition_sum = 0
        while end < size and partition_sum < k:
            partition_sum += sequence[end]
            if partition_sum == k:
                answer.append((i, end, abs(end - i)))
                break
            end += 1

    answer.sort(key=lambda x: x[2])
    print(answer)

    return [answer[0][0], answer[0][1]]


print(solution([1, 1, 1, 2, 3, 4, 5], 5))
print(solution([2, 2, 2, 2, 2], 6))
print(solution([1, 2, 3, 4, 5], 7))
