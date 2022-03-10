a = int(input())


for i in range(a):
    arr = []
    arr.append(1)
    arr.append(1)
    arr.append(1)
    c = int(input())
    for i in range(3, c):
        arr.append(arr[i-3]+arr[i-2])
    print(arr[c-1])