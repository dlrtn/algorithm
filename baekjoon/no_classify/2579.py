N = int(input())

arr = []

for i in range(N):
    arr.append(int(input()))

dp = [0] * N

if N > 3:
    dp[0] = arr[0]
    dp[1] = max(arr[0] + arr[1], arr[1])
    dp[2] = max(arr[0] + arr[2], arr[1] + arr[2])

    for i in range(3, N):
        dp[i] = max(dp[i - 2] + arr[i], arr[i - 1] + arr[i] + dp[i - 3])
    print(dp[-1])
else :
    if N == 1:
        print(arr[0])
    elif N == 2:
        print(max(arr[0] + arr[1], arr[1]))
    else :
        print(max(arr[0] + arr[2], arr[1] + arr[2]))

