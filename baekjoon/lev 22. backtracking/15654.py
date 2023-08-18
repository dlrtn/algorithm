N, M = map(int, input().split())
list = list(map(int, input().split()))
list.sort()

stack = []
def dfs():
    if len(stack) == M:
        print(' '.join(map(str, stack)))
        return

    for i in list:
        if i in stack:
            continue
        stack.append(i)
        dfs()
        stack.pop()

dfs()