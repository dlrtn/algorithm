import copy
import itertools
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
lab = list()
for i in range(N):
    lab.append(list(map(int, sys.stdin.readline().rstrip().split())))

void = []
start = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            void.append((i, j))
        if lab[i][j] == 2:
            start.append((i, j))

test_case = list(itertools.combinations(void, 3))


def bfs(map):
    queue = deque()
    for i in start:
        queue.append(i)
    while queue:
        x, y = queue.popleft()
        if x + 1 < N and map[x + 1][y] == 0:
            map[x + 1][y] = 2
            queue.append((x + 1, y))
        if x - 1 >= 0 and map[x - 1][y] == 0:
            map[x - 1][y] = 2
            queue.append((x - 1, y))
        if y + 1 < M and map[x][y + 1] == 0:
            map[x][y + 1] = 2
            queue.append((x, y + 1))
        if y - 1 >= 0 and map[x][y - 1] == 0:
            map[x][y - 1] = 2
            queue.append((x, y - 1))

    count = 0
    for x in range(N):
        for y in range(M):
            if map[x][y] == 0:
                count += 1

    return count


answer_count = 0
for i in test_case:
    temp = copy.deepcopy(lab)
    temp[i[0][0]][i[0][1]] = 1
    temp[i[1][0]][i[1][1]] = 1
    temp[i[2][0]][i[2][1]] = 1

    answer_count = max(answer_count, bfs(temp))
print(answer_count)
