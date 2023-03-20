import heapq

# 각 라운드마다 일정값을 push해준 후, 길이가 k를 넘어가면 pop해주어 최댓값들을 연산에서 제거하는 문제
def solution(n, k, enemy):
    temp = []

    for i in range(len(enemy)):
        heapq.heappush(temp, enemy[i])

        if len(temp) > k:
            n -= heapq.heappop(temp)

        if n < 0:
            return i

    return len(enemy)
