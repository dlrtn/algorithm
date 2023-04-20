def QuickSort(arr: list):
    if len(arr) <= 1:
        return arr

    left, right = [], []
    pivot = arr[0]

    for index in range(1, len(arr)):
        if arr[index] < pivot:
            left.append(arr[index])
        else:
            right.append(arr[index])

    return QuickSort(left) + [pivot] + QuickSort(right)

import random

data_list = random.sample(range(100), 100)

print(QuickSort(data_list))