num, k = map(int, input().split())

for i in range(1, num + 1):
    if num % i == 0:
        if k == 1:
            print(i)
            k -= 1
            break
        k -= 1

if k != 0:
    print(0)