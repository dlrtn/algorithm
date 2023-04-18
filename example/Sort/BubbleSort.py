import random
import time

# Bubble Sort WithOut Flag
def bubbleSort(arr: list):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Bubble Sort With Flag
def bubblSortWithFlag(arr: list):
    for i in range(len(arr)):
        flag = False
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
        if not flag:
            break

# act 5 times
for i in range(5):
    # 2 version of bubble sort time check with random number array
    test_arr = [random.randint(0, 100) for i in range(10000)]

    print(len(test_arr))

    # start time
    first_start = time.time()
    # sort
    sorted_arr = bubbleSort(test_arr)
    # end time
    first_end = time.time()
    # print time

    # start time
    second_start = time.time()
    # sort
    sorted_arr = bubblSortWithFlag(test_arr)
    # end time
    second_end = time.time()

    # print time
    print(first_end - first_start, second_end - second_start)

for i in range(5):
    # 2 version of bubble sort time check with random number array
    test_arr = [random.randint(0, 100) for i in range(10000000)]

    print(len(test_arr))

    # start time
    first_start = time.time()
    # sort
    sorted_arr = sorted(test_arr)
    # end time
    first_end = time.time()

    print(first_end - first_start)