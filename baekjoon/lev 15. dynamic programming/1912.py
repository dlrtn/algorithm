N = int(input())

A = list(map(int, input().split()))
arr = []

arr.append(A[0])
for i in range(1, N):
    if (A[i] + arr[i-1]) > A[i]:
        arr.append(A[i] + arr[i-1])
    else:
        arr.append(A[i])

print(max(arr))