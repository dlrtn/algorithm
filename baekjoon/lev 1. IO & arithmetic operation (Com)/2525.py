a,b = map(int, input().split())
c = int(input())

answer = a * 60 + b + c
print((answer//60)%24, answer%60)

