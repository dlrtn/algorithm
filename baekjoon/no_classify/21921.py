N, X = map(int, input().split())

arr = list(map(int, input().split()))

max_1 = 0
count = 1

temp = sum(arr[:X])

if max(arr) == 0:
    print("SAD")
else :
    for i in range(0, N - X + 1):
        if max_1 < temp:
            max_1 = temp
            count = 1
        elif max_1 == temp:
            count += 1
        if i + X == N:
            break
        temp = temp - arr[i] + arr[i+X]


    print(max_1)
    print(count)