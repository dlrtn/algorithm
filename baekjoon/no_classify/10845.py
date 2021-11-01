n = int(input())
queue = []
for i in range(n):
    str = input()
    if 'push' in str:
        queue.append(str[5:])
    if 'front' in str:
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    if 'pop' in str:
        if len(queue) > 0:
            print(queue[0])
            queue.remove(queue[0])
        else:
            print(-1)
    if 'size' in str:
        print(len(queue))
    if 'empty' in str:
        if len(queue) > 0:
            print(0)
        else:
            print(1)
    if 'back' in str:
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)