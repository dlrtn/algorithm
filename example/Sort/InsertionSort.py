def insertion_sort(arr):
    for index in range(len(arr) - 1):
        for i in range(1 + index, 0, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]  # ========= psuedo code =========#
            else:
                break

    return arr


# make random array
import random

arr = [random.randint(0, 100) for i in range(1000)]

# sort
sorted_arr = insertion_sort(arr)

# print
print(sorted_arr)
