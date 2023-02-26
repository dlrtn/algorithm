arr = list(map(int, input().split()))
n = -1
for i in range(len(arr) - 1):
    if n == 1 and arr[i] > arr[i + 1]:
        n = -1
        print("mixed")
        exit()
    elif n == 0 and arr[i] < arr[i + 1]:
        n = -1
        print("mixed")
        exit()
    elif arr[i] < arr[i + 1]:
        n = 1
    elif arr[i] > arr[i + 1]:
        n = 0

if n == 1:
    print('ascending')
else:
    print('descending')
