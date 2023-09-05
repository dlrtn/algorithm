N = int(input())
arr = list(map(int, input().split()))
number = int(input())


def binary_search(arr, number, answer):
    median = len(arr) // 2
    if len(arr) == 0:
        return -1

    if arr[median] == number:
        return answer + median + 1
    elif arr[median] > number:
        return binary_search(arr[:median], number, answer)
    else:
        return binary_search(arr[median + 1:], number, answer + median + 1)


print(binary_search(arr, number, 0))
