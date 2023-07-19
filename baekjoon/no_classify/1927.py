from queue import PriorityQueue
import sys

n = int(sys.stdin.readline())

# que = PriorityQueue()
que = []
for i in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        #if que.qsize() == 0:
        if len(que) == 0:
            print(0)
        else:
            #print(que.get())
            print(que.pop(0))
    else:
        #que.put(x)
        que.append(x)
        que.sort()
