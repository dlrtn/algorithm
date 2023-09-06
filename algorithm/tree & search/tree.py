class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


set = {}

N = list(map(str, input().split()))

for i in range(0, len(N), 2):
    if N[i] not in set:
        if N[i + 1] not in set:
            set[N[i]] = node(N[i])
            set[N[i + 1]] = node(N[i + 1])
            set[N[i]].left = set[N[i + 1]]
        else:
            set[N[i]] = node(N[i])
            set[N[i]].left = set[N[i + 1]]

    else:
        if N[i + 1] not in set:
            set[N[i + 1]] = node(N[i + 1])

            if set[N[i]].left is None:
                set[N[i]].left = set[N[i + 1]]
            else:
                set[N[i]].right = set[N[i + 1]]
        else:
            set[N[i]].right = set[N[i + 1]]

for i in set:
    print(set[i].data)
    if set[i].left != None:
        print(set[i].left.data)
    if set[i].right != None:
        print(set[i].right.data)
    print("------------------")
