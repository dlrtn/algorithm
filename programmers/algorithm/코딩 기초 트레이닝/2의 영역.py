def solution(arr):
    first_two = 0
    last_two = len(arr)

    for i in range(len(arr) - 1, 0, -1):
        if arr[i] == 2:
            last_two = i
            break

    for i in range(len(arr)):
        if arr[i] == 2:
            first_two = i
            break

    if first_two == 0 and last_two == len(arr):
        return [-1]

    return arr[first_two:last_two + 1]
