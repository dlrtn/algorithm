def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

import random

arr = [random.randint(0, 100) for i in range(1000)]

# sort
sorted_arr = selection_sort(arr)

# print
print(sorted_arr)