arr = list(map(int, input().split()))
str = []
s = 0
aa = []
for i in range(arr[0]):
    str.append(list(map(int, input().split())))

for i in range(arr[0]):
    s += sum(str[i])
temp = s // (arr[0] * arr[1])
temp1 = temp + 1
sum1 = 0
sum2 = 0
t1 = arr[2]
t2 = arr[2]
for i in range(arr[0]):
    for j in range(arr[1]):
        if str[i][j] < temp:
            sum1 += (temp - str[i][j])
            t1 -= 1
        elif str[i][j] > temp:
            sum1 += (str[i][j] - temp) * 2
            t1 += 1
        else :
            pass
for i in range(arr[0]):
    for j in range(arr[1]):
        if str[i][j] < temp1:
            sum2 += (temp1 - str[i][j])
            t2 -= 1
        elif str[i][j] > temp1:
            sum2 += (str[i][j] - temp1) * 2
            t2 += 1
        else :
            pass
if t1 < 0 or sum2 < sum1:
    print(sum2, end = ' ')
    print(temp1)
else :
    print(sum1, end = ' ')
    print(temp)