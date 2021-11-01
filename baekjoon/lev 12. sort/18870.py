n = int(input())
arr = list(map(int, input().split()))
a = {}
cnt = 0
str = arr
result = set(arr)
result1 = list(result)
result1.sort()
for i in result1:
    a[i] = cnt
    cnt+=1
for i in range(n):
    print(a[str[i]], end=' ')