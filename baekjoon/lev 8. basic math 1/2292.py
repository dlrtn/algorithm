n = int(input())
n = n - 1
cnt = 1
while 1:
    if n <= 0:
        break
    n = n - 6 * cnt
    cnt+=1
print(cnt)