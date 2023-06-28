a, b = map(int, input().split())
c, d = map(int, input().split())


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


num = c * b + d * a
den = b * d

print(num // gcd(num, den), den // gcd(num, den))
