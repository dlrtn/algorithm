a = []
a = list(map(int, input().split()))
answer = 0

if min(a) == max(a):
    answer += 10000
    answer += a[0] * 1000

elif a[0] == a[1] and a[1] != a[2]:
    answer += 1000
    answer += a[0] * 100

elif a[1] == a[2] and a[0] != a[2]:
    answer += 1000
    answer += a[1] * 100

elif a[0] == a[2] and a[0] != a[1]:
    answer += 1000
    answer += a[0] * 100

else :
    answer += max(a) * 100

print(answer)