import queue


def solution(x, y, n):
    array = [-1] * (y + 1)

    bfs(x, y, n, array)

    return array[y]


def bfs(x, y, n, array):
    q = queue.Queue()
    count = 0
    q.put((x, count))
    while not q.empty():
        x, count = q.get()

        if x == y and array[x] == -1:
            array[x] = count
        count += 1
        for i in range(3):
            if i == 0 and x * 2 <= y and array[x * 2] == -1:
                array[x * 2] = count
                q.put((x * 2, count))
            if i == 1 and x * 3 <= y and array[x * 3] == -1:
                array[x * 2] = count
                q.put((x * 3, count))
            if i == 2 and 0 <= x + n <= y and array[x + n] == -1:
                array[x + n] = count
                q.put((x + n, count))
