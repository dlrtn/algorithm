N = int(input())

lst = [[0] * N for i in range(N)]
print(lst)

T = int(input())
for i in range(T):
    a, b = map(int, input().split())

    lst[a - 1][b - 1] = 1
    lst[b - 1][a - 1] = 1

for i in range(N):
    print(lst[i])