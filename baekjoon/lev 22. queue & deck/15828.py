from collections import deque

n = int(input())
x = 0

q = deque()

while True:
    x = int(input())
    if x == -1:
        break
    elif x == 0:
        q.popleft()
    else:
        if len(q) < n:
            q.append(x)


if len(q) == 0:
    print(empty)
else :
    for i in q:
        print(i, end = ' ')

