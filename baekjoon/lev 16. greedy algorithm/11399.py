n = int(input())
a = list(map(int, input().split()))
a.sort()
sum = 0
cnt = n
for i in a:
    sum += cnt * i
    cnt -= 1
print(sum)
