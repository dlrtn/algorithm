n = int(input())
def prime(num):
    for j in range(2, num):
        if num % j == 0:
            return 0
    return 1
x=0
y=0
for i in range(n):
    min = 10000
    num = int(input())

    for j in range(2, num):
        if prime(j):
            if (prime(num - j)):
                if min > abs(j - (num - j)):
                    min = abs(j - (num - j))
                    x = j
                    y = num - j
    print(x, y)



