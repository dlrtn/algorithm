N = int(input())

array = []
for i in range(N):
    array.append(list(map(int, input().split())))

for i in range(N):
    print(array[i])
