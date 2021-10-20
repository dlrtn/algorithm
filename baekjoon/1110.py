n = int(input())
temp = n
cnt = 0
while 1:
    if n<10:
        n = (n%10)*10 + n
    else :
        n = (n%10)*10 + ((n/10+n%10))%10
    cnt+=1
    if temp==n:
        break
print(cnt)