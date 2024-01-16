from heapq import heappush
from heapq import heappop

def solution(scoville, K):
    heap = []
    count = 0

    for i in scoville:
        heappush(heap, i)

    while True:
        if heap[0] >= K:
            return count

        if len(heap) == 1 and heap[0] < K:
            return -1

        count += 1
        heappush(heap, heappop(heap) + heappop(heap) * 2)
