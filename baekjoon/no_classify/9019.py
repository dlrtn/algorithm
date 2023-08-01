from collections import deque

T = int(input())

global min_string
min_string = ''


def bfs(num, string):
    global m, min_string
    queue = deque([(num, string)])

    while True:
        num, string = queue.popleft()

        if num == B:
            if m > len(string):
                m = len(string)
                min_string = string
            break

        if (num * 2) % 10000 not in visited:
            visited.add((num * 2) % 10000)
            queue.append(((num * 2) % 10000, string + 'D'))

        if (9999 if num == 0 else num - 1) not in visited:
            visited.add(9999 if num == 0 else num - 1)
            queue.append((9999 if num == 0 else num - 1, string + 'S'))

        if (num // 1000) + (num % 1000) * 10 not in visited:
            visited.add((num // 1000) + (num % 1000) * 10)
            queue.append(((num // 1000) + (num % 1000) * 10, string + 'L'))

        if (num // 10) + (num % 10) * 1000 not in visited:
            visited.add((num // 10) + (num % 10) * 1000)
            queue.append(((num // 10) + (num % 10) * 1000, string + 'R'))


for i in range(T):
    m = 10000
    visited = set()
    A, B = map(int, input().split())
    bfs(A, '')
    print(min_string)
