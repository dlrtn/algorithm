from collections import deque
T = int(input())

for i in range(T):
    A, B = map(int, input().split())



command = ['D', 'S', 'L', 'R']
def dfs():    

    for i in range(4):
