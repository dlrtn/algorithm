arr = list(map(int, input().split()))
str = [1, 1, 2, 2, 2, 8]

for i in range(len(arr)):
    print(str[i] - arr[i], end = ' ')
