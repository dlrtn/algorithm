import sys
import heapq

N = int(sys.stdin.readline())
que = []
for i in range(N):
    for j in list(map(int, sys.stdin.readline().split())):
        if len(que) >= N and que[0] < j:
            heapq.heappop(que)
            heapq.heappush(que, j)
        elif len(que) < N:
            heapq.heappush(que, j)
        else:
            pass

print(que[0])
