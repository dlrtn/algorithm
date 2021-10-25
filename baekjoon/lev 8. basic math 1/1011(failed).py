global a
a=[]

def fly(x, y, n, cnt):

    x += n
    cnt += 1
    if x == y and n == 1:
        a.append(cnt)
    elif x < y and n > 0:
        fly(x, y, n-1, cnt)
        fly(x, y, n, cnt)
        fly(x, y, n+1, cnt)
    else:
        return 0
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    fly(0, y-x, 1, 0)
    print(min(a))
