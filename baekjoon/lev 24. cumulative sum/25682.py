import sys

N, M, K = map(int, sys.stdin.readline().split())

arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

def cumulative_sum(arr, color):
    prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(M):
            if (i + j) % 2 == 0:
                value = arr[i][j] != color
            else:
                value = arr[i][j] == color
            prefix_sum[i + 1][j + 1] = prefix_sum[i][j + 1] + prefix_sum[i + 1][j] - prefix_sum[i][j] + value
    return prefix_sum

B_cumulative_sum = cumulative_sum(arr, 'B')
W_cumulative_sum = cumulative_sum(arr, 'W')

def minimal_board(prefix_sum, K):
    count = sys.maxsize
    for i in range(1, N - K + 2):
        for j in range(1, M - K + 2):
            count = min(count, prefix_sum[i + K - 1][j + K - 1] - prefix_sum[i + K - 1][j - 1] - prefix_sum[i - 1][j + K - 1] + prefix_sum[i - 1][j - 1])
    return count

min_B = minimal_board(B_cumulative_sum, K)
min_W = minimal_board(W_cumulative_sum, K)

print(min(min_B, min_W))
