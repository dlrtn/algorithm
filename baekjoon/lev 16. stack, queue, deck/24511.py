import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
C = list(map(int, sys.stdin.readline().rstrip().split()))

queue = deque([])
for i in range(N):
    if A[i] == 0:
        queue.appendleft(B[i])
else:
    if not queue:
        print(' '.join(list(map(str, C))))
        sys.exit()

for i in range(M):
    queue.append(C[i])
    print(queue.popleft(), end=" ")
