from queue import PriorityQueue
import sys

N = int(sys.stdin.readline())

que = PriorityQueue()
for i in range(N):
    a = int(sys.stdin.readline())

    if a == 0:
        if que.qsize() == 0:
            print(0)
        else:
            print(-que.get())
    else:
        que.put(-a)
