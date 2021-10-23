n = int(input())
for i in range(n):
    arr = str(input())
    cnt=1
    sum=0
    for i in range(len(arr)):
        if arr[i] == 'O':
            sum += cnt
            cnt += 1
        else :
            cnt = 1

    print(sum)