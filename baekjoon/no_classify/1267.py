N = int(input())

lst = list(map(int, input().split()))

Y_price = 0
M_price = 0
for i in lst:
    Y_price += (i // 30 + 1) * 10
    M_price += (i // 60 + 1) * 15

if Y_price < M_price:
    print('Y', Y_price)
elif Y_price > M_price:
    print('M', M_price)
else:
    print('Y', 'M', M_price)
