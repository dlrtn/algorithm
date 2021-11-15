n = int(input())
arr = list(map(int, input().split()))
stack = []
for i in range(len(arr)):
    for j in range(i, len(arr)):
        a = 0

