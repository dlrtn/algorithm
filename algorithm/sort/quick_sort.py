s = list(map(int, input().split()))
c = list(map(int, input().split()))


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left, right = [], []
    for i in arr:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + quick_sort(right)


print(quick_sort(s))
