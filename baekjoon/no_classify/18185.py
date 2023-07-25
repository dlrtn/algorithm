N = int(input())

factories = list(map(int, input().split()))

count = 0
for i in range(N):
    while factories[i]:
        if i <= N - 2 and factories[i] > 0 and factories[i + 1] > 0  and factories[i + 2] > 0:
            factories[i] -= 1
            factories[i + 1] -= 1
            factories[i + 2] -= 1
            count += 7
        elif i <= N - 1 and factories[i] > 0 and factories[i + 1] > 0:
            factories[i] -= 1
            factories[i + 1] -= 1
            count += 5
        else:
            factories[i] -= 1
            count += 3

print(count)