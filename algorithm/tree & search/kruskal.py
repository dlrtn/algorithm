def getParent(parent, x):
    if parent[x] == x:
        return x
    return getParent(parent, parent[x])


def unionParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def findParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)

    if a == b:
        return True
    else:
        return False


N = int(input())


class vertex:
    def __init__(self, v1, v2, cost):
        self.v1 = v1
        self.v2 = v2
        self.cost = cost


for i in range(N):
    arr = list(map(int, input().split()))
    vertex_list = []
    parent = []
    max_node = 0
    sum = 0

    for j in range(0, len(arr), 3):
        vertex_list.append(vertex(arr[j], arr[j + 1], arr[j + 2]))

    for x in vertex_list:
        max_node = max(max_node, x.v1, x.v2)

    for j in range(max_node + 1):
        parent.append(j)

    vertex_list.sort(key=lambda x: x.cost)
    for k in vertex_list:
        if not findParent(parent, k.v1, k.v2):
            unionParent(parent, k.v1, k.v2)
            sum += k.cost

    print(sum)
