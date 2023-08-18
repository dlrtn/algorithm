N, M = map(int, input().split())
list = list(map(int, input().split()))

list.sort()
stack = []


def dfs(n=0):
    if len(stack) == M:
        temp = ' '.join(map(str, stack))
        print(temp)
        return

    for i in range(n, N):
        stack.append(list[i])
        dfs(i)
        stack.pop(-1)


dfs()
