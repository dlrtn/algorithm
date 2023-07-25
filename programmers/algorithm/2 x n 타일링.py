def solution(n):
    arr = [1, 2]

    for i in range(2, n + 1):
        arr.append((arr[i - 2] + arr[i - 1])  % 1000000007)

    return arr[n - 1]
