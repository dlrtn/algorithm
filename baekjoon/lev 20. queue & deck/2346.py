import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

number_list = deque(range(1, N + 1))
queue = deque(map(int, sys.stdin.readline().rstrip().split()))

while queue:
    rotate = queue.popleft()
    print(number_list.popleft(), end=' ')
    if rotate > 0:
        number_list.rotate(-(rotate - 1))
        queue.rotate(-(rotate - 1))
    else:
        number_list.rotate(-rotate)
        queue.rotate(-rotate)
