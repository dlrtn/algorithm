import sys

N = int(sys.stdin.readline())
line_count = int(sys.stdin.readline())
line_list = []
parent = [i for i in range(101)]


for i in range(1, N + 1):
    parent[i] = i

for _ in range(line_count):
    line_list.append(list(map(int, sys.stdin.readline().split())))

def find_parent(x):
    if parent[x] == x:
        return x
    return find_parent(parent[x])

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(line_count):
    union_parent(line_list[i][0], line_list[i][1])

print(parent.count(1) - 1)
