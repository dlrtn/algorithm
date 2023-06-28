while True:
    n = int(input())
    if n < 0:
        break

    sum = 0
    fac = []
    for i in range(1, n):
        if n % i == 0:
            sum += i
            fac.append(i)

    if sum == n:
        print(n, '=', ' + '.join(map(str, fac)))
    else:
        print(n, 'is NOT perfect.')
