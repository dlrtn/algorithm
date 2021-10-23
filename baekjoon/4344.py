n = int(input())
for i in range(n):
    arr = [int(x) for x in input().split()]
    cnt = 0
    for j in range(arr[0]):
        if (arr[j+1] > ((sum(arr)-arr[0])//arr[0])):
            cnt += 1
    print("{:.3f}%".format((float(cnt)/float(arr[0]))*100))