n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

def my_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)
temp = my_round(n * 0.15)
a.sort()
if n > 3:
    print(my_round((sum(a[temp:n-temp])/(n-2*temp))))
elif n == 0:
    print(0)
else :
    print(my_round(sum(a)/n))