def fac(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fac(n-2) + fac(n-1)
n = int(input())
print(fac(n))