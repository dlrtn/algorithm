from queue import PriorityQueue
import sys

N = int(sys.stdin.readline())

que = PriorityQueue()

for i in range(N):
    que.put(int(sys.stdin.readline()))

sum = 0
temp = 0
for i in range(N):
    

print(sum)
