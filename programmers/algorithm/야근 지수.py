import heapq


def solution(n, works):
    answer = 0

    heap = []

    for i in works:
        heapq.heappush(heap, (-i, i))

    while n > 0:
        max_num = heapq.heappop(heap)
        n -= 1
        heapq.heappush(heap, (max_num[0] + 1, max_num[1] - 1))

    for i in heap:
        if i[1] < 0 or i[0] > i[1]:
            continue
        answer += i[1] ** 2

    return answer
