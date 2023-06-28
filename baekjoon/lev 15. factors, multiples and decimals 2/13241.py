a, b = map(int, input().split())

if a >= b:
    max_num = a
    min_num = b
else:
    max_num = b
    min_num = a


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(max_num // gcd(max_num, min_num) * min_num)
