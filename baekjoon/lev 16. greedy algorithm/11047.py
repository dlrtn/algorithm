a, b = map(int, input().split())
c = []
for i in range(a):
    temp = int(input())
    c.append(temp)
c.sort(reverse=True)
cnt = 0
for i in range(0, len(c)):
    if (b % c[temp]) == 0:
        b = b - b // c[temp]
        cnt += b % c[temp]

print(cnt)