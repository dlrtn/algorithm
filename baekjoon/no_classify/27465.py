n = int(input())

temp = n

while True:
    temp += 1
    cnt = 0
    for i in range(2, int(temp ** 0.5)):
        if n % i == 0:
            cnt += 1
    if cnt != 0:
        print(temp)
        break
