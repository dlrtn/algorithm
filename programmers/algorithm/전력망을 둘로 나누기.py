from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    count = 1

    while queue:
        vertex = queue.popleft()
        visited.add(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                count += 1
                queue.append(neighbor)
                visited.add(neighbor)

    return count


def solution(n, wires):
    answer = float('inf')

    for i in range(len(wires)):
        temp_list = wires[:i] + wires[i + 1:]

        temp_dict = {i: [] for i in range(1, n + 1)}
        s = []

        for j in temp_list:
            temp_dict[j[0]].append(j[1])
            temp_dict[j[1]].append(j[0])

        for k in range(1, n + 1):
            s.append(bfs(temp_dict, k))

        if n == len(s):
            answer = min(max(s) - min(s), answer)

    return answer
