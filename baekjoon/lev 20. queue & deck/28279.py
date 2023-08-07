import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

queue = deque()
for i in range(N):
    temp = sys.stdin.readline().rstrip()

    if temp[0] == '1':
        queue.appendleft(temp[2:])

    elif temp[0] == '2':
        queue.append(temp[2:])

    elif temp[0] == '3':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())

    elif temp[0] == '4':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())

    elif temp[0] == '5':
        print(len(queue))

    elif temp[0] == '6':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif temp[0] == '7':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif temp[0] == '8':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

